"""Ingest a local deal folder into the demo's data fixtures.

Three modes:
  default (staging):  Runs LLM pipeline and writes to data/_ingested/<deal_slug>/.
  --commit:           Staging + appends to data/deals.json + data/documents.json.
                      Refuses if any taxonomy proposals exist (governance gate).
  --commit-only:      Skips LLM pipeline; commits already-staged files directly.
                      Use after reviewing staging output from a previous run.

Three deal kinds (via --kind):
  active     → pursuit-time snapshot. Default.
  portfolio  → held company; aggregates board packages into a portco_actuals
               time series, latest board package wins on snapshot financials.
  exited     → closed deal; entry IC memo drives financials + underwriting_case,
               returns_summary / exit IC memo drives outcome.

Folder names are parsed: a leading 'NN. ' numeric prefix is stripped, so
'01. Project Aurora' becomes codename 'Project Aurora'.

Requires ANTHROPIC_API_KEY in environment (not needed for --commit-only).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # picks up ANTHROPIC_API_KEY from .env at repo root

from services.ingestion.deal_resolver import _slug, synthesize_deal_from_tagged_docs
from services.ingestion.persistence import commit_to_fixtures, staging_paths, write_staging
from services.ingestion.sources import LocalFolderSource
from services.ingestion.tagger import tag_document
from services.ingestion.taxonomy import TaxonomyGateError
from services.ingestion.triage import primaries, triage


def _parse_codename(folder: Path) -> str:
    """Strip a leading 'NN. ' prefix if present."""
    name = folder.name
    return re.sub(r"^\d+\.\s*", "", name)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="Path to the deal folder (e.g. '01. Project Aurora')")
    parser.add_argument(
        "--kind",
        choices=("active", "portfolio", "exited"),
        default="active",
        help="Deal kind. Selects resolver strategy. Default: active.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--commit", action="store_true", help="Stage then merge into data/*.json.")
    mode.add_argument("--commit-only", action="store_true", help="Commit already-staged files without re-running LLM pipeline.")
    args = parser.parse_args(argv)

    folder: Path = args.folder.resolve()
    if not folder.is_dir():
        print(f"error: not a directory: {folder}", file=sys.stderr)
        return 2

    codename = _parse_codename(folder)

    if args.commit_only:
        deal_slug = _slug(codename)
        staging = staging_paths(deal_slug)
        if not staging.deal_json.exists():
            print(f"error: no staged files found at {staging.root} — run without --commit-only first", file=sys.stderr)
            return 1
        try:
            commit_to_fixtures(staging)
            import json
            deal_id = json.loads(staging.deal_json.read_text())["deal_id"]
            print(f"  committed deal_id={deal_id} to data/deals.json + data/documents.json")
        except TaxonomyGateError as e:
            print(str(e), file=sys.stderr)
            return 1
        return 0
    print(f"Ingesting '{codename}' from {folder}")

    # Stage 1: sources
    source = LocalFolderSource(folder)
    files = list(source.iter_files())
    print(f"  discovered {len(files)} files")

    # Stage 2: triage
    triage_entries = triage(files)
    primary_entries = primaries(triage_entries)
    print(
        f"  triage: {len(primary_entries)} primaries "
        f"({len(triage_entries) - len(primary_entries)} duplicates/superseded)"
    )

    # Stage 3+4: extract + tag (the LLM calls)
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

    # Assign doc_ids
    deal_slug = _slug(codename)
    doc_ids: dict[str, str] = {
        fref.path: f"doc_{deal_slug}_{i:03d}" for i, (fref, _) in enumerate(tagged, 1)
    }

    # Stage 5: resolve
    deal_dict, disagreements, needs_review = synthesize_deal_from_tagged_docs(
        folder_codename=codename,
        tagged=tagged,
        doc_ids=doc_ids,
        kind=args.kind,
    )
    print(
        f"  resolved deal_id={deal_dict['deal_id']} "
        f"(disagreements={len(disagreements)}, needs_review={needs_review or 'none'})"
    )

    # Stage 6: persist
    staging = write_staging(
        folder_codename=codename,
        deal_dict=deal_dict,
        tagged=tagged,
        doc_ids=doc_ids,
        triage_entries=triage_entries,
        disagreements=disagreements,
        needs_review=needs_review,
    )
    print(f"  staging written to {staging.root.relative_to(Path.cwd())}")

    if args.commit:
        try:
            commit_to_fixtures(staging)
            print(f"  committed deal_id={deal_dict['deal_id']} to data/deals.json + data/documents.json")
        except TaxonomyGateError as e:
            print(str(e), file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
