"""Ingest firm-level documents (LP reports, pitch decks, etc.) into data/documents.json.

Unlike append_docs.py, these docs are not linked to any deal — they describe
the firm itself across funds. Persisted with deal_id=null in documents.json
and given the 'firm' slug for doc_id numbering (doc_firm_001, doc_firm_002...).

Default mode stages only. --commit appends to data/documents.json and runs
the consistency check.

Requires ANTHROPIC_API_KEY in environment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from services.ingestion.persistence import (
    commit_appended_docs_to_fixtures,
    write_append_staging,
)
from services.ingestion.schemas import FileRef
from services.ingestion.tagger import tag_document
from services.ingestion.taxonomy import TaxonomyGateError
from services.ingestion.triage import primaries, triage


DOC_ID_RE = re.compile(r"^doc_(?P<slug>.+)_(?P<n>\d+)$")
FIRM_SLUG = "firm"
FIRM_CODENAME = "Atlas Crossing Partners"


def _sha1_of(path: Path, chunk_size: int = 1 << 20) -> str:
    h = hashlib.sha1()
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


def _file_ref(abs_path: Path, root: Path) -> FileRef:
    stat = abs_path.stat()
    try:
        rel = str(abs_path.relative_to(root))
    except ValueError:
        rel = abs_path.name
    return FileRef(
        path=rel,
        abs_path=abs_path,
        size_bytes=stat.st_size,
        mtime=datetime.fromtimestamp(stat.st_mtime),
        sha1=_sha1_of(abs_path),
    )


def _next_doc_index() -> int:
    docs_path = Path(__file__).resolve().parent.parent / "data" / "documents.json"
    docs = json.loads(docs_path.read_text())["documents"]
    max_n = 0
    for d in docs:
        m = DOC_ID_RE.match(d["doc_id"])
        if m and m.group("slug") == FIRM_SLUG:
            n = int(m.group("n"))
            if n > max_n:
                max_n = n
    return max_n + 1


def _iter_paths(args_paths: list[Path]) -> list[Path]:
    """Expand directories recursively; pass through files as-is."""
    resolved: list[Path] = []
    for p in args_paths:
        p = p.resolve()
        if p.is_dir():
            resolved.extend(sorted(q for q in p.rglob("*") if q.is_file() and not q.name.startswith(".")))
        elif p.is_file():
            resolved.append(p)
        else:
            print(f"error: not a file or directory: {p}", file=sys.stderr)
            sys.exit(2)
    return resolved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to ingest")
    parser.add_argument("--commit", action="store_true", help="Stage then merge into data/documents.json")
    args = parser.parse_args(argv)

    files = _iter_paths(args.paths)
    if not files:
        print("error: no files found", file=sys.stderr)
        return 1

    # Common parent for legible relative paths in the report.
    common_root = files[0].parent
    for p in files[1:]:
        while not str(p).startswith(str(common_root)):
            common_root = common_root.parent

    refs = [_file_ref(p, common_root) for p in files]

    triage_entries = triage(refs)
    primary_entries = primaries(triage_entries)
    print(
        f"Discovered {len(refs)} files; "
        f"{len(primary_entries)} primaries after triage "
        f"({len(triage_entries) - len(primary_entries)} duplicates skipped)"
    )

    tagged: list = []
    for i, entry in enumerate(primary_entries, 1):
        print(f"  [{i}/{len(primary_entries)}] tagging {entry.file.path} ...")
        try:
            output = tag_document(entry=entry, folder_codename=FIRM_CODENAME)
        except Exception as e:  # noqa: BLE001
            print(f"    ⚠ failed: {e}", file=sys.stderr)
            continue
        tagged.append((entry.file, output))

    if not tagged:
        print("error: no documents successfully tagged", file=sys.stderr)
        return 1

    next_n = _next_doc_index()
    doc_ids = {
        fref.path: f"doc_{FIRM_SLUG}_{next_n + i:03d}" for i, (fref, _) in enumerate(tagged)
    }
    print("  new doc_ids:", ", ".join(doc_ids.values()))

    staging = write_append_staging(
        deal_slug="_firm",
        deal_id=None,
        tagged=tagged,
        doc_ids=doc_ids,
    )
    print(f"  staging written to {staging.root.relative_to(Path.cwd())}")

    if args.commit:
        try:
            # Firm docs sit outside the deal taxonomy by design (a fund-level LP
            # report has no single sector). Bypass the gate so noisy deal_context
            # proposals from the tagger don't block legitimate firm-doc commits.
            commit_appended_docs_to_fixtures(staging, deal_id=None, skip_taxonomy_gate=True)
            print(f"  committed {len(tagged)} firm doc(s) to data/documents.json")
        except TaxonomyGateError as e:
            print(str(e), file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
