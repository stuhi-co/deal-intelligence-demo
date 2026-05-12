"""Portco actuals vs underwriting base case."""

from __future__ import annotations

from typing import Any

from ..matching import resolve_deal


def _underwriting_for_year(case: dict[str, Any], year_offset: int) -> dict[str, Any] | None:
    """Interpolate the underwriting case for a given year offset (year_1, year_3, year_5_exit)."""
    if year_offset <= 1:
        return case.get("year_1")
    if year_offset <= 3:
        return case.get("year_3")
    return case.get("year_5_exit")


def get_portco_performance(deal: str) -> dict[str, Any]:
    """Return actual annual performance (revenue, EBITDA, margin) for a closed deal."""
    d = resolve_deal(deal)
    if not d:
        return {"error": f"No deal matched '{deal}'."}
    actuals = d.get("portco_actuals")
    if not actuals:
        return {
            "deal_id": d["deal_id"],
            "codename": d["codename"],
            "status": d["status"],
            "note": "No portco actuals available (deal not closed or pre-investment).",
        }
    return {
        "deal_id": d["deal_id"],
        "codename": d["codename"],
        "company": d["company_canonical"],
        "actuals": actuals,
    }


def get_underwriting_case(deal: str) -> dict[str, Any]:
    """Return the underwriting base case (year-1, year-3, year-5 exit) for a closed deal."""
    d = resolve_deal(deal)
    if not d:
        return {"error": f"No deal matched '{deal}'."}
    case = d.get("underwriting_case")
    if not case:
        return {
            "deal_id": d["deal_id"],
            "codename": d["codename"],
            "status": d["status"],
            "note": "No underwriting case stored (deal not closed).",
        }
    return {
        "deal_id": d["deal_id"],
        "codename": d["codename"],
        "company": d["company_canonical"],
        "underwriting_case": case,
    }


def compare_portco_vs_underwriting(deal: str) -> dict[str, Any]:
    """Variance report: actuals vs underwriting base case, per metric per year.

    Each year's actuals are compared against the closest underwriting milestone (year_1,
    year_3, year_5_exit). Returns absolute and percent variance for revenue, EBITDA, and margin.
    """
    d = resolve_deal(deal)
    if not d:
        return {"error": f"No deal matched '{deal}'."}
    actuals = d.get("portco_actuals") or []
    case = d.get("underwriting_case")
    if not actuals or not case:
        return {
            "deal_id": d["deal_id"],
            "codename": d["codename"],
            "status": d["status"],
            "note": "Cannot compare — missing actuals or underwriting case.",
        }
    closed_year = int(d["stage_entered_at"][:4])
    rows = []
    for a in actuals:
        if a.get("quarter") is not None:
            # Underwriting case is annual; skip quarterly rows to avoid duplicate years.
            continue
        offset = a["year"] - closed_year
        uw = _underwriting_for_year(case, offset)
        if not uw:
            continue
        def variance(actual: float | None, plan: float | None) -> dict[str, Any] | None:
            if actual is None or plan is None:
                return None
            return {
                "actual": actual,
                "plan": plan,
                "absolute_variance": round(actual - plan, 4),
                "pct_variance": round((actual - plan) / plan, 4) if plan else None,
            }
        rows.append({
            "year": a["year"],
            "year_offset": offset,
            "milestone": "year_1" if offset <= 1 else ("year_3" if offset <= 3 else "year_5_exit"),
            "revenue": variance(a.get("revenue_usd"), uw.get("revenue_usd")),
            "ebitda": variance(a.get("ebitda_usd"), uw.get("ebitda_usd")),
            "ebitda_margin": variance(a.get("ebitda_margin"), uw.get("ebitda_margin")),
        })
    return {
        "deal_id": d["deal_id"],
        "codename": d["codename"],
        "company": d["company_canonical"],
        "comparison": rows,
        "underwriting_case": case,
    }
