"""Deterministic pre-pass triage. No LLM.

Groups format duplicates (PDF + DOCX pairs), drops superseded versions, dedupes
identical sha1s, and assigns a folder-derived doc_type_hint. Non-primaries are
labelled, not deleted — the staging report lists them so a user can promote one
to primary if the heuristic guessed wrong.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import PurePosixPath
from typing import Iterable

from .schemas import FileRef, TriageEntry


# Order matters: PDF preferred over DOCX/PPTX when the same basename appears in multiple formats.
_FORMAT_PRIORITY = {".pdf": 0, ".docx": 1, ".pptx": 1, ".xlsx": 0}

# Folder substring → doc_type_hint. First match wins (longest patterns first so
# more specific paths beat generic parents). Hints are advisory — the LLM has
# final say on doc_type (per tagger rule 8).
_FOLDER_DOCTYPE_RULES: list[tuple[str, str]] = [
    # Exit process tree — these are sell-side artifacts and must beat any
    # generic substring matches (e.g., "/cim" alone).
    ("exit process materials/marketing/cim", "cim"),
    ("exit process materials/marketing/teaser", "teaser"),
    ("exit process materials/marketing/process letter", "process_letter"),
    ("exit process materials/bids/ioi tracker", "ioi_tracker"),
    ("exit process materials/bids/final bid comparison", "final_bid_comparison"),
    ("exit process materials/bids", "management_presentation"),
    ("exit process materials/diligence/qofe", "qofe"),
    ("exit process materials/diligence/sell-side qofe", "qofe"),
    ("exit process materials/diligence/vdd", "vdd_model"),
    ("exit process materials/closing execution/funds flow", "funds_flow"),
    # Remaining closing execution artifacts (HSR, closing checklist, etc.) and
    # post-exit compliance (escrow, GP-LP, indemnity) → closest existing is dd_report.
    # Data room index under diligence also falls here.
    ("exit process materials/closing execution", "dd_report"),
    ("exit process materials/post exit compliance", "dd_report"),
    ("exit process materials/diligence/data room", "dd_report"),
    # Active diligence (existing)
    ("banker materials/cim", "cim"),
    ("banker materials/teaser", "teaser"),
    ("presentations/investment-decks", "ic_memo"),
    ("presentations/data-room-cuts", "ic_memo"),
    ("financial model", "financial_model"),
    ("data room/financials", "financial_model"),
    ("data room/legal", "dd_report"),
    ("data room/customers", "dd_report"),
    ("data room/operations", "dd_report"),
    ("data room/org-structure", "dd_report"),
    ("advisors", "dd_report"),
    ("legal", "dd_report"),
    # Portfolio reporting — coarse: any file under these folders.
    ("board materials", "board_package"),
    ("financial reporting", "quarterly_financials"),
    # Note: "Historical Performance" / "Deal Performance" folders (exit deals)
    # intentionally have no hint — they mix entry IC memos, exit IC memos, and
    # returns summaries. The LLM disambiguates from filenames like
    # IC_Memo_Entry_* / IC_Memo_Exit_* / Final_Returns_Summary_*.
]

# Filename version markers we strip when grouping versions.
_VERSION_RE = re.compile(
    r"""
    (?:_v\d+(?:\.\d+)?         # _v1, _v1.2
     |_final(?:_v\d+)?          # _final, _final_v3
     |_FINAL(?:_v\d+)?          # _FINAL, _FINAL_v3
     |[-_](?P<date>\d{4}-\d{2}(?:-\d{2})?)  # _2026-01 or _2026-01-15
    )$
    """,
    re.VERBOSE,
)


def _doc_type_hint(rel_path: str) -> str | None:
    p = rel_path.lower()
    for needle, hint in _FOLDER_DOCTYPE_RULES:
        if needle in p:
            return hint
    return None


def _version_stem(stem: str) -> tuple[str, str]:
    """Return (base_stem, version_token). version_token is '' if no version found."""
    m = _VERSION_RE.search(stem)
    if not m:
        return stem, ""
    return stem[: m.start()], m.group(0)


def _format_priority(suffix: str) -> int:
    return _FORMAT_PRIORITY.get(suffix.lower(), 99)


def triage(files: Iterable[FileRef]) -> list[TriageEntry]:
    """Apply the deterministic heuristics in order.

    Returns one TriageEntry per FileRef. Files in the same cluster_id are
    treated as the same logical doc (different formats or versions). One
    primary per cluster; others are format_duplicate or superseded.
    """
    files = list(files)

    # 1. sha1 dedup: identical bytes → same cluster (regardless of name/path).
    sha_groups: dict[str, list[FileRef]] = defaultdict(list)
    for f in files:
        sha_groups[f.sha1].append(f)

    sha_canonical: dict[str, FileRef] = {}
    sha_role: dict[str, str] = {}  # abs_path → role
    for sha, members in sha_groups.items():
        canonical = sorted(members, key=lambda f: (_format_priority(PurePosixPath(f.path).suffix), f.path))[0]
        sha_canonical[sha] = canonical
        for m in members:
            sha_role[str(m.abs_path)] = "primary" if m is canonical else "format_duplicate"

    # 2. Group by (parent_dir, base_stem_without_version) → version cluster.
    #    Within the cluster, pick the latest version as primary; others "superseded".
    #    Within a version-stem, pick the best format as primary; others "format_duplicate".
    version_groups: dict[tuple[str, str], list[tuple[FileRef, str]]] = defaultdict(list)
    for f in files:
        # Only consider files that survived sha1 dedup as canonical.
        if sha_canonical[f.sha1] is not f:
            continue
        rel = PurePosixPath(f.path)
        base_stem, version_token = _version_stem(rel.stem)
        key = (str(rel.parent), base_stem)
        version_groups[key].append((f, version_token))

    role_overrides: dict[str, str] = {}
    cluster_ids: dict[str, str] = {}

    for (parent, base_stem), members in version_groups.items():
        # Sort versions: empty token is treated as no-version (rank 0); else by token desc lexicographically
        # (works for dates and _vN since both sort sensibly).
        def _rank(item: tuple[FileRef, str]) -> tuple[int, str]:
            _, token = item
            return (1 if token else 0, token)

        ordered = sorted(members, key=_rank, reverse=True)
        latest_token = ordered[0][1]

        # Latest token group: primary candidates. Older tokens: superseded.
        for f, token in ordered:
            cid = f"c::{parent}::{base_stem}"
            cluster_ids[str(f.abs_path)] = cid
            if token != latest_token:
                role_overrides[str(f.abs_path)] = "superseded"

        # Within the latest-token group, pick best format as primary.
        latest_members = [f for f, t in ordered if t == latest_token]
        latest_members.sort(key=lambda f: (_format_priority(PurePosixPath(f.path).suffix), f.path))
        primary = latest_members[0]
        for f in latest_members:
            if f is not primary:
                role_overrides[str(f.abs_path)] = "format_duplicate"

    # 3. Build TriageEntry list, preserving input order.
    entries: list[TriageEntry] = []
    for f in files:
        key = str(f.abs_path)
        if sha_role.get(key) == "format_duplicate":
            role = "format_duplicate"
            cid = f"sha::{f.sha1[:8]}"
            notes = ["sha1 duplicate"]
        else:
            role = role_overrides.get(key, "primary")
            cid = cluster_ids.get(key, f"single::{f.path}")
            notes = []
            if role == "superseded":
                notes.append("older version superseded by newer in same folder")
            elif role == "format_duplicate":
                notes.append("PDF preferred over DOCX/PPTX twin")
        entries.append(
            TriageEntry(
                file=f,
                role=role,
                cluster_id=cid,
                doc_type_hint=_doc_type_hint(f.path),
                notes=notes,
            )
        )
    return entries


def primaries(entries: list[TriageEntry]) -> list[TriageEntry]:
    return [e for e in entries if e.role == "primary"]
