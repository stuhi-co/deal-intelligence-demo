# Ingestion report — project_pegasus

Deal ID: `deal_project_pegasus_2021`
Company canonical: `Stride & Co.`
Sector / subsector: `consumer_apparel` / `direct_to_consumer_brands`
Geography: `west_us`
Deal type: `platform`
Voted with 2 qualifying docs at confidence >= 0.9 (out of 2 tagged).

## Triage

### primary (2)
- `Marketing Materials/Project_Pegasus_CIM_Sept2021.pdf`
- `Marketing Materials/Project_Pegasus_Teaser_Sept2021.pdf`

### format_duplicate (2)
- `Marketing Materials/Project_Pegasus_CIM_Sept2021.pptx` — PDF preferred over DOCX/PPTX twin
- `Marketing Materials/Project_Pegasus_Teaser_Sept2021.pptx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Marketing Materials/Project_Pegasus_CIM_Sept2021.pdf` → `doc_project_pegasus_001` (cim)
- Title: Project Pegasus — Stride & Co. Confidential Information Memorandum
- Date: 2021-09-01
- Summary: Houlihan Lokey sell-side CIM for Stride & Co. ("Project Pegasus"), a purpose-driven premium DTC activewear brand founded in 2016 and headquartered in Los Angeles, CA. The Company offers performance apparel made from sustainably-sourced and recycled materials, complemented by the Stride Studio™ subscription membership (62K members, $21.7M ARR, 115% NRR). LTM Q2'21 revenue of $78M (+32% YoY) and Adj. EBITDA of $6.5M (8.3% margin). Asking EV of ~$130M (20x LTM EBITDA / 1.7x LTM Revenue). Management projects revenue growing to $235M and EBITDA to $54M by FY2025 driven by Studio membership expansion, men's line ramp, and international growth. Management team owns 71% of the company on a fully diluted basis. IOIs due October 8, 2021.
- deal_context (confidence=0.95): company=Stride & Co., sector=consumer_apparel, subsector=direct_to_consumer_brands
- <details><summary>⚠ extraction warnings</summary>

  - Revenue CAGR estimated from FY2018 ($28M) to LTM Q2'21 ($78.4M) over approximately 3 years (~41% CAGR); not explicitly stated in document.
  - Geography tagged as west_us based on Los Angeles HQ; the Company also operates in UK and Canada but the primary business and headquarters are US West Coast.
  - Deal type tagged as 'platform' based on CIM framing ('platform investment') and investment highlights language; no explicit acquirer type or add-on strategy stated in this document.
  - Founder transition thesis theme applied given management owns 71% and the Company is initiating a sale process, implying a liquidity/transition event for founding team.

  </details>

### `Marketing Materials/Project_Pegasus_Teaser_Sept2021.pdf` → `doc_project_pegasus_002` (teaser)
- Title: Project Pegasus — Executive Teaser
- Date: 2021-09-01
- Summary: Sell-side teaser prepared by Houlihan Lokey (exclusive advisor) for Stride & Co. ("Pegasus"), a Los Angeles-based premium DTC activewear brand founded in 2016. The Company offers performance apparel made from sustainably-sourced/recycled materials and has built a digital-first community anchored by the Stride Studio™ subscription membership (~62K members, $29/mo, $21.7M ARR). LTM revenue of $78M (+32% YoY) with $6.5M Adj. EBITDA (8.3% margin). Asking EV of ~$130M (~20x LTM EBITDA / 1.7x LTM Revenue). Key investment highlights include high-velocity DTC brand, differentiated sustainable product, capital-light outsourced manufacturing model, durable recurring revenue from Studio membership, international whitespace, and a founder-led management team owning 71% of the business. Management projects revenue growing to ~$235M by FY2025E with EBITDA margins expanding to ~13.9% by FY2022E.
- deal_context (confidence=0.93): company=Stride & Co., sector=consumer_apparel, subsector=direct_to_consumer_brands
- <details><summary>⚠ extraction warnings</summary>

  - LTM Q2'21 financials ($78.4M revenue / $6.5M EBITDA) treated as actuals per document labeling; FY2021E and beyond are management projections not independently verified by Houlihan Lokey.
  - FY2022E–FY2025E revenue figures ($122M–$235M) and EBITDA margin projections are from the chart and partial table only — FY2023E–FY2025E EBITDA dollar amounts not explicitly stated in text and are excluded.
  - Revenue CAGR (3yr) not directly stated; implied ~40% CAGR FY2018–FY2020 from actuals but not tagged given LTM-to-projected inconsistency.
  - Geography tagged as west_us (HQ: Los Angeles, CA) though the Company also sells in UK and Canada — national or international would be more accurate for revenue footprint, but HQ-based tagging applied per taxonomy.
  - Asking EV of ~$130M described as approximate ('~'); EV/EBITDA multiple of ~20x computed from stated figures.

  </details>

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- thesis_theme: proposed=`dtc_community_flywheel` (used `recurring_revenue`, confidence=0.72)
  - rationale: Stride's Stride Studio membership creates a community-driven subscription flywheel that goes beyond simple recurring revenue — it drives higher LTV, lower CAC, and brand defensibility. The existing taxonomy does not capture this DTC community/membership dynamic precisely.
- geography: proposed=`international` (used `west_us`, confidence=0.75)
  - rationale: Stride & Co. is HQ'd in Los Angeles (west_us) but actively sells in US, Canada, and UK. The existing taxonomy has no 'international' or 'multi-geography' option. west_us was used for HQ location; a broader geography tag would be more representative of the commercial footprint.
