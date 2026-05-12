"""Consistency check across data/ fixtures.

Asserts:
  - every doc_id referenced in deals.json exists in documents.json
  - every expert_id referenced in documents.json exists in experts.json
  - every deal_id referenced in documents.json exists in deals.json
  - every enum value used in deals.json (sector, subsector, status, thesis, risk) is declared in enums.yaml
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def _load_json(name: str) -> dict:
    return json.loads((DATA / name).read_text())


def _load_yaml(name: str) -> dict:
    return yaml.safe_load((ROOT / name).read_text())


def main() -> int:
    deals = _load_json("deals.json")["deals"]
    documents = _load_json("documents.json")["documents"]
    experts = _load_json("experts.json")["experts"]
    enums = _load_yaml("enums.yaml")

    errors: list[str] = []

    doc_ids = {d["doc_id"] for d in documents}
    expert_ids = {e["expert_id"] for e in experts}
    deal_ids = {d["deal_id"] for d in deals}

    for deal in deals:
        for ref in deal.get("source_documents", []):
            if ref not in doc_ids:
                errors.append(f"deal {deal['deal_id']} references missing doc {ref}")
        if deal["sector"] not in enums["sector"]:
            errors.append(f"deal {deal['deal_id']}: sector {deal['sector']} not in enums")
        sub_list = enums["subsector"].get(deal["sector"], [])
        if deal["subsector"] not in sub_list:
            errors.append(f"deal {deal['deal_id']}: subsector {deal['subsector']} not in enums for sector {deal['sector']}")
        if deal["status"] not in enums["deal_status"]:
            errors.append(f"deal {deal['deal_id']}: status {deal['status']} not in enums")
        if deal["deal_type"] not in enums["deal_type"]:
            errors.append(f"deal {deal['deal_id']}: deal_type {deal['deal_type']} not in enums")
        for t in deal.get("thesis_themes", []):
            if t not in enums["thesis_theme"]:
                errors.append(f"deal {deal['deal_id']}: thesis {t} not in enums")
        for r in deal.get("risk_flags", []):
            if r not in enums["risk_theme"]:
                errors.append(f"deal {deal['deal_id']}: risk {r} not in enums")

    for doc in documents:
        if doc.get("deal_id") and doc["deal_id"] not in deal_ids:
            errors.append(f"doc {doc['doc_id']}: deal_id {doc['deal_id']} not in deals")
        if doc.get("expert_id") and doc["expert_id"] not in expert_ids:
            errors.append(f"doc {doc['doc_id']}: expert_id {doc['expert_id']} not in experts")
        if doc["doc_type"] not in enums["doc_type"]:
            errors.append(f"doc {doc['doc_id']}: doc_type {doc['doc_type']} not in enums")

    for exp in experts:
        for ref in exp.get("deals_used_in", []):
            if ref not in deal_ids:
                errors.append(f"expert {exp['expert_id']}: deal_id {ref} not in deals")

    if errors:
        print("FAIL — consistency errors:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK — {len(deals)} deals, {len(documents)} documents, {len(experts)} experts. All references consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
