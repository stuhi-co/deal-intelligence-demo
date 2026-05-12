"""Aggregate per-doc tagger outputs into a single Deal record.

The pipeline supports three deal kinds, each with its own resolver:

  - active     → pursuit-time snapshot. Plurality vote on identity fields,
                 most-recent-CIM-wins on financials, no outcome.
  - portfolio  → held company. Plurality on identity, latest board package wins
                 on snapshot financials/thesis/risk, period_actuals aggregated
                 across all docs into a portco_actuals time series.
  - exited     → closed deal. Plurality on identity, entry IC memo (or pre-entry
                 CIM) wins on financials, underwriting_case from entry memo,
                 outcome assembled from returns_summary / exit IC memo.

Shared primitives (`_vote_categorical`, `_union_list`, `_pick_qualifying`) are
kind-agnostic. The differences live in financials picking and outcome assembly.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from datetime import date
from typing import Any, Callable, Iterable, Optional

from .schemas import (
    DealContext,
    FileRef,
    ResolverDisagreement,
    StructuredPayload,
    TaggerOutput,
)


_CATEGORICAL_FIELDS = (
    "company_canonical",
    "sector",
    "subsector",
    "geography",
    "deal_type",
)
_LIST_FIELDS = ("thesis_themes", "risk_flags")
_FINANCIAL_FIELDS = (
    "revenue_ltm_usd",
    "ebitda_ltm_usd",
    "ebitda_margin",
    "revenue_cagr_3yr",
    "ev_proposed_usd",
    "ev_ebitda_multiple",
)

# Doc types that carry financials/end-market data but not company sector identity.
# Exclude them from sector/subsector voting to reduce noise.
_FIELD_VOTE_DENYLIST: dict[str, set[str]] = {
    "sector": {"financial_model"},
    "subsector": {"financial_model"},
}

_CORP_SUFFIX_RE = re.compile(
    r"[,\s]+(inc|llc|lp|l\.p\.|l\.l\.c\.|corp|corporation|ltd)\.?$",
    re.IGNORECASE,
)
_PARENS_RE = re.compile(r"\s*\([^)]*\)\s*")


def _normalize_company(s: Any) -> str | Any:
    if not isinstance(s, str):
        return s
    s = _PARENS_RE.sub(" ", s)
    s = _CORP_SUFFIX_RE.sub("", s.strip())
    return " ".join(s.split()).strip().lower()


def _slug(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def _enum_value(v: Any) -> Any:
    """Unwrap StrEnum to its string value; pass other types through."""
    return v.value if hasattr(v, "value") else v


def _pick_qualifying(
    tagged: list[tuple[FileRef, TaggerOutput]],
    threshold: float,
) -> list[tuple[FileRef, TaggerOutput]]:
    return [
        (f, t)
        for f, t in tagged
        if t.deal_context is not None and t.deal_context.confidence >= threshold
    ]


def _vote_categorical(
    field: str,
    qualifying: list[tuple[FileRef, TaggerOutput]],
) -> tuple[Any, ResolverDisagreement | None]:
    """Per-field plurality vote with confidence-sum tiebreak.

    For company_canonical, normalizes values before voting (strips corp suffixes
    and parentheticals) so cosmetic variants collapse to one candidate. The display
    form with highest confidence is kept for output.

    Docs in _FIELD_VOTE_DENYLIST[field] are silently excluded from the vote.
    """
    denied_types = _FIELD_VOTE_DENYLIST.get(field, set())
    is_company = field == "company_canonical"

    voters_by_value: dict[Any, list[str]] = defaultdict(list)
    confidence_by_value: dict[Any, float] = defaultdict(float)
    display_by_normalized: dict[Any, str] = {}  # only used for company_canonical

    for f, t in qualifying:
        if t.doc_type.value in denied_types:
            continue
        ctx = t.deal_context
        assert ctx is not None  # guaranteed by _pick_qualifying
        raw = _enum_value(getattr(ctx, field))
        if raw is None:
            continue

        if is_company:
            key = _normalize_company(raw)
            # Keep the longest display form per normalized key as the canonical spelling.
            if key not in display_by_normalized or len(raw) > len(display_by_normalized[key]):
                display_by_normalized[key] = raw
        else:
            key = raw

        voters_by_value[key].append(f.path)
        confidence_by_value[key] += ctx.confidence

    if not voters_by_value:
        return None, None

    counts = Counter({v: len(paths) for v, paths in voters_by_value.items()})
    top_count = counts.most_common(1)[0][1]
    top_values = [v for v, c in counts.items() if c == top_count]

    if len(top_values) == 1:
        chosen_key = top_values[0]
        tiebreak_note = ""
    else:
        chosen_key = max(top_values, key=lambda v: confidence_by_value[v])
        tiebreak_note = f"; tied {top_count}-way, broke tie by confidence sum"

    # Resolve display form for company_canonical; other fields use key as-is.
    chosen = display_by_normalized.get(chosen_key, chosen_key) if is_company else chosen_key

    chosen_voters = voters_by_value[chosen_key]
    dissenting_keys = {v: paths for v, paths in voters_by_value.items() if v != chosen_key}
    # Convert dissenting keys back to display forms for readability.
    dissenting = {
        (display_by_normalized.get(v, v) if is_company else v): paths
        for v, paths in dissenting_keys.items()
    }

    if not dissenting:
        return chosen, None

    return chosen, ResolverDisagreement(
        field=field,
        chosen_value=chosen,
        chosen_voters=chosen_voters,
        dissenting=dissenting,
        note=f"plurality {top_count}/{sum(counts.values())}{tiebreak_note}",
    )


def _union_list(
    field: str,
    qualifying: list[tuple[FileRef, TaggerOutput]],
) -> list[str]:
    seen: list[str] = []
    for _, t in qualifying:
        ctx = t.deal_context
        assert ctx is not None
        for item in getattr(ctx, field):
            v = _enum_value(item)
            if v not in seen:
                seen.append(v)
    return seen


def _pick_stage_entered_at(
    tagged: list[tuple[FileRef, TaggerOutput]],
    *,
    rank: dict[str, int] | None = None,
    prefer_earliest: bool = False,
) -> date:
    """Choose a representative date.

    Default (`prefer_earliest=False`) returns the earliest date among the
    highest-ranked doc types — anchors deal_id year to the deal's decision docs.
    With `prefer_earliest=True`, scans all docs and returns the earliest date
    overall (used for portfolio: original entry date, not most recent board pkg).
    """
    rank = rank or {"ic_memo": 0, "cim": 1}
    if prefer_earliest:
        # Earliest date across all docs, with type rank as a soft tiebreak.
        candidates = [
            (rank.get(t.doc_type.value, 2), t.date.toordinal(), t.date)
            for _, t in tagged
            if t.date
        ]
        if not candidates:
            return date.today()
        candidates.sort()
        return candidates[0][2]

    # Original behavior: rank first, then most recent within rank.
    candidates = [
        (rank.get(t.doc_type.value, 2), -(t.date.toordinal()), t.date)
        for _, t in tagged
        if t.date
    ]
    if not candidates:
        return date.today()
    candidates.sort()
    return candidates[0][2]


def _pick_financials(
    tagged: list[tuple[FileRef, TaggerOutput]],
    *,
    preference: tuple[str, ...] = ("cim", "ic_memo"),
    doc_filter: Callable[[FileRef, TaggerOutput], bool] | None = None,
) -> tuple[dict[str, float | None], list[ResolverDisagreement]]:
    """Per-field financial pick.

    Sort docs by (type_rank from `preference`, most-recent date desc) and take the
    first non-null value per financial field. `doc_filter` further restricts the
    candidate set before sorting — e.g., exited resolver filters out post-entry
    sell-side CIM by date so the entry-era snapshot wins cleanly.

    Sanity check: if another doc reports a value differing by >20%, log a
    disagreement (don't override).
    """
    if doc_filter is not None:
        candidates = [(f, t) for f, t in tagged if doc_filter(f, t)]
    else:
        candidates = list(tagged)

    rank = {dt: i for i, dt in enumerate(preference)}
    default_rank = len(preference)

    def _order_key(item: tuple[FileRef, TaggerOutput]) -> tuple[int, int]:
        _, t = item
        type_rank = rank.get(t.doc_type.value, default_rank)
        date_key = -(t.date.toordinal() if t.date else 0)
        return (type_rank, date_key)

    sorted_tagged = sorted(candidates, key=_order_key)

    financials: dict[str, float | None] = {field: None for field in _FINANCIAL_FIELDS}
    chosen_source: dict[str, str] = {}
    disagreements: list[ResolverDisagreement] = []

    for field in _FINANCIAL_FIELDS:
        chosen_value = None
        chosen_path = None
        other_values: dict[float, list[str]] = defaultdict(list)

        for f, t in sorted_tagged:
            v = getattr(t.structured, field)
            if v is None:
                continue
            if chosen_value is None:
                chosen_value = v
                chosen_path = f.path
            elif chosen_value != 0 and abs(v - chosen_value) / abs(chosen_value) > 0.20:
                other_values[v].append(f.path)

        financials[field] = chosen_value
        if chosen_path:
            chosen_source[field] = chosen_path
        if other_values and chosen_value is not None:
            disagreements.append(
                ResolverDisagreement(
                    field=f"financials.{field}",
                    chosen_value=chosen_value,
                    chosen_voters=[chosen_source[field]],
                    dissenting={str(v): paths for v, paths in other_values.items()},
                    note="other docs reported values differing by >20%; chosen value not overridden",
                )
            )

    return financials, disagreements


# -----------------------------------------------------------------------------
# Portfolio + exited specific helpers
# -----------------------------------------------------------------------------


def _latest_doc_of_type(
    tagged: list[tuple[FileRef, TaggerOutput]],
    doc_types: tuple[str, ...],
) -> tuple[FileRef, TaggerOutput] | None:
    """Return the most recent (by date) doc whose doc_type is in the set, or None."""
    candidates = [
        (f, t) for f, t in tagged if t.doc_type.value in doc_types and t.date
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[1].date, reverse=True)  # type: ignore[arg-type, return-value]
    return candidates[0]


_PERIOD_FIELDS = ("revenue_usd", "ebitda_usd", "ebitda_margin")


def _aggregate_period_actuals(
    tagged: list[tuple[FileRef, TaggerOutput]],
) -> list[dict[str, Any]]:
    """Merge PeriodActual rows across all docs by (year, quarter), per-field.
    Latest doc (by tag date) wins per field — so a period reported by an early
    board pkg with only ebitda still gets revenue filled in from a later
    financial supplement. Annual rows (quarter=None) and quarterly rows for
    the same year coexist as separate rows. Returns sorted ascending."""
    # (year, quarter) → field → (date, value).
    per_field: dict[tuple[int, Optional[int]], dict[str, tuple[date, Any]]] = defaultdict(dict)
    for _, t in tagged:
        if not t.period_actuals or t.date is None:
            # Skip docs with no date — can't reason about recency.
            continue
        for pa in t.period_actuals:
            key = (pa.year, pa.quarter)
            for field in _PERIOD_FIELDS:
                v = getattr(pa, field)
                if v is None:
                    continue
                existing = per_field[key].get(field)
                if existing is None or t.date > existing[0]:
                    per_field[key][field] = (t.date, v)

    rows = []
    # Sort annual (quarter=None → 0) before quarterly rows of the same year.
    for key in sorted(per_field.keys(), key=lambda k: (k[0], k[1] or 0)):
        year, quarter = key
        row: dict[str, Any] = {"year": year}
        if quarter is not None:
            row["quarter"] = quarter
        for field in _PERIOD_FIELDS:
            entry = per_field[key].get(field)
            row[field] = entry[1] if entry else None
        rows.append(row)
    return rows


# -----------------------------------------------------------------------------
# Shared deal-record assembly
# -----------------------------------------------------------------------------


def _build_common_deal_fields(
    *,
    folder_codename: str,
    qualifying: list[tuple[FileRef, TaggerOutput]],
    tagged: list[tuple[FileRef, TaggerOutput]],
    doc_ids: dict[str, str],
    stage_entered_at: date,
) -> tuple[dict[str, Any], dict[str, Any], list[ResolverDisagreement], list[str]]:
    """Compute the kind-agnostic deal-record fields shared by all three resolvers.

    Returns: (deal_partial, voted_dict, disagreements, needs_review_fields).
    """
    disagreements: list[ResolverDisagreement] = []
    needs_review: list[str] = []

    voted: dict[str, Any] = {}
    for field in _CATEGORICAL_FIELDS:
        chosen, dis = _vote_categorical(field, qualifying)
        voted[field] = chosen
        if dis:
            disagreements.append(dis)
        if chosen is None:
            needs_review.append(field)

    codename = folder_codename
    company_canonical = voted.get("company_canonical")
    detected_codenames = [
        t.deal_context.codename_detected
        for _, t in qualifying
        if t.deal_context and t.deal_context.codename_detected and t.deal_context.codename_detected != codename
    ]
    aliases_seq: list[str] = []
    for a in [codename, company_canonical, *detected_codenames]:
        if a and a not in aliases_seq:
            aliases_seq.append(a)

    deal_slug = _slug(codename)
    deal_id = f"deal_{deal_slug}_{stage_entered_at.year}"
    source_documents = [doc_ids[f.path] for f, _ in tagged if f.path in doc_ids]

    deal_partial = {
        "deal_id": deal_id,
        "codename": codename,
        "aliases": aliases_seq,
        "company_canonical": company_canonical,
        "stage_entered_at": stage_entered_at.isoformat(),
        "lead_partner": None,
        "deal_team": [],
        "sector": voted.get("sector"),
        "subsector": voted.get("subsector"),
        "geography": voted.get("geography"),
        "deal_type": voted.get("deal_type"),
        "source_documents": source_documents,
        "salesforce_opportunity_id": None,
        "similar_deals_computed": [],
    }
    return deal_partial, voted, disagreements, needs_review


# -----------------------------------------------------------------------------
# Per-kind resolvers
# -----------------------------------------------------------------------------


def _synthesize_active(
    *,
    folder_codename: str,
    tagged: list[tuple[FileRef, TaggerOutput]],
    doc_ids: dict[str, str],
    qualifying: list[tuple[FileRef, TaggerOutput]],
    threshold_used: float,
) -> tuple[dict[str, Any], list[ResolverDisagreement], list[str]]:
    stage_entered_at = _pick_stage_entered_at(tagged)
    deal_partial, _, disagreements, needs_review = _build_common_deal_fields(
        folder_codename=folder_codename,
        qualifying=qualifying,
        tagged=tagged,
        doc_ids=doc_ids,
        stage_entered_at=stage_entered_at,
    )
    thesis_themes = _union_list("thesis_themes", qualifying)
    risk_flags = _union_list("risk_flags", qualifying)
    financials, fin_disagreements = _pick_financials(tagged)
    disagreements.extend(fin_disagreements)

    deal_dict = {
        **deal_partial,
        "status": "active_diligence",
        "financials": financials,
        "thesis_themes": thesis_themes,
        "risk_flags": risk_flags,
        "outcome": None,
        "_resolver_meta": {
            "kind": "active",
            "qualifying_doc_count": len(qualifying),
            "confidence_threshold_used": threshold_used,
            "total_tagged_docs": len(tagged),
        },
    }
    # Preserve historical field order for clean diffs against existing fixtures.
    return _reorder_active(deal_dict), disagreements, needs_review


def _reorder_active(d: dict[str, Any]) -> dict[str, Any]:
    """Match the historical key order used by previously-committed active deals."""
    order = [
        "deal_id", "codename", "aliases", "company_canonical", "status",
        "stage_entered_at", "lead_partner", "deal_team", "sector", "subsector",
        "geography", "deal_type", "financials", "thesis_themes", "risk_flags",
        "source_documents", "salesforce_opportunity_id", "similar_deals_computed",
        "outcome", "_resolver_meta",
    ]
    return {k: d[k] for k in order if k in d}


def _synthesize_portfolio(
    *,
    folder_codename: str,
    tagged: list[tuple[FileRef, TaggerOutput]],
    doc_ids: dict[str, str],
    qualifying: list[tuple[FileRef, TaggerOutput]],
    threshold_used: float,
) -> tuple[dict[str, Any], list[ResolverDisagreement], list[str]]:
    # stage_entered_at: original entry date, NOT latest board package.
    stage_entered_at = _pick_stage_entered_at(
        tagged,
        rank={"ic_memo": 0, "board_package": 1, "quarterly_financials": 2},
        prefer_earliest=True,
    )
    deal_partial, _, disagreements, needs_review = _build_common_deal_fields(
        folder_codename=folder_codename,
        qualifying=qualifying,
        tagged=tagged,
        doc_ids=doc_ids,
        stage_entered_at=stage_entered_at,
    )

    # Snapshot financials: per-field, most-recent reporting doc wins.
    # Board packages and quarterly_financials are the primary sources; older
    # docs fill in fields the latest pkg didn't report (e.g., revenue when a
    # board deck only shows EBITDA).
    financials, fin_disagreements = _pick_financials(
        tagged,
        preference=("board_package", "quarterly_financials"),
    )
    disagreements.extend(fin_disagreements)

    # Thesis / risk from latest board package only (drift over hold period).
    latest_board = _latest_doc_of_type(tagged, ("board_package", "quarterly_financials"))
    if latest_board is not None:
        _, board_t = latest_board
        if board_t.deal_context is not None:
            thesis_themes = [_enum_value(v) for v in board_t.deal_context.thesis_themes]
            risk_flags = [_enum_value(v) for v in board_t.deal_context.risk_flags]
        else:
            thesis_themes = _union_list("thesis_themes", qualifying)
            risk_flags = _union_list("risk_flags", qualifying)
    else:
        thesis_themes = _union_list("thesis_themes", qualifying)
        risk_flags = _union_list("risk_flags", qualifying)

    portco_actuals = _aggregate_period_actuals(tagged)

    deal_dict = {
        **deal_partial,
        "status": "closed_held",
        "financials": financials,
        "thesis_themes": thesis_themes,
        "risk_flags": risk_flags,
        "outcome": None,
        "portco_actuals": portco_actuals,
        "_resolver_meta": {
            "kind": "portfolio",
            "qualifying_doc_count": len(qualifying),
            "confidence_threshold_used": threshold_used,
            "total_tagged_docs": len(tagged),
        },
    }
    return deal_dict, disagreements, needs_review


def _synthesize_exited(
    *,
    folder_codename: str,
    tagged: list[tuple[FileRef, TaggerOutput]],
    doc_ids: dict[str, str],
    qualifying: list[tuple[FileRef, TaggerOutput]],
    threshold_used: float,
) -> tuple[dict[str, Any], list[ResolverDisagreement], list[str]]:
    # Anchor on the entry IC memo for stage_entered_at.
    entry_memo = _pick_entry_memo(tagged)
    if entry_memo is not None and entry_memo[1].date:
        stage_entered_at = entry_memo[1].date
    else:
        stage_entered_at = _pick_stage_entered_at(tagged)

    deal_partial, _, disagreements, needs_review = _build_common_deal_fields(
        folder_codename=folder_codename,
        qualifying=qualifying,
        tagged=tagged,
        doc_ids=doc_ids,
        stage_entered_at=stage_entered_at,
    )

    # Financials = entry-era snapshot. Exclude the post-entry sell-side CIM
    # via date filter so it doesn't shadow the entry IC memo.
    entry_cutoff = stage_entered_at

    def _entry_era_filter(_f: FileRef, t: TaggerOutput) -> bool:
        if t.doc_type.value == "ic_memo":
            return t.memo_purpose == "entry" or t.memo_purpose is None
        # Allow CIM / financial_model only if they pre-date (or match) entry.
        if t.date is None:
            return False
        return t.date <= entry_cutoff

    financials, fin_disagreements = _pick_financials(
        tagged,
        preference=("ic_memo", "cim", "financial_model"),
        doc_filter=_entry_era_filter,
    )
    disagreements.extend(fin_disagreements)

    # Identity-list fields: union from all qualifying docs (entry context dominates
    # because there's typically one entry memo + one exit memo; both reflect the
    # same company's thesis/risks).
    thesis_themes = _union_list("thesis_themes", qualifying)
    risk_flags = _union_list("risk_flags", qualifying)

    # Underwriting case: first non-empty extract from an entry IC memo.
    underwriting_case = None
    if entry_memo is not None:
        _, em_t = entry_memo
        if em_t.underwriting_case_extract:
            underwriting_case = {
                year_label: yr.model_dump(mode="json", exclude_none=True)
                for year_label, yr in em_t.underwriting_case_extract.items()
            }

    # Outcome: prefer returns_summary xlsx; fall back to exit IC memo.
    outcome = _assemble_exit_outcome(tagged)

    deal_dict = {
        **deal_partial,
        "status": "closed_exited",
        "financials": financials,
        "thesis_themes": thesis_themes,
        "risk_flags": risk_flags,
        "outcome": outcome,
        "underwriting_case": underwriting_case,
        "_resolver_meta": {
            "kind": "exited",
            "qualifying_doc_count": len(qualifying),
            "confidence_threshold_used": threshold_used,
            "total_tagged_docs": len(tagged),
        },
    }
    return deal_dict, disagreements, needs_review


def _pick_entry_memo(
    tagged: list[tuple[FileRef, TaggerOutput]],
) -> tuple[FileRef, TaggerOutput] | None:
    """Find the entry IC memo. Prefer explicit memo_purpose='entry'; otherwise
    fall back to the earliest ic_memo by date."""
    explicit = [
        (f, t) for f, t in tagged
        if t.doc_type.value == "ic_memo" and t.memo_purpose == "entry"
    ]
    if explicit:
        explicit.sort(key=lambda x: x[1].date or date.min)
        return explicit[0]
    all_memos = [
        (f, t) for f, t in tagged
        if t.doc_type.value == "ic_memo" and t.date
    ]
    if not all_memos:
        return None
    all_memos.sort(key=lambda x: x[1].date)  # type: ignore[arg-type, return-value]
    return all_memos[0]


def _pick_exit_memo(
    tagged: list[tuple[FileRef, TaggerOutput]],
) -> tuple[FileRef, TaggerOutput] | None:
    """Find the exit IC memo. Prefer explicit memo_purpose='exit'; fall back to
    the latest ic_memo (assumes an exited folder has both entry + exit memos)."""
    explicit = [
        (f, t) for f, t in tagged
        if t.doc_type.value == "ic_memo" and t.memo_purpose == "exit"
    ]
    if explicit:
        explicit.sort(key=lambda x: x[1].date or date.min, reverse=True)
        return explicit[0]
    all_memos = [
        (f, t) for f, t in tagged
        if t.doc_type.value == "ic_memo" and t.date
    ]
    if len(all_memos) < 2:
        return None  # only entry memo present
    all_memos.sort(key=lambda x: x[1].date, reverse=True)  # type: ignore[arg-type, return-value]
    return all_memos[0]


def _assemble_exit_outcome(
    tagged: list[tuple[FileRef, TaggerOutput]],
) -> dict[str, Any] | None:
    """Build the `outcome` block. Returns None if no returns signal anywhere."""
    # Prefer authoritative returns_summary xlsx; fall back to funds_flow, then exit IC memo.
    returns_src: TaggerOutput | None = None
    for preferred_type in ("returns_summary", "funds_flow"):
        for _, t in tagged:
            if t.doc_type.value == preferred_type and t.returns_extract is not None:
                returns_src = t
                break
        if returns_src is not None:
            break

    exit_memo = _pick_exit_memo(tagged)
    if returns_src is None and exit_memo is not None and exit_memo[1].returns_extract is not None:
        returns_src = exit_memo[1]

    if returns_src is None and exit_memo is None:
        return None

    outcome: dict[str, Any] = {
        "decision": "closed",
        "decision_date": exit_memo[1].date.isoformat() if exit_memo and exit_memo[1].date else None,
        "primary_reason": None,
        "secondary_reasons": [],
    }

    if returns_src and returns_src.returns_extract:
        r = returns_src.returns_extract
        outcome.update(
            {
                "irr": r.irr,
                "moic": r.moic,
                "holding_period_years": r.holding_period_years,
                "exit_year": r.exit_year,
                "exit_ev_usd": r.exit_ev_usd,
                "exit_type": _enum_value(r.exit_type) if r.exit_type else None,
            }
        )

    if exit_memo is not None:
        outcome["post_decision_tracking"] = exit_memo[1].summary or None
    else:
        outcome["post_decision_tracking"] = None

    return outcome


# -----------------------------------------------------------------------------
# Public dispatcher
# -----------------------------------------------------------------------------


def synthesize_deal_from_tagged_docs(
    *,
    folder_codename: str,
    tagged: list[tuple[FileRef, TaggerOutput]],
    doc_ids: dict[str, str],  # FileRef.path → assigned doc_id
    kind: str = "active",
    primary_confidence_threshold: float = 0.9,
    fallback_confidence_threshold: float = 0.7,
) -> tuple[dict[str, Any], list[ResolverDisagreement], list[str]]:
    """Build the Deal record. Returns (deal_dict, disagreements, needs_review_fields).

    `kind` selects the resolver strategy:
      - "active"    → pursuit-time snapshot (status=active_diligence, outcome=None)
      - "portfolio" → held company (status=closed_held, portco_actuals time series)
      - "exited"    → closed deal (status=closed_exited, outcome + underwriting_case)

    deal_dict is shaped to match data/deals.json — the persistence layer writes it directly.
    """
    qualifying = _pick_qualifying(tagged, primary_confidence_threshold)
    threshold_used = primary_confidence_threshold

    if len(qualifying) < 2:
        qualifying = _pick_qualifying(tagged, fallback_confidence_threshold)
        threshold_used = fallback_confidence_threshold

    common_kwargs = dict(
        folder_codename=folder_codename,
        tagged=tagged,
        doc_ids=doc_ids,
        qualifying=qualifying,
        threshold_used=threshold_used,
    )
    if kind == "active":
        return _synthesize_active(**common_kwargs)
    if kind == "portfolio":
        return _synthesize_portfolio(**common_kwargs)
    if kind == "exited":
        return _synthesize_exited(**common_kwargs)
    raise ValueError(f"Unknown deal kind: {kind!r}. Expected active|portfolio|exited.")


# Production-only stub. Documented here so the swap surface is visible.
#
# def resolve_via_salesforce(company_name: str) -> dict | None:
#     """Fuzzy-match against sf_accounts.Name. Return SF-driven deal record (deal_id from
#     SF Opportunity ID, status from Opportunity stage, etc.). Populates entity_aliases
#     with the codename → SF Account link as a side effect."""
#     ...
