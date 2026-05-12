"""Profile and sourcing tools — surface company profile, find lookalikes in market universe."""

from __future__ import annotations

from typing import Any, Optional

from ..data_loader import load_market_companies
from ..matching import resolve_deal
from ..models import CompanyProfile


def get_company_profile(company: str) -> dict[str, Any]:
    """Return a normalized profile for a company referenced by deal codename, alias, or canonical name.

    The profile is what `source_similar_companies` consumes — surface it back to the user for
    confirmation before searching the market universe.
    """
    d = resolve_deal(company)
    if not d:
        return {"error": f"No company/deal matched '{company}'."}
    fin = d.get("financials", {})
    profile = CompanyProfile(
        name=d["company_canonical"],
        sector=d["sector"],
        subsector=d["subsector"],
        geography=d["geography"],
        revenue_usd=fin.get("revenue_ltm_usd"),
        ebitda_usd=fin.get("ebitda_ltm_usd"),
        ebitda_margin=fin.get("ebitda_margin"),
        revenue_cagr_3yr=fin.get("revenue_cagr_3yr"),
        thesis_themes=d.get("thesis_themes", []),
        risk_flags=d.get("risk_flags", []),
    )
    return {
        "deal_id": d["deal_id"],
        "codename": d["codename"],
        "profile": profile.model_dump(),
        "confirmation_prompt": "Confirm this profile is accurate before sourcing similar companies.",
    }


def source_similar_companies(profile: CompanyProfile, top_k: int = 10) -> dict[str, Any]:
    """Return top-k companies from the market universe matching a CompanyProfile.

    Scoring: sector match (+0.4), subsector match (+0.3), revenue proximity (+up to 0.2),
    margin proximity (+up to 0.1).
    """
    scored: list[tuple[float, dict[str, Any], dict[str, str]]] = []
    for mc in load_market_companies():
        score = 0.0
        drivers: dict[str, str] = {}
        if profile.sector and mc["sector"] == profile.sector:
            score += 0.4
            drivers["sector"] = "match"
        if profile.subsector and mc["subsector"] == profile.subsector:
            score += 0.3
            drivers["subsector"] = "match"
        if profile.revenue_usd and mc.get("revenue_usd"):
            ratio = min(mc["revenue_usd"], profile.revenue_usd) / max(mc["revenue_usd"], profile.revenue_usd)
            score += 0.2 * ratio
            drivers["size_ratio"] = f"{ratio:.2f}"
        if profile.ebitda_margin and mc.get("ebitda_margin"):
            prox = 1 - min(abs(mc["ebitda_margin"] - profile.ebitda_margin) / 0.2, 1.0)
            score += 0.1 * prox
            drivers["margin_proximity"] = f"{prox:.2f}"
        if score > 0:
            scored.append((score, mc, drivers))
    scored.sort(key=lambda x: -x[0])
    return {
        "profile": profile.model_dump(),
        "count": len(scored[:top_k]),
        "matches": [
            {"score": round(s, 3), "drivers": drv, "company": mc}
            for s, mc, drv in scored[:top_k]
        ],
    }
