# Ingestion report — wholesum_foods_distribution

Deal ID: `deal_wholesum_foods_distribution_2022`
Company canonical: `Wholesum Foods Distribution, Inc.`
Sector / subsector: `consumer_products` / `food_distribution`
Geography: `national`
Deal type: `platform`
Voted with 8 qualifying docs at confidence >= 0.9 (out of 12 tagged).

## Triage

### primary (12)
- `Board Materials/Board_Package_Q1_2026.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2022.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2023.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2024.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2025.pdf` [hint: board_package]
- `Deal Materials/IC_Memo_Entry_2022-06.pdf`
- `Financial Reporting/Comps_Analysis_Entry_2022-06.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q1_2026.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2022.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2023.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2024.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2025.xlsx` [hint: quarterly_financials]

### format_duplicate (6)
- `Board Materials/Board_Package_Q1_2026.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2022.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2023.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2024.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2025.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Deal Materials/IC_Memo_Entry_2022-06.docx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Board Materials/Board_Package_Q1_2026.pdf` → `doc_wholesum_foods_distribution_001` (board_package)
- Title: Wholesum Foods Distribution, Inc. — Board of Directors Package Q1 2026
- Date: 2026-05-07
- Summary: Final board package for Wholesum Foods Distribution, Inc. (Fund III portfolio company) covering Q1 2026 performance. Company delivered $298.0M revenue and $39.5M EBITDA (13.3% margin), both ahead of budget. The document confirms this is the last board meeting as an Atlas Crossing portfolio company, with a transaction close expected April 30, 2026 (HSR cleared March 12). Management highlights LTM EBITDA of $153.2M vs. entry of $72.4M, net leverage reduced from 6.0x to 4.4x, private label penetration grown from 8% to 16.5%, and customer count grown from 3,500 to 5,310 across 17 distribution centers. Estimated exit returns: ~2.3x gross MOIC, ~18–19% gross IRR.
- deal_context (confidence=0.92): company=Wholesum Foods Distribution, sector=consumer_products, subsector=food_distribution
- <details><summary>⚠ extraction warnings</summary>

  - IRR stated as a range (18–19%); midpoint of 18.5% (0.185) used for returns_extract.irr.
  - MOIC stated as '~2.3x' (approximate); flagged as estimated, not a finalized realized figure — transaction had not yet closed as of board meeting date (April 30 close expected).
  - Holding period not explicitly stated; entry year cannot be precisely determined from this document alone (referenced as 'three-and-a-half year partnership').
  - Entry and exit EV not explicitly disclosed in this document; LTM EBITDA at entry ($72.4M) and current ($153.2M) are available but entry multiple is not stated.
  - Geography tagged as west_us based on Atlas Crossing HQ (San Francisco, CA); actual company operating geography may be national given 17 distribution centers — insufficient detail to confirm.

  </details>

### `Board Materials/Board_Package_Q4_2022.pdf` → `doc_wholesum_foods_distribution_002` (board_package)
- Title: Wholesum Foods Distribution, Inc. — Q4 2022 Board of Directors Package
- Date: 2023-02-09
- Summary: Q4 2022 board package for Wholesum Foods Distribution, Inc. (Atlas Crossing Partners Fund III portfolio company). Q4 2022 revenue was $171.0M and EBITDA was $18.9M (11.1% margin), both beating budget. LTM EBITDA was $71.7M with net leverage at 5.8x (down from entry 6.0x). Key updates include completion of ERP Phase 1 across all 12 DCs, a signed definitive agreement to acquire Crescent Bay Foods (expected to close February 2023, adding ~$36M annualized revenue), and progress on private label expansion (target: 18% of revenue by exit, currently 8.5%). FY2023 plan: $765M revenue and $87M EBITDA.
- deal_context (confidence=0.92): company=Wholesum Foods Distribution, sector=consumer_products, subsector=food_distribution
- <details><summary>⚠ extraction warnings</summary>

  - Prior year quarter financials are not provided (shown as '—'); YoY comparison unavailable.
  - LTM revenue is not explicitly stated; only LTM EBITDA ($71.7M) is shown. Revenue LTM left null.
  - Q4 2022 EBITDA margin (11.1%) used as the primary ebitda_margin in structured; note the LTM margin differs but is not calculable without LTM revenue.
  - Geography set to west_us based on HQ/meeting location; company operates 12 DCs whose geographic spread is not detailed — could be national.
  - A full FY2022 annual rollup row was emitted with only LTM EBITDA ($71.7M) populated, as the doc cites this figure explicitly; revenue and margin for the full year are not available.
  - H2 2022 combined figures ($334.0M revenue, $36.3M EBITDA) are noted in the executive summary but not broken out into separate period_actuals rows as they represent only the first two post-close quarters, not a standard reporting period.

  </details>

### `Board Materials/Board_Package_Q4_2023.pdf` → `doc_wholesum_foods_distribution_003` (board_package)
- Title: Wholesum Foods Distribution, Inc. — Q4 2023 Board of Directors Package
- Date: 2024-02-08
- Summary: Q4 2023 board package for Wholesum Foods Distribution, Inc. (Atlas Crossing Partners Fund III). Q4 revenue of $208.0M and EBITDA of $25.6M (12.3% margin) beat budget. Full-year FY2023 revenue was $785.0M and EBITDA $93.7M, 29% above entry LTM of $72.4M. Net leverage improved to 5.4x from entry 6.0x. Rio Grande Latino Foods acquisition closed January 9, 2024. Midwest Specialty Foods is under formal evaluation. Private label at 10.5% of revenue, ahead of plan. FY2024 plan calls for $880M revenue and $112M EBITDA.
- deal_context (confidence=0.92): company=Wholesum Foods Distribution, sector=consumer_products, subsector=food_distribution
- <details><summary>⚠ extraction warnings</summary>

  - ebitda_margin for FY2023 full year computed as 93.7M/785.0M = 11.94%; document does not state full-year margin explicitly
  - Q4 prior-year revenue ($171.0M) and EBITDA ($18.9M) noted in the variance table but not emitted as a separate period_actual since they are comparative figures only and not the primary reporting period of this document

  </details>

### `Board Materials/Board_Package_Q4_2024.pdf` → `doc_wholesum_foods_distribution_004` (board_package)
- Title: Wholesum Foods Distribution, Inc. — Q4 2024 Board of Directors Package
- Date: 2025-02-06
- Summary: Q4 2024 board package for Wholesum Foods Distribution, Inc. (Atlas Crossing Partners Fund III portfolio company). Q4 2024 revenue of $259.0M and EBITDA of $32.9M (12.7% margin). Full-year FY2024 revenue of $952.0M and EBITDA of $118.5M — 64% above entry LTM EBITDA of $72.4M. Net leverage declined to 4.9x vs. entry of 6.0x, 1.1 turns ahead of plan. IC has approved exit preparation process targeting a sell-side launch in Q2 2026 with Houlihan Lokey shortlisted. Private label at 13.0% of revenue (vs. 8.0% at entry), targeting 18% by exit. Customer count grown from 3,500 to 4,710. FY2025 plan: $1,085M revenue, $138M EBITDA.
- deal_context (confidence=0.92): company=Wholesum Foods Distribution, sector=consumer_products, subsector=food_distribution
- <details><summary>⚠ extraction warnings</summary>

  - FY2024 full-year EBITDA margin computed as $118.5M / $952.0M ≈ 12.45%; document only explicitly states the 12.7% Q4 margin figure. Annual margin stored as computed value.
  - Geography set to west_us based on HQ address (San Francisco, CA) inferred from board meeting location; company may operate nationally as a food distributor — national geography is plausible but not confirmed in this document.
  - Entry EV not explicitly stated in this document; entry LTM EBITDA of $72.4M and entry leverage of 6.0x are noted but no purchase price is disclosed.

  </details>

### `Board Materials/Board_Package_Q4_2025.pdf` → `doc_wholesum_foods_distribution_005` (board_package)
- Title: Wholesum Foods Distribution, Inc. — Q4 2025 Board of Directors Package
- Date: 2026-02-05
- Summary: Q4 2025 and full-year FY2025 board package for Wholesum Foods Distribution, Inc. (Atlas Crossing Partners Fund III). Q4 revenue of $309.0M and EBITDA of $40.9M (13.2% margin); FY2025 revenue of $1,118.0M and EBITDA of $145.5M — 101% above entry LTM EBITDA of $72.4M. Atlas Crossing signed a definitive agreement to sell Wholesum on January 29, 2026, valuing the company at ~$1.65B (~11.3x LTM EBITDA). Close expected Q2 2026 pending HSR clearance. Fund III gross MOIC estimated at 2.3x with gross IRR of 18–19%. Key operational milestones include customer growth from 3,500 to 5,240, DC footprint expansion from 12 to 17, and private label revenue penetration of 16% (nearing 18% exit target). Net leverage reduced from 6.0x at entry to 4.5x.
- deal_context (confidence=0.92): company=Wholesum Foods Distribution, sector=consumer_products, subsector=food_distribution
- <details><summary>⚠ extraction warnings</summary>

  - IRR returned as midpoint of stated range (18–19%); stored as 0.185 decimal.
  - Entry EV not explicitly stated in document; entry_ev_usd left null.
  - Holding period years not explicitly stated; left null.
  - Geography tagged as west_us based on HQ address (San Francisco, CA); company may operate nationally as a distributor — consider national if broader footprint is confirmed.
  - returns_extract populated from board package rather than a dedicated returns_summary/funds_flow doc — figures are estimates ('estimated') not yet realized at time of writing (close pending Q2 2026).

  </details>

### `Deal Materials/IC_Memo_Entry_2022-06.pdf` → `doc_wholesum_foods_distribution_006` (ic_memo)
- Title: Investment Committee Memorandum — Initial Investment Recommendation — Wholesum Foods Distribution, Inc.
- Date: 2022-06-14
- Summary: Atlas Crossing Partners Fund III IC entry memo recommending acquisition of a majority controlling interest in Wholesum Foods Distribution, Inc. at $710M enterprise value (9.8x LTM Adj. EBITDA of $72.4M). Wholesum is the largest US specialty foodservice distributor focused on Hispanic, Asian, and Mediterranean/Italian product lines, serving ~3,500 restaurant and retail customers from 12 DCs. Atlas Crossing is contributing $155M equity; the Gonzales family is rolling $125M (22%). Key thesis themes include market consolidation via bolt-on M&A, private-label margin expansion, tech modernization (NetSuite/WMS), and organic growth in high-growth ethnic food segments. Target 4-year hold with base case 3.4x MOIC / 35.8% gross IRR at a $1.22B exit EV.
- deal_context (confidence=0.95): company=Wholesum Foods Distribution, Inc., sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - FY2022 LTM revenue growth rate of 13.4–13.5% implies ~3-year CAGR from FY19 to FY22 LTM of approximately 8.9% — revenue_cagr_3yr not explicitly stated in doc, left null.
  - Returns sensitivity table shows base case 4-year hold; figures in underwriting_case_extract represent base case only. Downside (1.7x / 13.4% IRR) and upside (4.7x / 47.2% IRR) scenarios exist but are not separately captured in the extract.
  - Period actuals for FY22 LTM represent trailing twelve months as of memo date (June 2022), not a completed fiscal year — tagged as year 2022 annual row with this caveat.
  - Sector tagged as industrial_distribution (closest fit) but company is a foodservice distributor; taxonomy_proposals filed for both sector and subsector.

  </details>

### `Financial Reporting/Comps_Analysis_Entry_2022-06.xlsx` → `doc_wholesum_foods_distribution_007` (financial_model)
- Title: Wholesum Foods Distribution — Valuation Analysis (Entry IC Materials, June 2022)
- Date: 2022-06-10
- Summary: Comparables and valuation analysis workbook prepared as part of Atlas Crossing Partners Fund III entry IC materials for Wholesum Foods Distribution (June 2022). The workbook includes a public trading comps set (foodservice broadliners and specialty food distributors), precedent M&A transactions (2018–2022), and an entry valuation sensitivity table. Based on an LTM Adjusted EBITDA of $72.4M (per EY QofE) and a selected entry multiple of 9.8x, the implied entry EV is ~$710M. The selected multiple is positioned between mainstream broadliners (8–10x) and specialty/premium food distribution (11–14x), supported by Wholesum's specialty/ethnic positioning, 12%+ growth profile, and 21.8% gross margin.
- deal_context (confidence=0.9): company=Wholesum Foods Distribution, sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - Doc_type overridden from folder hint 'quarterly_financials' to 'financial_model': content is a comps/valuation analysis workbook (public comps, transaction comps, sensitivity table) prepared for entry IC materials, not a periodic financial reporting document.
  - Implied entry EV of ~$710M is derived from the sensitivity table ($72.4M × 9.8x = $709.52M, rounded to $710M in document text); populated in ev_proposed_usd.
  - LTM revenue for Wholesum not explicitly stated in the workbook; left null.
  - EBITDA margin for Wholesum not explicitly stated; gross margin of 21.8% is mentioned in commentary but is a gross margin, not EBITDA margin — left ebitda_margin null to avoid confusion.
  - Revenue 3Y CAGR of 12%+ is mentioned for Wholesum in qualitative commentary but not in a structured table; not populated as revenue_cagr_3yr due to uncertainty of precision.
  - Public comp EV/LTM EBITDA and EV/LTM revenue multiples columns are present but empty in the source document (formula columns not rendered); not extractable.

  </details>

### `Financial Reporting/Financial_Supplement_Q1_2026.xlsx` → `doc_wholesum_foods_distribution_008` (quarterly_financials)
- Title: Wholesum Foods Distribution — Quarterly Income Statement & Financial Supplement Q1 2026
- Date: 2026-03-31
- Summary: Q1 2026 quarterly financial supplement for Wholesum Foods Distribution, a held portfolio company (entry August 2022). The workbook covers four sheets: (1) Income Statement showing Q1 2026 actuals vs. budget and prior year — Revenue $298M, EBITDA $39.5M (13.3% margin), beating budget by $1.5M on EBITDA; (2) KPI Dashboard with LTM figures — Revenue $1,155.8M, EBITDA $153.2M (13.3% LTM margin), 5,310 customers across 17 distribution centers, net leverage of 4.4x vs. 6.0x at entry; (3) Balance Sheet Snapshot comparing current to entry (Aug 2022); and (4) Covenant Compliance showing all four covenants passing with material headroom. EBITDA margin has expanded from 10.9% at entry to 13.3% LTM, and net leverage has improved from 6.0x to 4.4x, reflecting meaningful operational progress since acquisition.
- deal_context (confidence=0.92): company=Wholesum Foods Distribution, sector=consumer_products, subsector=food_distribution
- <details><summary>⚠ extraction warnings</summary>

  - Prior year Q1 (Q1 2025) revenue of $250M and EBITDA of $31.8M are noted but labeled 'Pre-acq.' for most line items; only revenue and EBITDA are available for the prior year quarter and have been omitted from period_actuals as pre-acquisition figures may not be on a comparable basis.
  - EBITDA margin on KPI dashboard is expressed as a percentage (13.255%) rather than a decimal — converted to 0.13255 for structured payload.
  - LTM figures from KPI Dashboard used for revenue_ltm_usd and ebitda_ltm_usd; Q1 2026 single-quarter figures used for period_actuals.
  - Entry date of August 2022 noted in KPI Dashboard, confirming this is a held portfolio company.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2022.xlsx` → `doc_wholesum_foods_distribution_009` (quarterly_financials)
- Title: Wholesum Foods Distribution — Quarterly Income Statement & KPI Dashboard Q4 2022
- Date: 2022-12-31
- Summary: Q4 2022 financial supplement for Wholesum Foods Distribution, a food distribution portfolio company acquired in August 2022. The workbook presents a quarterly income statement (Q4 2022 actual vs. budget), a KPI dashboard comparing current metrics to entry assumptions, a balance sheet snapshot, and covenant compliance tracking. Q4 2022 revenue came in at $171M vs. $167M budget; EBITDA was $18.9M at an 11.1% margin, beating budget by $0.9M. LTM revenue is $648.7M and LTM EBITDA is $71.7M (11.1% margin). The company is tracking below its 18%+ EBITDA margin target and its private label penetration goal (8.5% actual vs. 18% target), but net leverage improved to 5.8x from 6.0x at entry. All four debt covenants are passing with meaningful headroom.
- deal_context (confidence=0.88): company=Wholesum Foods Distribution, sector=consumer_products, subsector=food_distribution
- <details><summary>⚠ extraction warnings</summary>

  - Prior Year Qtr figures are all listed as 'N/A — Pre-acq.' because the acquisition closed in August 2022; no prior-year quarterly comparisons are available.
  - EBITDA margin % in the KPI Dashboard is shown as '11.0526' — interpreted as a percentage (11.05%), not a decimal ratio. Stored as 0.1105 to align with schema convention.
  - LTM revenue ($648.7M) and LTM EBITDA ($71.7M) are from the KPI Dashboard; a single PeriodActual row is emitted for Q4 2022 quarterly actuals only. No full-year annual rollup is separately presented in this document.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2023.xlsx` → `doc_wholesum_foods_distribution_010` (quarterly_financials)
- Title: Wholesum Foods Distribution — Quarterly Income Statement & Financial Supplement Q4 2023
- Date: 2023-12-31
- Summary: Q4 2023 financial supplement for Wholesum Foods Distribution, a held portfolio company in food distribution. The workbook covers four sheets: (1) Income Statement showing Q4 2023 actuals vs. budget and prior year — revenue of $208M, EBITDA of $25.6M (12.3% margin), beating budget by $1.2M; (2) KPI Dashboard with LTM metrics (revenue $761.3M, EBITDA $93.7M, 12.3% LTM margin) vs. entry (Aug 2022) baselines, showing 700 net new customers and 2 new distribution centers since acquisition; (3) Balance Sheet snapshot comparing Q4 2023 to entry — total assets of $503.6M, net debt of $398M; (4) Covenant Compliance confirming all four covenants pass with comfortable headroom, including 5.4x net leverage vs. 7.5x covenant.
- deal_context (confidence=0.88): company=Wholesum Foods Distribution, sector=consumer_products, subsector=food_distribution
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue of $761.3125M from KPI Dashboard is an LTM figure ending Q4 2023; emitted as a FY 2023 annual row with quarter=null.
  - Prior Year Qtr EBITDA margin % not explicitly stated; margin computed from revenue ($171M) and EBITDA ($18.9M) is ~11.05% but not confirmed in doc, so left null.
  - Entry date explicitly stated as August 2022 in KPI Dashboard; deal appears to be a closed/held platform investment.
  - Revenue per customer and EBITDA per DC are operational KPIs; not mapped to structured payload fields — captured in growth_drivers/risks narrative.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2024.xlsx` → `doc_wholesum_foods_distribution_011` (quarterly_financials)
- Title: Wholesum Foods Distribution — Quarterly Income Statement & Financial Supplement Q4 2024
- Date: 2024-12-31
- Summary: Q4 2024 financial supplement for Wholesum Foods Distribution covering the income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q4 2024 revenue of $259M came in $5M ahead of budget with EBITDA of $32.9M (12.7% margin), also beating budget by $1.4M. On an LTM basis, revenue was $932.9M and EBITDA was $118.5M (12.7% margin). Since entry in August 2022, the business has added 5 distribution centers (12→17), grown its customer count by ~35% (3,500→4,710), and expanded EBITDA margin ~180 bps. Net leverage improved from 6.0x at entry to 4.9x, and all four debt covenants are in compliance with meaningful headroom.
- deal_context (confidence=0.88): company=Wholesum Foods Distribution, sector=consumer_products, subsector=food_distribution
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue ($932.9M) and EBITDA ($118.5M) are from the KPI Dashboard sheet and represent trailing twelve months, not a single quarter — emitted only in structured payload, not as a period_actual row to avoid confusion with Q4 standalone figures.
  - Prior year Q4 revenue ($208M) is available but prior year EBITDA is not broken out separately; no prior-year period_actual row emitted due to missing EBITDA data.
  - EBITDA margin shown as 12.7027% on KPI dashboard; stored as 0.127 (decimal). Gross margin of 20.2% also noted but EBITDA margin used as primary margin metric.
  - Entry date inferred as August 2022 from KPI dashboard 'Entry (Aug 2022)' column.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2025.xlsx` → `doc_wholesum_foods_distribution_012` (quarterly_financials)
- Title: Wholesum Foods Distribution — Quarterly Income Statement & Financial Supplement Q4 2025
- Date: 2025-12-31
- Summary: Q4 2025 quarterly financial supplement for Wholesum Foods Distribution, a portfolio company in food distribution. The workbook covers four sheets: (1) Income Statement showing Q4 2025 actual revenue of $309M, EBITDA of $40.9M (13.24% margin), favorably ahead of budget by $1.7M; (2) KPI Dashboard reporting LTM revenue of ~$1.099B, LTM EBITDA of $145.5M (13.24% margin), and strong growth vs. entry (Aug 2022) across customers, distribution centers, and EBITDA per DC; (3) Balance Sheet Snapshot comparing Q4 2025 vs. entry positions, showing net debt reduction of $27M to $389M; and (4) Covenant Compliance confirming all four covenants are passing with comfortable headroom, including net leverage at 4.5x vs. 7.5x covenant.
- deal_context (confidence=0.85): company=Wholesum Foods Distribution, sector=consumer_products, subsector=food_distribution
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue figure ($1,099.25M) is taken from the KPI Dashboard sheet; it is an LTM aggregate, not a single-quarter figure. A separate period_actuals row has been emitted for the LTM period with quarter=null.
  - Q4 2024 prior-year EBITDA of $32.9M is noted in the income statement but is pre-acquisition; not emitted as a period_actuals row due to pre-acq. flag on several line items.
  - EBITDA margin % in KPI Dashboard is expressed as 13.2362 (appears to be a percentage value, not decimal); converted to 0.1324 decimal for ebitda_margin fields.
  - Entry date of August 2022 noted in KPI Dashboard; deal appears to be a closed/held platform investment.

  </details>

## Resolver disagreements

### sector
- Chosen: `consumer_products` (plurality 6/7)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf', 'Board Materials/Board_Package_Q4_2022.pdf', 'Board Materials/Board_Package_Q4_2023.pdf', 'Board Materials/Board_Package_Q4_2024.pdf', 'Board Materials/Board_Package_Q4_2025.pdf', 'Financial Reporting/Financial_Supplement_Q1_2026.xlsx']
- Dissent `industrial_distribution`: ['Deal Materials/IC_Memo_Entry_2022-06.pdf']

### subsector
- Chosen: `food_distribution` (plurality 6/7)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf', 'Board Materials/Board_Package_Q4_2022.pdf', 'Board Materials/Board_Package_Q4_2023.pdf', 'Board Materials/Board_Package_Q4_2024.pdf', 'Board Materials/Board_Package_Q4_2025.pdf', 'Financial Reporting/Financial_Supplement_Q1_2026.xlsx']
- Dissent `specialty_distribution`: ['Deal Materials/IC_Memo_Entry_2022-06.pdf']

### geography
- Chosen: `national` (plurality 4/8; tied 4-way, broke tie by confidence sum)
- Voters for chosen: ['Board Materials/Board_Package_Q4_2023.pdf', 'Deal Materials/IC_Memo_Entry_2022-06.pdf', 'Financial Reporting/Comps_Analysis_Entry_2022-06.xlsx', 'Financial Reporting/Financial_Supplement_Q1_2026.xlsx']
- Dissent `west_us`: ['Board Materials/Board_Package_Q1_2026.pdf', 'Board Materials/Board_Package_Q4_2022.pdf', 'Board Materials/Board_Package_Q4_2024.pdf', 'Board Materials/Board_Package_Q4_2025.pdf']

### financials.revenue_ltm_usd
- Chosen: `1118000000.0` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Board Materials/Board_Package_Q4_2025.pdf']
- Dissent `785000000.0`: ['Board Materials/Board_Package_Q4_2023.pdf']
- Dissent `761312500.0`: ['Financial Reporting/Financial_Supplement_Q4_2023.xlsx']
- Dissent `648714300.0`: ['Financial Reporting/Financial_Supplement_Q4_2022.xlsx']
- Dissent `885000000.0`: ['Deal Materials/IC_Memo_Entry_2022-06.pdf']

### financials.ebitda_ltm_usd
- Chosen: `153200000.0` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf']
- Dissent `118500000.0`: ['Board Materials/Board_Package_Q4_2024.pdf', 'Financial Reporting/Financial_Supplement_Q4_2024.xlsx']
- Dissent `93700000.0`: ['Board Materials/Board_Package_Q4_2023.pdf', 'Financial Reporting/Financial_Supplement_Q4_2023.xlsx']
- Dissent `71700000.0`: ['Board Materials/Board_Package_Q4_2022.pdf', 'Financial Reporting/Financial_Supplement_Q4_2022.xlsx']
- Dissent `72400000.0`: ['Deal Materials/IC_Memo_Entry_2022-06.pdf', 'Financial Reporting/Comps_Analysis_Entry_2022-06.xlsx']

### financials.ebitda_margin
- Chosen: `0.133` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf']
- Dissent `0.082`: ['Deal Materials/IC_Memo_Entry_2022-06.pdf']

### financials.ev_proposed_usd
- Chosen: `1650000000.0` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Board Materials/Board_Package_Q4_2025.pdf']
- Dissent `710000000.0`: ['Deal Materials/IC_Memo_Entry_2022-06.pdf', 'Financial Reporting/Comps_Analysis_Entry_2022-06.xlsx']

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- subsector: proposed=`food_distribution` (used `food_distribution`, confidence=0.98)
  - rationale: Wholesum Foods Distribution is a food distribution business; food_distribution is listed under consumer_products in the taxonomy and is an exact fit.
- geography: proposed=`west_us` (used `west_us`, confidence=0.6)
  - rationale: Atlas Crossing Partners is headquartered in San Francisco, CA (2 Embarcadero Center); board meeting held there. However, distribution company with 12 DCs may be national in scope — insufficient detail to confirm. Defaulting to west_us given HQ and meeting location signal.
- geography: proposed=`national` (used `west_us`, confidence=0.65)
  - rationale: Wholesum Foods Distribution operates 17 distribution centers (up from 12 via bolt-ons) suggesting a multi-regional or national footprint, though HQ is in San Francisco. A 'national' geography classification would be more accurate for a food distributor of this scale ($952M revenue). Persisting west_us as the closest match based on HQ location.
- sector: proposed=`food_distribution` (used `industrial_distribution`, confidence=0.72)
  - rationale: Wholesum is a B2B specialty foodservice distributor. The taxonomy lacks a dedicated food_distribution sector; industrial_distribution with subsector specialty_distribution is the best available fit, but the company is meaningfully consumer/food-oriented rather than industrial.
- subsector: proposed=`foodservice_distribution` (used `specialty_distribution`, confidence=0.8)
  - rationale: Wholesum operates as a specialty foodservice distributor (ethnic/specialty foods to restaurants). The taxonomy's specialty_distribution under industrial_distribution is the closest fit, though foodservice_distribution would be more precise.
