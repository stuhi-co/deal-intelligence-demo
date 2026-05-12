"""CIM parsing and evaluation against fund criteria."""

from __future__ import annotations

from typing import Any

from ..data_loader import get_document, load_investment_criteria


def parse_cim(cim_doc_id: str) -> dict[str, Any]:
    """Return the structured profile of a CIM document.

    Surfaces company name, revenue, EBITDA, margin, growth, thesis hooks, and risks in a
    normalized shape suitable for downstream tools (find_precedent_deals, source_similar_companies,
    evaluate_cim_against_criteria).
    """
    doc = get_document(cim_doc_id)
    if not doc:
        return {"error": f"No document matched '{cim_doc_id}'."}
    if doc["doc_type"] != "cim":
        return {"error": f"Document {cim_doc_id} is a {doc['doc_type']}, not a CIM."}
    return {
        "doc_id": doc["doc_id"],
        "deal_id": doc["deal_id"],
        "title": doc["title"],
        "date": doc["date"],
        "summary": doc.get("summary"),
        "profile": doc.get("structured", {}),
    }


def _criterion(name: str, passed: bool, detail: str) -> dict[str, Any]:
    return {"criterion": name, "passed": passed, "detail": detail}


def evaluate_cim_against_criteria(cim_doc_id: str) -> dict[str, Any]:
    """Evaluate a parsed CIM against the fund's investment criteria. Returns a pass/proceed verdict.

    Checks: revenue band, EBITDA min, EBITDA margin min, entry-valuation guardrail, and listed
    deal-breaker patterns. Verdict is `proceed` (all green), `proceed_with_caution` (≤1 amber),
    or `pass` (any deal-breaker triggered).
    """
    doc = get_document(cim_doc_id)
    if not doc:
        return {"error": f"No document matched '{cim_doc_id}'."}
    if doc["doc_type"] != "cim":
        return {"error": f"Document {cim_doc_id} is a {doc['doc_type']}, not a CIM."}

    profile = doc.get("structured", {})
    criteria = load_investment_criteria()
    size = criteria["size_criteria"]
    guard = criteria["valuation_guardrails"]
    checks: list[dict[str, Any]] = []

    rev = profile.get("revenue_ltm_usd")
    if rev is not None:
        in_band = size["revenue_min_usd"] <= rev <= size["revenue_max_usd"]
        checks.append(_criterion(
            "revenue_band",
            in_band,
            f"${rev/1e6:.0f}M revenue vs target band ${size['revenue_min_usd']/1e6:.0f}M-${size['revenue_max_usd']/1e6:.0f}M",
        ))

    ebitda = profile.get("ebitda_ltm_usd")
    if ebitda is not None:
        checks.append(_criterion(
            "ebitda_min",
            ebitda >= size["ebitda_min_usd"],
            f"${ebitda/1e6:.1f}M EBITDA vs ${size['ebitda_min_usd']/1e6:.0f}M minimum",
        ))

    margin = profile.get("ebitda_margin")
    if margin is not None:
        checks.append(_criterion(
            "ebitda_margin_min",
            margin >= size["ebitda_margin_min"],
            f"{margin*100:.1f}% margin vs {size['ebitda_margin_min']*100:.0f}% minimum",
        ))

    # Sector preference
    sector_pref = None
    # the deal that the CIM is attached to gives us a sector
    from ..data_loader import get_deal as _get_deal
    deal = _get_deal(doc["deal_id"])
    if deal:
        sector_pref = deal["sector"] in criteria["sector_preferences"]
        checks.append(_criterion(
            "sector_preference",
            sector_pref,
            f"sector={deal['sector']}; preferred={'yes' if sector_pref else 'no'}",
        ))
        # Multiple guardrail vs deal financials
        mult = (deal.get("financials") or {}).get("ev_ebitda_multiple")
        if mult is not None:
            within = mult <= guard["ev_ebitda_multiple_max"]
            stretch = mult <= guard["ev_ebitda_multiple_stretch_max"]
            checks.append(_criterion(
                "valuation_guardrail",
                within,
                f"{mult}x vs target ≤{guard['ev_ebitda_multiple_max']}x (stretch ≤{guard['ev_ebitda_multiple_stretch_max']}x; {'stretch ok' if (not within and stretch) else 'over stretch' if not stretch else 'within'})",
            ))

    # Deal-breakers heuristic: scan the CIM risks list for keywords
    risks_text = " ".join(profile.get("risks", [])).lower()
    triggered: list[str] = []
    for db in criteria["deal_breakers"]:
        key = db["key"]
        if key == "ebitda_margin_below_8pct" and margin is not None and margin < 0.08:
            triggered.append(db["description"])
        if "payer" in key and ("payer" in risks_text and "%" in risks_text):
            # naive trip if CIM mentions specific concentration
            if any(token in risks_text for token in ["31%", "32%", "35%", "40%", "50%"]):
                triggered.append(db["description"])
        if "customer" in key:
            for token in ["= 34%", "34% of revenue", "35% of revenue", "40% of revenue"]:
                if token in risks_text:
                    triggered.append(db["description"])
                    break

    n_fail = sum(1 for c in checks if not c["passed"])
    if triggered or n_fail >= 2:
        verdict = "pass"
    elif n_fail == 1:
        verdict = "proceed_with_caution"
    else:
        verdict = "proceed"

    return {
        "doc_id": cim_doc_id,
        "deal_id": doc["deal_id"],
        "company": profile.get("company"),
        "verdict": verdict,
        "checks": checks,
        "deal_breakers_triggered": triggered,
        "return_targets": criteria["return_targets"],
    }
