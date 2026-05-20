"""One-shot: archive 15 hand-seeded fixture deals out of canonical data files.

Splits data/deals.json, data/documents.json, data/experts.json into:
  - canonical files (truly-ingested deals only)
  - .fixture.json companions (archived fixtures)

`people` in deals.json is shared across the demo and stays in the canonical file.
"""
from __future__ import annotations

import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"

FIXTURE_IDS = {
    "deal_acme_2021", "deal_atlas_2022", "deal_cascade_2024",
    "deal_crunch_2026", "deal_falcon_2025", "deal_forge_2018",
    "deal_healthroll_2020", "deal_kibble_2024", "deal_midstates_2022",
    "deal_orion_2026", "deal_packtech_2022", "deal_paws_2023",
    "deal_polymer_2019", "deal_techflow_2019", "deal_whisker_2025",
}


def main() -> None:
    deals_data = json.loads((DATA / "deals.json").read_text())
    docs_data = json.loads((DATA / "documents.json").read_text())
    experts_data = json.loads((DATA / "experts.json").read_text())

    keep_deals = [d for d in deals_data["deals"] if d["deal_id"] not in FIXTURE_IDS]
    archive_deals = [d for d in deals_data["deals"] if d["deal_id"] in FIXTURE_IDS]

    keep_docs = [d for d in docs_data["documents"] if d["deal_id"] not in FIXTURE_IDS]
    archive_docs = [d for d in docs_data["documents"] if d["deal_id"] in FIXTURE_IDS]

    ingested_expert_refs = {d.get("expert_id") for d in keep_docs if d.get("expert_id")}
    keep_experts = [e for e in experts_data["experts"] if e["expert_id"] in ingested_expert_refs]
    archive_experts = [e for e in experts_data["experts"] if e["expert_id"] not in ingested_expert_refs]

    (DATA / "deals.json").write_text(json.dumps({"deals": keep_deals, "people": deals_data["people"]}, indent=2) + "\n")
    (DATA / "deals.fixture.json").write_text(json.dumps({"deals": archive_deals}, indent=2) + "\n")

    (DATA / "documents.json").write_text(json.dumps({"documents": keep_docs}, indent=2) + "\n")
    (DATA / "documents.fixture.json").write_text(json.dumps({"documents": archive_docs}, indent=2) + "\n")

    (DATA / "experts.json").write_text(json.dumps({"experts": keep_experts}, indent=2) + "\n")
    (DATA / "experts.fixture.json").write_text(json.dumps({"experts": archive_experts}, indent=2) + "\n")

    print(f"deals: {len(keep_deals)} canonical / {len(archive_deals)} archived")
    print(f"docs:  {len(keep_docs)} canonical / {len(archive_docs)} archived")
    print(f"experts: {len(keep_experts)} canonical / {len(archive_experts)} archived")


if __name__ == "__main__":
    main()
