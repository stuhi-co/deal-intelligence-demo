"""Precedent/comparable analysis."""

from __future__ import annotations

from statistics import mean
from typing import Any, Optional

from ..data_loader import load_deals
from ..matching import resolve_deal
from ..models import CompanyProfile


def _summary(deal: dict[str, Any]) -> dict[str, Any]:
    fin = deal.get("financials", {})
    out = deal.get("outcome") or {}
    return {
        "deal_id": deal["deal_id"],
        "codename": deal["codename"],
        "company": deal["company_canonical"],
        "year": int(deal["stage_entered_at"][:4]),
        "status": deal["status"],
        "sector": deal["sector"],
        "subsector": deal["subsector"],
        "revenue_ltm_usd": fin.get("revenue_ltm_usd"),
        "ebitda_ltm_usd": fin.get("ebitda_ltm_usd"),
        "ebitda_margin": fin.get("ebitda_margin"),
        "ev_proposed_usd": fin.get("ev_proposed_usd"),
        "ev_ebitda_multiple": fin.get("ev_ebitda_multiple"),
        "irr": out.get("irr"),
        "moic": out.get("moic"),
        "exit_type": out.get("exit_type"),
    }


def find_precedent_deals(
    deal: Optional[str] = None,
    profile: Optional[CompanyProfile] = None,
    top_k: int = 5,
) -> dict[str, Any]:
    """Return precedent deals similar to either an existing deal or a free-form CompanyProfile.

    When `deal` is given, returns the precomputed `similar_deals_computed` set enriched with
    outcomes. When `profile` is given, scores all closed deals against the profile by sector
    match (+0.4), subsector match (+0.3), size proximity (+up to 0.2), margin proximity (+up to 0.1).

    Args:
        deal: Existing deal reference (ID/codename/alias/company name).
        profile: Free-form company profile (e.g. parsed from a CIM).
        top_k: Max results.
    """
    if deal:
        d = resolve_deal(deal)
        if not d:
            return {"error": f"No deal matched '{deal}'."}
        results = []
        for sim in d.get("similar_deals_computed", [])[:top_k]:
            target = next((x for x in load_deals() if x["deal_id"] == sim["deal_id"]), None)
            if not target:
                continue
            results.append({
                "score": sim["score"],
                "drivers": sim["drivers"],
                **_summary(target),
            })
        return {"anchor": _summary(d), "precedents": results}

    if profile is None:
        return {"error": "Provide either `deal` or `profile`."}

    scored: list[tuple[float, dict[str, Any]]] = []
    for d in load_deals():
        if d.get("outcome") is None:
            continue
        score = 0.0
        if profile.sector and d["sector"] == profile.sector:
            score += 0.4
        if profile.subsector and d["subsector"] == profile.subsector:
            score += 0.3
        rev_d = (d.get("financials") or {}).get("revenue_ltm_usd")
        if profile.revenue_usd and rev_d:
            ratio = min(rev_d, profile.revenue_usd) / max(rev_d, profile.revenue_usd)
            score += 0.2 * ratio
        mar_d = (d.get("financials") or {}).get("ebitda_margin")
        if profile.ebitda_margin and mar_d:
            score += 0.1 * (1 - min(abs(mar_d - profile.ebitda_margin) / 0.2, 1.0))
        if score > 0:
            scored.append((score, d))
    scored.sort(key=lambda x: -x[0])
    return {
        "anchor": {"profile": profile.model_dump()},
        "precedents": [
            {"score": round(s, 3), **_summary(d)} for s, d in scored[:top_k]
        ],
    }


def compare_deals(deal_ids: list[str], dimensions: Optional[list[str]] = None) -> dict[str, Any]:
    """Side-by-side comparison of two or more deals across financial and outcome dimensions.

    Args:
        deal_ids: Deal references (any of ID/codename/alias/company name).
        dimensions: Optional subset of fields to compare. Defaults to a sensible set.
    """
    resolved = [resolve_deal(x) for x in deal_ids]
    if any(r is None for r in resolved):
        missing = [orig for orig, r in zip(deal_ids, resolved) if r is None]
        return {"error": f"Could not resolve: {missing}"}
    default_dims = [
        "year", "sector", "subsector", "revenue_ltm_usd", "ebitda_ltm_usd",
        "ebitda_margin", "ev_proposed_usd", "ev_ebitda_multiple", "irr", "moic", "exit_type",
    ]
    dims = dimensions or default_dims
    rows = []
    for d in resolved:
        summary = _summary(d)
        rows.append({
            "deal_id": d["deal_id"],
            "codename": d["codename"],
            **{k: summary.get(k) for k in dims},
        })
    return {"dimensions": dims, "rows": rows}


def analyze_exit_drivers(sector: str, status: str = "closed_exited") -> dict[str, Any]:
    """Aggregate analysis of exits (default: closed_exited) within a sector — common drivers and stats.

    Returns mean IRR/MOIC, most common thesis themes and risk flags, and the underlying deal list.
    Use this for "what did our best deals in X sector have in common" questions.
    """
    deals = [
        d for d in load_deals()
        if d["sector"] == sector and d["status"] == status and d.get("outcome")
    ]
    if not deals:
        return {"sector": sector, "status": status, "count": 0, "deals": []}

    irrs = [d["outcome"].get("irr") for d in deals if d["outcome"].get("irr") is not None]
    moics = [d["outcome"].get("moic") for d in deals if d["outcome"].get("moic") is not None]
    entry_multiples = [
        d["financials"].get("ev_ebitda_multiple") for d in deals
        if d.get("financials", {}).get("ev_ebitda_multiple") is not None
    ]
    margin_lift: list[float] = []
    for d in deals:
        actuals = d.get("portco_actuals") or []
        if len(actuals) >= 2:
            margin_lift.append(actuals[-1]["ebitda_margin"] - actuals[0]["ebitda_margin"])

    theme_counts: dict[str, int] = {}
    risk_counts: dict[str, int] = {}
    for d in deals:
        for t in d.get("thesis_themes", []):
            theme_counts[t] = theme_counts.get(t, 0) + 1
        for r in d.get("risk_flags", []):
            risk_counts[r] = risk_counts.get(r, 0) + 1

    best = max(deals, key=lambda d: d["outcome"].get("irr") or 0)
    return {
        "sector": sector,
        "status": status,
        "count": len(deals),
        "aggregate": {
            "mean_irr": round(mean(irrs), 3) if irrs else None,
            "mean_moic": round(mean(moics), 2) if moics else None,
            "mean_entry_multiple": round(mean(entry_multiples), 2) if entry_multiples else None,
            "mean_ebitda_margin_lift": round(mean(margin_lift), 3) if margin_lift else None,
        },
        "top_thesis_themes": sorted(theme_counts.items(), key=lambda x: -x[1]),
        "top_risk_flags": sorted(risk_counts.items(), key=lambda x: -x[1]),
        "best_performer": _summary(best),
        "deals": [_summary(d) for d in deals],
    }
