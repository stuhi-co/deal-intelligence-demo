"""Fund investment criteria lookup."""

from __future__ import annotations

from typing import Any

from ..data_loader import load_investment_criteria


def get_investment_criteria() -> dict[str, Any]:
    """Return the fund's investment criteria: size band, sector preferences, thesis preferences,
    deal-breakers, return targets, and valuation guardrails. Used to evaluate new opportunities."""
    return load_investment_criteria()
