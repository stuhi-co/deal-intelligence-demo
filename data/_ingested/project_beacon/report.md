# Ingestion report — project_beacon

Deal ID: `deal_project_beacon_2023`
Company canonical: `Lighthouse Logistics Group`
Sector / subsector: `transportation_logistics` / `last_mile_delivery`
Geography: `southeast_us`
Deal type: `platform`
Voted with 2 qualifying docs at confidence >= 0.9 (out of 2 tagged).

## Triage

### primary (2)
- `Marketing Materials/Project_Beacon_CIM_Sep2023.pdf`
- `Marketing Materials/Project_Beacon_Teaser_Sep2023.pdf`

### format_duplicate (2)
- `Marketing Materials/Project_Beacon_CIM_Sep2023.pptx` — PDF preferred over DOCX/PPTX twin
- `Marketing Materials/Project_Beacon_Teaser_Sep2023.pptx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Marketing Materials/Project_Beacon_CIM_Sep2023.pdf` → `doc_project_beacon_001` (cim)
- Title: Project Beacon – Confidential Information Memorandum: Lighthouse Logistics Group
- Date: 2023-09-01
- Summary: William Blair-prepared CIM for Lighthouse Logistics Group ("Project Beacon"), a technology-enabled regional LTL and final-mile freight provider headquartered in Charlotte, NC. The company operates 14 terminals across the Southeast and Mid-Atlantic, a fleet of 680 vehicles, and a proprietary route-optimization platform (BeaconOS). LTM Sep 2023 revenue of $218M and Adj. EBITDA of $33.7M (15.5% margin). The e-commerce final-mile segment grew 41% YoY and represents 28% of revenue, with a target of 40%+ by 2026. BeaconOS is also white-labeled to 3PLs generating $2.1M ARR. The process kicked off in Aug 2023 with a Q1 2024 targeted signing/close. Implied EV of ~$310M based on 9.2x LTM EBITDA. Platform acquisition opportunity in a highly fragmented Southeast LTL market.
- deal_context (confidence=0.95): company=Lighthouse Logistics Group, sector=transportation_logistics, subsector=last_mile_delivery
- <details><summary>⚠ extraction warnings</summary>

  - EV of ~$310M is inferred: total sources of $322.5M less estimated transaction fees (~$12M); the CIM shows 9.2x LTM EBITDA as the implied multiple — $33.7M × 9.2 = ~$310M used as ev_proposed_usd.
  - Revenue CAGR (3yr) of ~13.8% is computed from 2020 ($148.2M) to LTM Sep 2023 ($218.3M) over approximately 3 years; not explicitly stated in document.
  - Geography tagged as southeast_us (primary operating footprint); company also has Mid-Atlantic presence but Southeast is the dominant region and HQ location.
  - Subsector 'last_mile_delivery' used as closest existing value; core business is regional LTL freight — see taxonomy_proposals for gap flagged.

  </details>

### `Marketing Materials/Project_Beacon_Teaser_Sep2023.pdf` → `doc_project_beacon_002` (teaser)
- Title: PROJECT BEACON — Executive Summary Teaser | Lighthouse Logistics Group
- Date: 2023-09-01
- Summary: William Blair-distributed sell-side teaser for Project Beacon, Lighthouse Logistics Group — a technology-enabled regional LTL and final-mile freight provider headquartered in Charlotte, NC, operating 14 terminals across the Southeast and Mid-Atlantic U.S. LTM revenue of $218M and LTM Adj. EBITDA of $33.7M (15.5% margin). Seller is asking ~$310M (9.2x LTM EBITDA). Key investment highlights include proprietary BeaconOS route optimization technology, a rapidly growing e-commerce/final-mile segment (41% YoY, 28% of revenue), a fragmented regional LTL market opportunity, and a diversified revenue base with counter-cyclical healthcare exposure. Process launched September 2023 through William Blair.
- deal_context (confidence=0.92): company=Lighthouse Logistics Group, sector=transportation_logistics, subsector=last_mile_delivery
- <details><summary>⚠ extraction warnings</summary>

  - Subsector is ambiguous: Lighthouse is primarily a regional LTL carrier (closer to freight_logistics) but the teaser heavily emphasizes the final-mile/e-commerce growth vector. Selected last_mile_delivery as the subsector to reflect the forward-looking mix shift highlighted in the investment thesis, but freight_logistics is a plausible alternative. See taxonomy_proposals.
  - Geography set to southeast_us based on primary operating footprint (SE/Mid-Atlantic); Mid-Atlantic overlap is notable but Southeast appears primary given HQ in Charlotte, NC and market sizing language.
  - Revenue CAGR 3yr not explicitly stated; only YoY +17% revenue growth and 3-year healthcare segment CAGR of 24% are provided — revenue_cagr_3yr left null.
  - Process date is September 2023 — exact day not specified; defaulting to 2023-09-01.

  </details>

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- subsector: proposed=`regional_ltl_freight` (used `last_mile_delivery`, confidence=0.72)
  - rationale: Lighthouse Logistics is primarily a regional LTL carrier with a growing final-mile practice. 'last_mile_delivery' captures the final-mile segment but misses the core LTL business. A 'regional_ltl_freight' subsector under transportation_logistics would be more precise. 'freight_logistics' at the subsector level is not available under transportation_logistics in the current taxonomy, so 'last_mile_delivery' is used as the closest fit given the prominent final-mile segment.
