# Ingestion report — project_ember

Deal ID: `deal_project_ember_2024`
Company canonical: `Cascade Outdoor Brands`
Sector / subsector: `consumer_products` / `outdoor_hardgoods`
Geography: `national`
Deal type: `platform`
Voted with 2 qualifying docs at confidence >= 0.9 (out of 2 tagged).

## Triage

### primary (2)
- `Marketing Materials/Project_Ember_CIM_Apr2024.pdf`
- `Marketing Materials/Project_Ember_Teaser_Apr2024.pdf`

### format_duplicate (2)
- `Marketing Materials/Project_Ember_CIM_Apr2024.pptx` — PDF preferred over DOCX/PPTX twin
- `Marketing Materials/Project_Ember_Teaser_Apr2024.pptx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Marketing Materials/Project_Ember_CIM_Apr2024.pdf` → `doc_project_ember_001` (cim)
- Title: Project Ember – Cascade Outdoor Brands Confidential Information Memorandum
- Date: 2024-04-01
- Summary: Harris Williams sell-side CIM for Cascade Outdoor Brands ("Project Ember"), a Denver, CO-based premium designer and manufacturer of technical outdoor hardgoods (tents, shelters, ultralight cookware) sold under two owned brands — Ridgeline (mid-market, $95 ASP) and Summit Series (premium, $285 ASP). LTM Apr 2024 revenue of $112M and Adj. EBITDA of $14.0M (12.5% margin). DTC e-commerce represents 44% of revenue, up from 29% three years ago. The Company has 58K paid loyalty members, 3 issued patents, international revenue in 22 countries, and an OEM/licensing royalty stream ($3.2M ARR). Indicative EV implied at ~$175M (12.5x LTM EBITDA). Sale process initiated April 2024; closing targeted Q3 2024.
- deal_context (confidence=0.95): company=Cascade Outdoor Brands, sector=consumer_products, subsector=outdoor_hardgoods
- <details><summary>⚠ extraction warnings</summary>

  - EV of ~$175M is inferred from total sources ($165.5M) and EV/LTM EBITDA multiple of 12.5x × $14.0M EBITDA; the CIM does not state a single explicit enterprise value figure.
  - Revenue CAGR of ~10.7% is computed from 2021 ($82.5M) to LTM Apr 2024 ($112M) over approximately 3 years; not stated explicitly in the document.
  - subsector 'outdoor_hardgoods' is confirmed in the consumer_products taxonomy and is a valid entry.

  </details>

### `Marketing Materials/Project_Ember_Teaser_Apr2024.pdf` → `doc_project_ember_002` (teaser)
- Title: Project Ember — Executive Summary Teaser: Cascade Outdoor Brands
- Date: 2024-04-01
- Summary: Harris Williams sell-side teaser for Cascade Outdoor Brands ("Project Ember"), a Denver, CO-based premium designer and manufacturer of technical outdoor hardgoods (tents, shelters, ultralight cookware) sold under two owned brands — Ridgeline (mid-market, $95 ASP) and Summit Series (premium, $285 ASP). The company was founded in 2009 by two former REI product managers and distributes through DTC e-commerce (44%), specialty outdoor retail (38%), and international distributors across 22 countries (18%). LTM Revenue of $112M and LTM Adj. EBITDA of $14M (12.5% margin). Asking price of ~$175M (12.5x LTM Adj. EBITDA). Key highlights include DTC-led margin expansion, proprietary AeroShield™ material innovation (3 patents), and strong international momentum (+34% YoY).
- deal_context (confidence=0.95): company=Cascade Outdoor Brands, sector=consumer_products, subsector=outdoor_hardgoods
- <details><summary>⚠ extraction warnings</summary>

  - Revenue CAGR (3-year) not explicitly stated; only YoY +14% growth rate provided.
  - Process date given as 'April 2024' — defaulted to 2024-04-01 as exact day not specified.
  - Deal type tagged as 'platform' by inference (full acquisition ask with no add-on or carve-out language); buyer type not confirmed in document.

  </details>

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- subsector: proposed=`outdoor_hardgoods` (used `outdoor_hardgoods`, confidence=0.99)
  - rationale: Cascade Outdoor Brands manufactures and sells technical outdoor hardgoods (tents, shelters, cookware). The taxonomy includes 'outdoor_hardgoods' under consumer_products, which is an exact fit.
- thesis_theme: proposed=`dtc_channel_shift` (used `margin_expansion`, confidence=0.75)
  - rationale: The document heavily emphasizes the shift from wholesale to DTC e-commerce as a core value creation driver (29%→44% revenue mix, 15pp gross margin advantage). 'margin_expansion' is the closest existing theme but doesn't fully capture the channel strategy angle.
