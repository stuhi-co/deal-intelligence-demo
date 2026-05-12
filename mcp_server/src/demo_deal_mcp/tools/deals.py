"""Tools for core deal lookup: list, get, financials, outcome."""

from __future__ import annotations

from typing import Any, Optional

from ..data_loader import load_deals
from ..matching import resolve_deal


def _stage_year(deal: dict[str, Any]) -> int:
    return int(deal["stage_entered_at"][:4])


def _summary(deal: dict[str, Any]) -> dict[str, Any]:
    fin = deal.get("financials", {})
    return {
        "deal_id": deal["deal_id"],
        "codename": deal["codename"],
        "company": deal["company_canonical"],
        "status": deal["status"],
        "year": _stage_year(deal),
        "sector": deal["sector"],
        "subsector": deal["subsector"],
        "geography": deal["geography"],
        "deal_type": deal["deal_type"],
        "revenue_ltm_usd": fin.get("revenue_ltm_usd"),
        "ebitda_ltm_usd": fin.get("ebitda_ltm_usd"),
        "ev_proposed_usd": fin.get("ev_proposed_usd"),
        "ev_ebitda_multiple": fin.get("ev_ebitda_multiple"),
    }


def list_deals(
    sector: Optional[str] = None,
    subsector: Optional[str] = None,
    status: Optional[str] = None,
    year_from: Optional[int] = None,
    year_to: Optional[int] = None,
    keyword: Optional[str] = None,
) -> dict[str, Any]:
    """List deals in the firm's history, optionally filtered.

    Use this for any "show me deals where X" question — pet food deals, manufacturing exits,
    deals in a year range, deals matching a keyword, etc.

    Args:
        sector: Sector enum key (e.g. "consumer_products", "manufacturing", "healthcare_services").
        subsector: Subsector enum key (e.g. "pet_food", "industrial_components").
        status: Deal status: active_diligence | closed_exited | closed_held | passed | dead.
        year_from: Inclusive lower bound on the year the deal entered diligence.
        year_to: Inclusive upper bound.
        keyword: Free-text match against codename, company name, or aliases.
    """
    deals = load_deals()
    out: list[dict[str, Any]] = []
    for d in deals:
        if sector and d["sector"] != sector:
            continue
        if subsector and d["subsector"] != subsector:
            continue
        if status and d["status"] != status:
            continue
        yr = _stage_year(d)
        if year_from is not None and yr < year_from:
            continue
        if year_to is not None and yr > year_to:
            continue
        if keyword:
            hay = " ".join([d["codename"], d["company_canonical"], *d.get("aliases", [])]).lower()
            if keyword.lower() not in hay:
                continue
        out.append(_summary(d))
    return {"count": len(out), "deals": out}


def get_deal(deal: str) -> dict[str, Any]:
    """Return the full record for a deal identified by ID, codename, alias, or company name."""
    d = resolve_deal(deal)
    if not d:
        return {"error": f"No deal matched '{deal}'."}
    return d


def get_deal_financials(deal: str) -> dict[str, Any]:
    """Return entry financials for a deal: revenue, EBITDA, margin, growth, EV, and EV/EBITDA multiple."""
    d = resolve_deal(deal)
    if not d:
        return {"error": f"No deal matched '{deal}'."}
    fin = d.get("financials", {})
    return {
        "deal_id": d["deal_id"],
        "codename": d["codename"],
        "company": d["company_canonical"],
        "stage_entered_at": d["stage_entered_at"],
        **fin,
    }


def get_deal_outcome(deal: str) -> dict[str, Any]:
    """Return the deal's outcome: decision, IRR, MOIC, holding period, exit type, and narrative.

    For active_diligence deals, returns status only. For passed/dead deals, returns the decision
    reason. For closed_exited/closed_held deals, returns the full return profile.
    """
    d = resolve_deal(deal)
    if not d:
        return {"error": f"No deal matched '{deal}'."}
    out = d.get("outcome")
    if out is None:
        return {
            "deal_id": d["deal_id"],
            "codename": d["codename"],
            "status": d["status"],
            "note": "Deal is in active diligence; no outcome yet.",
        }
    return {
        "deal_id": d["deal_id"],
        "codename": d["codename"],
        "company": d["company_canonical"],
        "status": d["status"],
        **out,
    }
