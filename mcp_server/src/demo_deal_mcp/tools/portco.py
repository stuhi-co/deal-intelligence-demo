"""Portco actuals vs underwriting base case."""

from __future__ import annotations

import re
from typing import Any

from ..matching import resolve_deal


def _variance(actual: float | None, plan: float | None) -> dict[str, Any] | None:
    if actual is None or plan is None:
        return None
    return {
        "actual": actual,
        "plan": plan,
        "absolute_variance": round(actual - plan, 4),
        "pct_variance": round((actual - plan) / plan, 4) if plan else None,
    }


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
        rows.append({
            "year": a["year"],
            "year_offset": offset,
            "milestone": "year_1" if offset <= 1 else ("year_3" if offset <= 3 else "year_5_exit"),
            "revenue": _variance(a.get("revenue_usd"), uw.get("revenue_usd")),
            "ebitda": _variance(a.get("ebitda_usd"), uw.get("ebitda_usd")),
            "ebitda_margin": _variance(a.get("ebitda_margin"), uw.get("ebitda_margin")),
        })
    return {
        "deal_id": d["deal_id"],
        "codename": d["codename"],
        "company": d["company_canonical"],
        "comparison": rows,
        "underwriting_case": case,
    }


def _pick_exit_year_key(case: dict[str, Any]) -> str | None:
    """Pick the exit-year key from an underwriting_case dict.

    Priority:
      1. Any key matching `year_<n>_exit` (highest n wins).
      2. The highest `year_<n>` key.
      3. 'base' if bear/base/bull labels are used.
      4. None if nothing fits.
    """
    exit_keys = [k for k in case if re.match(r"^year_\d+_exit$", k)]
    if exit_keys:
        return max(exit_keys, key=lambda k: int(re.search(r"\d+", k).group()))
    year_keys = [k for k in case if re.match(r"^year_\d+$", k)]
    if year_keys:
        return max(year_keys, key=lambda k: int(re.search(r"\d+", k).group()))
    if "base" in case:
        return "base"
    return None


def compare_exit_vs_underwriting(deal: str) -> dict[str, Any]:
    """For exited deals: variance between projected exit-year case and realized outcome.

    Compares the entry IC memo's exit-year projection (EV, MOIC, IRR) against the
    deal's realized `outcome`. Held deals should use `compare_portco_vs_underwriting`
    instead.
    """
    d = resolve_deal(deal)
    if not d:
        return {"error": f"No deal matched '{deal}'."}
    if d.get("status") != "closed_exited":
        return {
            "deal_id": d["deal_id"],
            "codename": d["codename"],
            "status": d.get("status"),
            "note": (
                "compare_exit_vs_underwriting only applies to exited deals. "
                "Use compare_portco_vs_underwriting for held portfolio companies."
            ),
        }
    case = d.get("underwriting_case")
    outcome = d.get("outcome")
    if not case or not outcome:
        return {
            "deal_id": d["deal_id"],
            "codename": d["codename"],
            "status": d["status"],
            "note": "Cannot compare — missing underwriting case or realized outcome.",
        }
    exit_key = _pick_exit_year_key(case)
    if exit_key is None:
        return {
            "deal_id": d["deal_id"],
            "codename": d["codename"],
            "status": d["status"],
            "note": "Cannot identify an exit-year milestone in underwriting case.",
            "underwriting_case_keys": list(case.keys()),
        }
    plan = case[exit_key]
    comparison = {
        "milestone": exit_key,
        "ev_usd": _variance(outcome.get("exit_ev_usd"), plan.get("ev_usd")),
        "moic": _variance(outcome.get("moic"), plan.get("moic")),
        "irr": _variance(outcome.get("irr"), plan.get("irr")),
    }
    return {
        "deal_id": d["deal_id"],
        "codename": d["codename"],
        "company": d["company_canonical"],
        "comparison": comparison,
        "underwriting_case": case,
        "outcome": outcome,
    }
