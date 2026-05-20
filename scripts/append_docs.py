"""Append net-new documents to an already-ingested deal.

Unlike ingest_folder.py — which builds a full deal record from a folder via the
resolver — this script takes a deal slug and individual file paths, tags each
file via the LLM, and appends the resulting doc records to data/documents.json
while extending the existing deal's source_documents list.

Use when a doc arrives after a deal is already committed (e.g., a Q4 board
package, an LBO model added later). ingest_folder.py refuses to re-commit an
existing deal_id, so this path keeps the deal record untouched.

Default mode stages only to data/_ingested/<slug>/_appends/<timestamp>/.
--commit additionally appends to data/deals.json + data/documents.json and runs
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


DEAL_ID_RE = re.compile(r"^deal_(?P<slug>.+)_(?P<year>\d{4})$")
DOC_ID_RE = re.compile(r"^doc_(?P<slug>.+)_(?P<n>\d+)$")


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


def _resolve_deal(deal_slug_or_id: str) -> tuple[dict, str]:
    """Find the deal in data/deals.json by slug, deal_id, or codename. Return (deal, doc_slug)
    where doc_slug is the stem used in doc_id patterns (e.g. 'pinecrest_foods')."""
    deals_path = Path(__file__).resolve().parent.parent / "data" / "deals.json"
    deals = json.loads(deals_path.read_text())["deals"]

    matches = []
    for d in deals:
        if d["deal_id"] == deal_slug_or_id:
            matches.append(d)
        elif d.get("codename") == deal_slug_or_id:
            matches.append(d)
        else:
            m = DEAL_ID_RE.match(d["deal_id"])
            if m and m.group("slug") == deal_slug_or_id:
                matches.append(d)
    if not matches:
        raise SystemExit(f"error: no deal matching {deal_slug_or_id!r} in data/deals.json")
    if len(matches) > 1:
        ids = [d["deal_id"] for d in matches]
        raise SystemExit(f"error: ambiguous slug {deal_slug_or_id!r} matches {ids}")

    deal = matches[0]
    m = DEAL_ID_RE.match(deal["deal_id"])
    doc_slug = m.group("slug") if m else deal["codename"]
    return deal, doc_slug


def _next_doc_index(doc_slug: str) -> int:
    """Find max NNN across docs with id matching doc_<doc_slug>_NNN. Returns next int."""
    docs_path = Path(__file__).resolve().parent.parent / "data" / "documents.json"
    docs = json.loads(docs_path.read_text())["documents"]
    max_n = 0
    for d in docs:
        m = DOC_ID_RE.match(d["doc_id"])
        if m and m.group("slug") == doc_slug:
            n = int(m.group("n"))
            if n > max_n:
                max_n = n
    return max_n + 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deal", help="Deal slug, codename, or full deal_id (e.g. 'pinecrest_foods')")
    parser.add_argument("files", nargs="+", type=Path, help="One or more file paths to append")
    parser.add_argument("--commit", action="store_true", help="Stage then merge into data/*.json")
    args = parser.parse_args(argv)

    deal, doc_slug = _resolve_deal(args.deal)
    deal_id = deal["deal_id"]
    codename = deal.get("company_canonical") or deal.get("codename") or doc_slug
    print(f"Appending to deal_id={deal_id} (codename for tagger: {codename!r})")

    paths = [p.resolve() for p in args.files]
    for p in paths:
        if not p.is_file():
            print(f"error: not a file: {p}", file=sys.stderr)
            return 2

    # Use the common-parent as the source root so relative paths in the report stay legible.
    try:
        common_root = Path(*Path(paths[0]).parts[:-1])
        for p in paths[1:]:
            while not str(p).startswith(str(common_root)):
                common_root = common_root.parent
    except Exception:
        common_root = paths[0].parent

    refs = [_file_ref(p, common_root) for p in paths]

    # Triage gives us doc_type_hints + drops sha1/format duplicates if the user passed dupes.
    triage_entries = triage(refs)
    primary_entries = primaries(triage_entries)
    print(
        f"  triage: {len(primary_entries)} primaries "
        f"({len(triage_entries) - len(primary_entries)} duplicates skipped)"
    )

    tagged: list = []
    for i, entry in enumerate(primary_entries, 1):
        print(f"  [{i}/{len(primary_entries)}] tagging {entry.file.path} ...")
        try:
            output = tag_document(entry=entry, folder_codename=codename)
        except Exception as e:  # noqa: BLE001
            print(f"    ⚠ failed: {e}", file=sys.stderr)
            continue
        tagged.append((entry.file, output))

    if not tagged:
        print("error: no documents successfully tagged", file=sys.stderr)
        return 1

    # Assign continuing doc_ids
    next_n = _next_doc_index(doc_slug)
    doc_ids = {
        fref.path: f"doc_{doc_slug}_{next_n + i:03d}" for i, (fref, _) in enumerate(tagged)
    }
    print("  new doc_ids:", ", ".join(doc_ids.values()))

    staging = write_append_staging(
        deal_slug=doc_slug,
        deal_id=deal_id,
        tagged=tagged,
        doc_ids=doc_ids,
    )
    print(f"  staging written to {staging.root.relative_to(Path.cwd())}")

    if args.commit:
        try:
            commit_appended_docs_to_fixtures(staging, deal_id=deal_id)
            print(f"  committed {len(tagged)} doc(s) to data/documents.json (deal_id={deal_id})")
        except TaxonomyGateError as e:
            print(str(e), file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
