"""Resolve free-form deal references (codename, alias, company name, ID) to a deal record."""

from __future__ import annotations

from typing import Any

from rapidfuzz import fuzz, process

from .data_loader import load_deals, load_market_companies


def _candidates_for_deal(deal: dict[str, Any]) -> list[str]:
    cands = [deal["deal_id"], deal["codename"], deal["company_canonical"]]
    cands.extend(deal.get("aliases", []))
    return [c for c in cands if c]


def resolve_deal(query: str) -> dict[str, Any] | None:
    """Return the deal matching `query` (deal_id, codename, alias, or canonical company name).
    Falls back to fuzzy match (rapidfuzz, score >= 85)."""
    if not query:
        return None
    q = query.strip()
    deals = load_deals()

    for deal in deals:
        for cand in _candidates_for_deal(deal):
            if cand.lower() == q.lower():
                return deal

    # Fuzzy fallback across all candidates
    all_candidates: list[tuple[str, dict[str, Any]]] = []
    for deal in deals:
        for cand in _candidates_for_deal(deal):
            all_candidates.append((cand, deal))

    choices = [c[0] for c in all_candidates]
    match = process.extractOne(q, choices, scorer=fuzz.WRatio)
    if match and match[1] >= 85:
        _, _, idx = match
        return all_candidates[idx][1]
    return None


def resolve_company(query: str) -> dict[str, Any] | None:
    """Match a query to a market company OR a deal company. Deal wins on tie."""
    deal = resolve_deal(query)
    if deal:
        return {
            "source": "deal",
            "deal_id": deal["deal_id"],
            "name": deal["company_canonical"],
            "data": deal,
        }
    for mc in load_market_companies():
        if mc["name"].lower() == query.lower():
            return {"source": "market", "name": mc["name"], "data": mc}
    choices = {mc["name"]: mc for mc in load_market_companies()}
    match = process.extractOne(query, list(choices.keys()), scorer=fuzz.WRatio)
    if match and match[1] >= 85:
        return {"source": "market", "name": match[0], "data": choices[match[0]]}
    return None
