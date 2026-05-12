"""Document and expert-quote search."""

from __future__ import annotations

from typing import Any, Optional

from rapidfuzz import fuzz

from ..data_loader import get_document, get_expert, load_documents
from ..matching import resolve_deal


def _score_quote(query: str, text: str) -> int:
    return max(
        fuzz.partial_ratio(query.lower(), text.lower()),
        fuzz.token_set_ratio(query.lower(), text.lower()),
    )


def search_documents(
    query: str,
    deal: Optional[str] = None,
    doc_type: Optional[str] = None,
    top_k: int = 10,
) -> dict[str, Any]:
    """Search deal documents (CIMs, expert calls, IC memos, DD reports) for quotes/passages.

    Returns hits ranked by fuzzy text match, each with the matched quote, document metadata,
    and expert attribution where applicable. Use this for "who said X about Y" questions.

    Args:
        query: Free-text query (e.g. "channel pricing power declined").
        deal: Optional deal filter (ID/codename/alias/company).
        doc_type: Optional doc_type filter: cim | expert_call | ic_memo | dd_report | financial_model.
        top_k: Max hits.
    """
    target_deal_id: Optional[str] = None
    if deal:
        d = resolve_deal(deal)
        if not d:
            return {"error": f"No deal matched '{deal}'."}
        target_deal_id = d["deal_id"]

    hits: list[dict[str, Any]] = []
    for doc in load_documents():
        if target_deal_id and doc["deal_id"] != target_deal_id:
            continue
        if doc_type and doc["doc_type"] != doc_type:
            continue
        searchable_blocks: list[tuple[str, dict[str, Any] | None]] = []
        for kq in doc.get("key_quotes") or []:
            searchable_blocks.append((kq["quote"], kq))
        if doc.get("summary"):
            searchable_blocks.append((doc["summary"], None))
        if doc.get("full_text_excerpt"):
            searchable_blocks.append((doc["full_text_excerpt"], None))

        best: tuple[int, str, dict[str, Any] | None] | None = None
        for text, meta in searchable_blocks:
            s = _score_quote(query, text)
            if best is None or s > best[0]:
                best = (s, text, meta)
        if best and best[0] >= 60:
            expert = get_expert(doc["expert_id"]) if doc.get("expert_id") else None
            hits.append({
                "score": best[0],
                "doc_id": doc["doc_id"],
                "deal_id": doc["deal_id"],
                "doc_type": doc["doc_type"],
                "title": doc["title"],
                "date": doc["date"],
                "match_text": best[1],
                "topic": (best[2] or {}).get("topic") if best[2] else None,
                "expert": (
                    {"expert_id": expert["expert_id"], "name": expert["name"], "firm": expert["firm"], "title": expert["title"]}
                    if expert else None
                ),
            })

    hits.sort(key=lambda x: -x["score"])
    return {"query": query, "count": len(hits[:top_k]), "hits": hits[:top_k]}


def get_document_by_id(doc_id: str) -> dict[str, Any]:
    """Return the full record for a document by ID."""
    doc = get_document(doc_id)
    if not doc:
        return {"error": f"No document matched '{doc_id}'."}
    expert = get_expert(doc["expert_id"]) if doc.get("expert_id") else None
    return {**doc, "expert_detail": expert}
