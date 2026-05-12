"""JSON fixture loaders. Cached at import time."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "data"


def _load(filename: str) -> dict[str, Any]:
    path = DATA_DIR / filename
    with path.open() as f:
        return json.load(f)


@lru_cache(maxsize=1)
def load_deals() -> list[dict[str, Any]]:
    return _load("deals.json")["deals"]


@lru_cache(maxsize=1)
def load_people() -> list[dict[str, Any]]:
    return _load("deals.json")["people"]


@lru_cache(maxsize=1)
def load_documents() -> list[dict[str, Any]]:
    return _load("documents.json")["documents"]


@lru_cache(maxsize=1)
def load_experts() -> list[dict[str, Any]]:
    return _load("experts.json")["experts"]


@lru_cache(maxsize=1)
def load_macro() -> list[dict[str, Any]]:
    return _load("macro.json")["snapshots"]


@lru_cache(maxsize=1)
def load_investment_criteria() -> dict[str, Any]:
    return _load("investment_criteria.json")


@lru_cache(maxsize=1)
def load_market_companies() -> list[dict[str, Any]]:
    return _load("market_companies.json")["companies"]


def get_deal(deal_id: str) -> dict[str, Any] | None:
    for d in load_deals():
        if d["deal_id"] == deal_id:
            return d
    return None


def get_document(doc_id: str) -> dict[str, Any] | None:
    for d in load_documents():
        if d["doc_id"] == doc_id:
            return d
    return None


def get_expert(expert_id: str) -> dict[str, Any] | None:
    for e in load_experts():
        if e["expert_id"] == expert_id:
            return e
    return None


def get_person(person_id: str) -> dict[str, Any] | None:
    for p in load_people():
        if p["person_id"] == person_id:
            return p
    return None
