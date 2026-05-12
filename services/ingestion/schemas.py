"""Pydantic models for the ingestion pipeline.

Two layers:
  - Intermediate records (FileRef, TriageEntry) flow between stages.
  - LLM output schemas (TaggerOutput and friends) enforce structured-output validity
    at the Anthropic tool-use boundary.

Enums are reused from demo_deal_mcp.models so the demo and ingestion share one source of truth.
"""

from __future__ import annotations

import json
import re
from datetime import date as _date, datetime
from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from demo_deal_mcp.models import (
    DealType,
    DocType,
    ExitType,
    Geography,
    RiskTheme,
    Sector,
    ThesisTheme,
)


_THESIS_VALUES = {t.value for t in ThesisTheme}
_RISK_VALUES = {t.value for t in RiskTheme}
_YYYY_MM_RE = re.compile(r"^\d{4}-\d{2}$")


# -----------------------------------------------------------------------------
# Source (Stage 1)
# -----------------------------------------------------------------------------


class FileRef(BaseModel):
    """A file discovered by a Source. Path is relative to the source root."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    path: str
    abs_path: Path
    size_bytes: int
    mtime: datetime
    sha1: str


# -----------------------------------------------------------------------------
# Triage (Stage 2)
# -----------------------------------------------------------------------------


TriageRole = Literal["primary", "format_duplicate", "superseded", "system"]


class TriageEntry(BaseModel):
    file: FileRef
    role: TriageRole
    cluster_id: str
    doc_type_hint: Optional[str] = None
    notes: list[str] = Field(default_factory=list)


# -----------------------------------------------------------------------------
# Tagger output (Stage 4) — the LLM tool-use schema
# -----------------------------------------------------------------------------


class KeyQuote(BaseModel):
    quote: str
    topic: str


class StructuredPayload(BaseModel):
    """Mirrors documents.structured in the existing demo schema, with two added
    fields used by deal.financials (ev_proposed_usd, ev_ebitda_multiple)."""

    company: Optional[str] = None
    revenue_ltm_usd: Optional[float] = None
    ebitda_ltm_usd: Optional[float] = None
    ebitda_margin: Optional[float] = None
    revenue_cagr_3yr: Optional[float] = None
    ev_proposed_usd: Optional[float] = None
    ev_ebitda_multiple: Optional[float] = None
    growth_drivers: list[str] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)


class ReturnsExtract(BaseModel):
    """Realized returns extracted from returns_summary / funds_flow / exit IC memo.
    Only realized/final/actual figures — never pro-forma projections."""

    irr: Optional[float] = None
    moic: Optional[float] = None
    holding_period_years: Optional[int] = None
    exit_year: Optional[int] = None
    exit_ev_usd: Optional[float] = None
    entry_ev_usd: Optional[float] = None
    exit_type: Optional[ExitType] = None


class UnderwritingCaseYear(BaseModel):
    revenue_usd: Optional[float] = None
    ebitda_usd: Optional[float] = None
    ebitda_margin: Optional[float] = None
    ev_usd: Optional[float] = None
    moic: Optional[float] = None
    irr: Optional[float] = None


class PeriodActual(BaseModel):
    """One reporting period of realized actuals from a board package or
    quarterly_financials. `quarter` is None for full fiscal-year rollups and
    1–4 for single-quarter rows. A single doc may carry multiple PeriodActual
    entries (e.g., a board deck with a 3-year history table)."""

    year: int
    quarter: Optional[int] = None
    revenue_usd: Optional[float] = None
    ebitda_usd: Optional[float] = None
    ebitda_margin: Optional[float] = None


class DealContext(BaseModel):
    """Any doc may emit this with whatever deal-level fields it can confidently
    extract. The resolver aggregates across all docs via per-field plurality vote,
    so per-field nulls are expected (a Legal/Term_Sheet might know company_canonical
    but not sector, etc.)."""

    company_canonical: Optional[str] = None
    codename_detected: Optional[str] = None
    sector: Optional[Sector] = None
    subsector: Optional[str] = None
    geography: Optional[Geography] = None
    deal_type: Optional[DealType] = None
    thesis_themes: list[ThesisTheme] = Field(default_factory=list)
    risk_flags: list[RiskTheme] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)

    @field_validator("thesis_themes", mode="before")
    @classmethod
    def _filter_thesis_themes(cls, v):
        # Drop values that aren't valid thesis themes (the LLM occasionally puts
        # risk-theme strings here or vice versa). Strict enum stays in the tool
        # schema; this rescues almost-right responses at parse time.
        if isinstance(v, list):
            return [item for item in v if isinstance(item, str) and item in _THESIS_VALUES]
        return v

    @field_validator("risk_flags", mode="before")
    @classmethod
    def _filter_risk_flags(cls, v):
        if isinstance(v, list):
            return [item for item in v if isinstance(item, str) and item in _RISK_VALUES]
        return v


TaxonomyField = Literal[
    "sector",
    "subsector",
    "geography",
    "deal_type",
    "thesis_theme",
    "risk_theme",
    "doc_type",
]


class TaxonomyProposal(BaseModel):
    """Emitted when the LLM wanted to use a value not in the firm's taxonomy.
    closest_existing is always non-null — it's what gets persisted. The proposal
    flows to taxonomy_proposals.yaml for human review."""

    field: TaxonomyField
    proposed_value: str
    closest_existing: str
    rationale: str
    confidence: float = Field(ge=0.0, le=1.0)


class TaggerOutput(BaseModel):
    """LLM tool-use schema. Every Sonnet call returns exactly this shape."""

    doc_type: DocType
    title: str
    date: Optional[_date] = None
    summary: str
    key_quotes: list[KeyQuote] = Field(default_factory=list)
    structured: StructuredPayload = Field(default_factory=StructuredPayload)

    # Disambiguates entry- vs exit-time ic_memos. Null for non-ic_memo docs.
    memo_purpose: Optional[Literal["entry", "exit"]] = None

    # Optional sub-payloads — populated only for docs whose doc_type warrants them
    # (see prompts/doc_tagger/v1_3.py for the conditional rules). Resolver branches
    # consume these; active-kind ignores them.
    returns_extract: Optional[ReturnsExtract] = None
    underwriting_case_extract: dict[str, UnderwritingCaseYear] = Field(default_factory=dict)
    period_actuals: list[PeriodActual] = Field(default_factory=list)

    deal_context: Optional[DealContext] = None
    taxonomy_proposals: list[TaxonomyProposal] = Field(default_factory=list)
    extraction_warnings: list[str] = Field(default_factory=list)

    @field_validator("date", mode="before")
    @classmethod
    def _coerce_partial_date(cls, v):
        # Allow YYYY-MM by coercing to YYYY-MM-01. Empty strings → None.
        if v is None or v == "":
            return None
        if isinstance(v, str) and _YYYY_MM_RE.match(v):
            return f"{v}-01"
        return v

    @field_validator("key_quotes", mode="before")
    @classmethod
    def _parse_key_quotes_string(cls, v):
        # Anthropic tool-use occasionally double-encodes a complex array as a JSON string.
        if isinstance(v, str):
            try:
                parsed = json.loads(v)
                return parsed if isinstance(parsed, list) else []
            except json.JSONDecodeError:
                return []
        return v


# -----------------------------------------------------------------------------
# Resolver (Stage 5)
# -----------------------------------------------------------------------------


class ResolverDisagreement(BaseModel):
    """When the per-field vote is less than unanimous, log what disagreed.
    Surfaced in report.md so the analyst sees real ambiguity vs. silently picked plurality."""

    field: str
    chosen_value: object = None
    chosen_voters: list[str] = Field(default_factory=list)
    dissenting: dict[str, list[str]] = Field(default_factory=dict)
    note: str = ""
