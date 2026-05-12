"""Staging output writer + optional --commit merge into data/*.json.

Staging mode (default) is the v1 happy path: writes documents.jsonl, deal.json,
report.md, taxonomy_proposals.yaml under data/_ingested/<deal_slug>/.

Commit mode additionally merges into data/deals.json and data/documents.json
and invokes scripts/check_consistency.py as a contract check. Refuses if any
taxonomy proposals exist (the governance gate).
"""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

from .deal_resolver import _slug
from .schemas import FileRef, ResolverDisagreement, TaggerOutput, TriageEntry
from .taxonomy import enforce_commit_gate, repo_root


def _json_default(o: Any) -> Any:
    if isinstance(o, (datetime, date)):
        return o.isoformat()
    if isinstance(o, Path):
        return str(o)
    raise TypeError(f"Not JSON serializable: {type(o).__name__}")


@dataclass
class StagingPaths:
    root: Path
    documents_jsonl: Path
    deal_json: Path
    report_md: Path
    taxonomy_proposals_yaml: Path


def staging_paths(deal_slug: str) -> StagingPaths:
    root = repo_root() / "data" / "_ingested" / deal_slug
    return StagingPaths(
        root=root,
        documents_jsonl=root / "documents.jsonl",
        deal_json=root / "deal.json",
        report_md=root / "report.md",
        taxonomy_proposals_yaml=root / "taxonomy_proposals.yaml",
    )


def _strip_aux_fields(d: dict) -> dict:
    """Remove TaggerOutput aux fields that don't belong in data/documents.json."""
    return {k: v for k, v in d.items() if k not in {"deal_context", "taxonomy_proposals", "extraction_warnings"}}


def _normalize_proposal(s: str) -> str:
    """Collapse spacing/case/separator variants so 'specialty chemicals distribution'
    and 'specialty_chemicals_distribution' map to the same dedup key."""
    s = s.strip().lower()
    s = re.sub(r"[\s_\-]+", "_", s)
    return s.strip("_")


def _aggregate_proposals(tagged: list[tuple[FileRef, TaggerOutput]]) -> list[dict]:
    """Dedupe taxonomy proposals across docs by (field, normalized_proposed_value).
    Keep the highest-confidence original spelling for each normalized stem."""
    by_key: dict[tuple[str, str], dict] = {}
    for _, t in tagged:
        for p in t.taxonomy_proposals:
            key = (p.field, _normalize_proposal(p.proposed_value))
            d = p.model_dump()
            if key not in by_key or d["confidence"] > by_key[key]["confidence"]:
                by_key[key] = d
    return list(by_key.values())


def _doc_record(
    *,
    doc_id: str,
    deal_id: str,
    output: TaggerOutput,
) -> dict:
    """Shape the document row exactly like data/documents.json expects."""
    full = output.model_dump(mode="json")
    stripped = _strip_aux_fields(full)
    return {
        "doc_id": doc_id,
        "deal_id": deal_id,
        **stripped,
        "full_text_excerpt": "...",  # not extracted in v1 — matches seed data convention
        "expert_id": None,  # Aurora has no expert_call docs; v1 doesn't extract experts.
    }


def write_staging(
    *,
    folder_codename: str,
    deal_dict: dict,
    tagged: list[tuple[FileRef, TaggerOutput]],
    doc_ids: dict[str, str],
    triage_entries: list[TriageEntry],
    disagreements: list[ResolverDisagreement],
    needs_review: list[str],
) -> StagingPaths:
    deal_slug = _slug(folder_codename)
    paths = staging_paths(deal_slug)
    paths.root.mkdir(parents=True, exist_ok=True)

    # documents.jsonl
    deal_id = deal_dict["deal_id"]
    with paths.documents_jsonl.open("w") as f:
        for fref, output in tagged:
            doc_id = doc_ids[fref.path]
            f.write(json.dumps(_doc_record(doc_id=doc_id, deal_id=deal_id, output=output), default=_json_default) + "\n")

    # deal.json
    paths.deal_json.write_text(json.dumps(deal_dict, indent=2, default=_json_default))

    # taxonomy_proposals.yaml
    proposals = _aggregate_proposals(tagged)
    paths.taxonomy_proposals_yaml.write_text(yaml.safe_dump({"proposals": proposals}, sort_keys=False))

    # report.md
    paths.report_md.write_text(_build_report(
        folder_codename=folder_codename,
        deal_dict=deal_dict,
        tagged=tagged,
        doc_ids=doc_ids,
        triage_entries=triage_entries,
        disagreements=disagreements,
        needs_review=needs_review,
        proposals=proposals,
    ))

    return paths


def _build_report(
    *,
    folder_codename: str,
    deal_dict: dict,
    tagged: list[tuple[FileRef, TaggerOutput]],
    doc_ids: dict[str, str],
    triage_entries: list[TriageEntry],
    disagreements: list[ResolverDisagreement],
    needs_review: list[str],
    proposals: list[dict],
) -> str:
    lines: list[str] = []
    lines.append(f"# Ingestion report — {folder_codename}")
    lines.append("")
    lines.append(f"Deal ID: `{deal_dict['deal_id']}`")
    lines.append(f"Company canonical: `{deal_dict['company_canonical']}`")
    lines.append(f"Sector / subsector: `{deal_dict['sector']}` / `{deal_dict['subsector']}`")
    lines.append(f"Geography: `{deal_dict['geography']}`")
    lines.append(f"Deal type: `{deal_dict['deal_type']}`")
    meta = deal_dict.get("_resolver_meta", {})
    lines.append(
        f"Voted with {meta.get('qualifying_doc_count')} qualifying docs at confidence >= "
        f"{meta.get('confidence_threshold_used')} (out of {meta.get('total_tagged_docs')} tagged)."
    )
    lines.append("")

    # Triage decisions
    lines.append("## Triage")
    lines.append("")
    by_role: dict[str, list[TriageEntry]] = {"primary": [], "format_duplicate": [], "superseded": [], "system": []}
    for e in triage_entries:
        by_role.setdefault(e.role, []).append(e)
    for role in ("primary", "format_duplicate", "superseded", "system"):
        items = by_role.get(role, [])
        if not items:
            continue
        lines.append(f"### {role} ({len(items)})")
        for e in items:
            hint = f" [hint: {e.doc_type_hint}]" if e.doc_type_hint else ""
            notes = f" — {'; '.join(e.notes)}" if e.notes else ""
            lines.append(f"- `{e.file.path}`{hint}{notes}")
        lines.append("")

    # Per-doc tag summary
    lines.append("## Tagged documents")
    lines.append("")
    for fref, output in tagged:
        doc_id = doc_ids[fref.path]
        lines.append(f"### `{fref.path}` → `{doc_id}` ({output.doc_type.value})")
        lines.append(f"- Title: {output.title}")
        lines.append(f"- Date: {output.date.isoformat() if output.date else '(none)'}")
        lines.append(f"- Summary: {output.summary}")
        if output.deal_context:
            lines.append(
                f"- deal_context (confidence={output.deal_context.confidence}): "
                f"company={output.deal_context.company_canonical}, "
                f"sector={output.deal_context.sector}, "
                f"subsector={output.deal_context.subsector}"
            )
        if output.extraction_warnings:
            lines.append("- <details><summary>⚠ extraction warnings</summary>")
            lines.append("")
            for w in output.extraction_warnings:
                lines.append(f"  - {w}")
            lines.append("")
            lines.append("  </details>")
        lines.append("")

    # Resolver vote breakdown
    if disagreements:
        lines.append("## Resolver disagreements")
        lines.append("")
        for d in disagreements:
            lines.append(f"### {d.field}")
            lines.append(f"- Chosen: `{d.chosen_value}` ({d.note})")
            lines.append(f"- Voters for chosen: {d.chosen_voters}")
            for val, paths in d.dissenting.items():
                lines.append(f"- Dissent `{val}`: {paths}")
            lines.append("")

    # Needs-review
    if needs_review:
        lines.append("## Needs review (fields the vote couldn't resolve)")
        lines.append("")
        for field in needs_review:
            lines.append(f"- {field}")
        lines.append("")

    # Taxonomy proposals
    if proposals:
        lines.append("## Taxonomy proposals")
        lines.append("")
        lines.append("These values were not in `enums.yaml`. The tagger persisted `closest_existing`")
        lines.append("but flagged the proposed addition. `--commit` will refuse until these are resolved.")
        lines.append("")
        for p in proposals:
            lines.append(
                f"- {p['field']}: proposed=`{p['proposed_value']}` "
                f"(used `{p['closest_existing']}`, confidence={p['confidence']})"
            )
            if p.get("rationale"):
                lines.append(f"  - rationale: {p['rationale']}")
        lines.append("")

    return "\n".join(lines)


# -----------------------------------------------------------------------------
# --commit
# -----------------------------------------------------------------------------


def _strip_resolver_meta(deal: dict) -> dict:
    return {k: v for k, v in deal.items() if k != "_resolver_meta"}


def commit_to_fixtures(staging: StagingPaths) -> None:
    """Append the staged deal + documents to data/deals.json and data/documents.json.
    Refuses if taxonomy_proposals.yaml is non-empty. Runs check_consistency.py after."""
    proposals_doc = yaml.safe_load(staging.taxonomy_proposals_yaml.read_text()) or {}
    proposals = proposals_doc.get("proposals") or []
    enforce_commit_gate(proposals)

    deal = json.loads(staging.deal_json.read_text())
    deal_clean = _strip_resolver_meta(deal)

    docs: list[dict] = []
    with staging.documents_jsonl.open() as f:
        for line in f:
            line = line.strip()
            if line:
                docs.append(json.loads(line))

    deals_path = repo_root() / "data" / "deals.json"
    documents_path = repo_root() / "data" / "documents.json"

    deals_blob = json.loads(deals_path.read_text())
    documents_blob = json.loads(documents_path.read_text())

    # Idempotency: refuse to double-commit the same deal_id.
    existing_ids = {d["deal_id"] for d in deals_blob["deals"]}
    if deal_clean["deal_id"] in existing_ids:
        raise RuntimeError(
            f"deal_id {deal_clean['deal_id']!r} already exists in data/deals.json. "
            "Remove it manually before re-committing."
        )

    deals_blob["deals"].append(deal_clean)
    documents_blob["documents"].extend(docs)

    deals_path.write_text(json.dumps(deals_blob, indent=2))
    documents_path.write_text(json.dumps(documents_blob, indent=2))

    # Contract check
    script = repo_root() / "scripts" / "check_consistency.py"
    result = subprocess.run(
        ["uv", "run", "python", str(script)],
        cwd=repo_root(),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"⚠ check_consistency.py failed after commit (exit {result.returncode}):")
        print(result.stdout)
        print(result.stderr)
    else:
        print(result.stdout.strip() or "consistency check passed.")
