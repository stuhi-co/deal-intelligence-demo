"""Macro environment lookups."""

from __future__ import annotations

from typing import Any, Optional

from ..data_loader import load_macro


def _find(sector: str, as_of: str) -> dict[str, Any] | None:
    for s in load_macro():
        if s["sector"] == sector and s["as_of"] == as_of:
            return s
    return None


def get_macro_snapshot(sector: str, as_of: str) -> dict[str, Any]:
    """Return the macro snapshot for a sector at a quarter (e.g. "2026-Q1").

    Args:
        sector: Sector enum key.
        as_of: Quarter string in YYYY-Qx format.
    """
    s = _find(sector, as_of)
    if not s:
        available = sorted({(x["sector"], x["as_of"]) for x in load_macro()})
        return {"error": f"No snapshot for {sector}@{as_of}.", "available": available}
    return s


def compare_macro(sector: str, date_a: str, date_b: str) -> dict[str, Any]:
    """Compare two macro snapshots for the same sector. Returns both snapshots plus a delta block.

    The delta block surfaces absolute change for each shared metric and sector KPI, plus a
    composite narrative built from the two snapshots' narratives.
    """
    a = _find(sector, date_a)
    b = _find(sector, date_b)
    if not a or not b:
        missing = [d for d, snap in [(date_a, a), (date_b, b)] if snap is None]
        return {"error": f"Missing snapshot(s) for {sector}: {missing}"}
    deltas: dict[str, Any] = {"metrics": {}, "sector_kpis": {}}
    for k in set(a["metrics"]) & set(b["metrics"]):
        deltas["metrics"][k] = round(b["metrics"][k] - a["metrics"][k], 4)
    for k in set(a.get("sector_kpis", {})) & set(b.get("sector_kpis", {})):
        deltas["sector_kpis"][k] = round(b["sector_kpis"][k] - a["sector_kpis"][k], 4)
    return {
        "sector": sector,
        "a": a,
        "b": b,
        "delta": deltas,
        "comparison_narrative": f"{date_a}: {a['narrative']}\n\n{date_b}: {b['narrative']}",
    }
