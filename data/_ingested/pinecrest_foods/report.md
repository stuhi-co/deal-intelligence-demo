# Ingestion report — pinecrest_foods

Deal ID: `deal_pinecrest_foods_2022`
Company canonical: `Pinecrest Specialty Foods`
Sector / subsector: `consumer_products` / `packaged_food`
Geography: `national`
Deal type: `platform`
Voted with 6 qualifying docs at confidence >= 0.9 (out of 12 tagged).

## Triage

### primary (12)
- `Board Materials/Board_Package_Q1_2026.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2021.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2022.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2023.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2024.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2025.pdf` [hint: board_package]
- `Financial Reporting/Financial_Supplement_Q1_2026.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2021.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2022.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2023.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2024.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2025.xlsx` [hint: quarterly_financials]

### format_duplicate (6)
- `Board Materials/Board_Package_Q1_2026.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2021.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2022.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2023.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2024.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2025.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Board Materials/Board_Package_Q1_2026.pdf` → `doc_pinecrest_foods_001` (board_package)
- Title: Pinecrest Specialty Foods — Q1 2026 Board of Directors Package
- Date: 2026-05-08
- Summary: Final board package for Pinecrest Specialty Foods (Fund III portfolio company) covering Q1 2026 performance ahead of an imminent transaction close. Q1 2026 revenue was $151.3M (+11.4% YoY) and EBITDA was $20.4M (13.5% margin), both ahead of budget. LTM EBITDA stands at $75.1M vs. $37.7M at entry, reflecting significant growth. The company was transformed from a commodity frozen food brand into a premium Better-for-You (BFY) platform. Net leverage improved from 7.2x at entry to 4.6x. HSR cleared, financing confirmed, and buyer handover completed. Fund III gross MOIC estimated at ~2.2x. This is explicitly noted as the final board package as a portfolio company.
- deal_context (confidence=0.92): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - returns_extract.moic of 2.2x is labeled 'estimated' in the document — treated as near-final/realized given all closing conditions are satisfied and this is the final board package; flagged for human review.
  - exit_type inferred as strategic_sale based on buyer handover language and HSR clearance; not explicitly stated as a strategic vs. financial buyer sale.
  - geography set to west_us based on HQ address (San Francisco, CA) for Atlas Crossing; Pinecrest's own operational geography may be broader/national given 6 manufacturing facilities.
  - LTM revenue not explicitly stated; only Q1 2026 single-quarter revenue ($151.3M) and LTM EBITDA ($75.1M) are provided. revenue_ltm_usd left null.
  - entry_ev_usd and exit_ev_usd not disclosed in this document.

  </details>

### `Board Materials/Board_Package_Q4_2021.pdf` → `doc_pinecrest_foods_002` (board_package)
- Title: Pinecrest Specialty Foods — Q4 2021 Board of Directors Package
- Date: 2022-02-06
- Summary: Q4 2021 board package for Pinecrest Specialty Foods (Atlas Crossing Partners Fund III). Company delivered Q4 2021 revenue of $83.4M and EBITDA of $10.4M (12.5% margin), beating budget by 3.1% and 5.1% respectively. LTM EBITDA of $36.9M vs. entry baseline of $37.7M; net leverage improved to 6.8x from entry 7.2x. Key highlights include Albertsons national program signed (2,200 incremental stores), Harvest Kitchen acquisition LOI signed with close target Q2 2022, ERP rollout underway, and BFY reformulation in progress. Primary risk is input cost inflation (+22% YoY), with ~60% passed through pricing. Q1 2022 revenue outlook of $83.5M.
- deal_context (confidence=0.92): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Prior Year Quarter and YoY columns in the financial table are blank — no comparable period data available to compute revenue CAGR or YoY growth.
  - LTM revenue not explicitly stated; only Q4 2021 quarterly revenue ($83.4M) and LTM EBITDA ($36.9M) are provided.
  - EV and entry multiple not disclosed in this document; net leverage and LTM EBITDA at entry are referenced but not a full capital structure breakdown.

  </details>

### `Board Materials/Board_Package_Q4_2022.pdf` → `doc_pinecrest_foods_003` (board_package)
- Title: Pinecrest Specialty Foods — Q4 2022 Board of Directors Package
- Date: 2023-02-06
- Summary: Q4 2022 board package for Pinecrest Specialty Foods (Atlas Crossing Partners Fund III). Q4 revenue of $102.7M (+23.1% YoY) and EBITDA of $13.1M (12.7% margin) both came in ahead of budget. LTM EBITDA reached $45.5M vs. $37.7M at entry; net leverage declined to 6.5x from 7.2x at entry. National retail distribution expanded to 56K points (+47% since entry), driven by Kroger, Meijer, and Publix wins. Harvest Kitchen integration is in progress with Day-1 complete. Key risks include input cost inflation (partially hedged via forward contracts) and category competition from Lean Cuisine and Amy's Kitchen in the better-for-you segment. Q1 2023 revenue expected at ~$102.6M, with evaluation of Coastal Provisions bolt-on underway.
- deal_context (confidence=0.92): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue not explicitly stated; only Q4 2022 quarterly revenue ($102.7M) and LTM EBITDA ($45.5M) are provided. revenue_ltm_usd left null.
  - Retail Distribution Points KPI shows 49.9K in table but 56K referenced in executive summary and strategic initiatives — likely executive summary figure (56K) reflects cumulative as of board date vs. table KPI of 49.9K at quarter-end; both noted.
  - Q1 2023 outlook revenue of $102.6M is a forward projection and has not been included in period_actuals.

  </details>

### `Board Materials/Board_Package_Q4_2023.pdf` → `doc_pinecrest_foods_004` (board_package)
- Title: Pinecrest Specialty Foods — Q4 2023 Board of Directors Package
- Date: 2024-02-06
- Summary: Q4 2023 board package for Pinecrest Specialty Foods (Atlas Crossing Partners Fund III). Q4 2023 revenue of $122.3M and EBITDA of $15.9M (13.0% margin), both ahead of budget. LTM EBITDA of $54.8M vs. entry baseline of $37.7M. Net leverage improved to 6.1x from entry 7.2x. Key strategic updates include Coastal Provisions integration (Day-1 IMO established), better-for-you (BFY) SKU expansion ahead of target at 31.2% (vs. 18% at entry), and IC-approved exit preparation targeting a sell-side process in Q4 2025 with Houlihan Lokey engagement targeted for Q1 2024. Q1 2024 revenue expected at $122.1M.
- deal_context (confidence=0.92): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue not explicitly stated; only Q4 2023 quarterly revenue ($122.3M) and LTM EBITDA ($54.8M) are provided. revenue_ltm_usd left null.
  - BFY % of SKUs reported as 31.2% in the KPI table but the Strategic Initiatives section states 'BFY at 38% of SKUs — ahead of 35% target' — possible timing/methodology discrepancy within the document; KPI table value used for period_actuals.
  - Q1 2024 outlook revenue of $122.1M noted but not tagged as an actual; excluded from period_actuals.

  </details>

### `Board Materials/Board_Package_Q4_2024.pdf` → `doc_pinecrest_foods_005` (board_package)
- Title: Pinecrest Specialty Foods — Q4 2024 Board of Directors Package
- Date: 2025-02-06
- Summary: Q4 2024 board package for Pinecrest Specialty Foods (Atlas Crossing Partners Fund III). Q4 2024 revenue of $136.1M and EBITDA of $18.0M (13.2% margin), both ahead of budget. LTM EBITDA of $64.1M, net leverage of 5.2x (down from entry 7.2x). BFY SKU mix reached 36% (entry: 18%) against a 42% target. Strategic initiatives are exit-focused: Houlihan Lokey engaged, CIM in progress, management equity refresh completed. Q1 2025 IOIs targeted. Document signals active exit process underway.
- deal_context (confidence=0.92): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Q1 2025 outlook mentions 'CIM distribution Q3 2024' and 'Management presentations Q4 2024' — these appear to be historical milestones referenced in the outlook section, possibly a copy/paste inconsistency in the source document.
  - LTM revenue is not explicitly stated; only Q4 2024 quarterly revenue ($136.1M) and LTM EBITDA ($64.1M) are disclosed. LTM revenue left null.
  - Geography tagged as west_us based on company HQ inferred from Atlas Crossing Partners' San Francisco address; Pinecrest's own operating footprint geography is not explicitly stated.
  - Gross profit and EBIT figures are for Q4 only, not LTM, and have not been mapped to period_actuals as they are not revenue/EBITDA primary metrics.

  </details>

### `Board Materials/Board_Package_Q4_2025.pdf` → `doc_pinecrest_foods_006` (board_package)
- Title: Pinecrest Specialty Foods — Q4 2025 Board of Directors Package
- Date: 2026-02-06
- Summary: Q4 2025 board package for Pinecrest Specialty Foods (Atlas Crossing Partners Fund III). Company delivered Q4 2025 revenue of $151.5M (+11.3% YoY) and EBITDA of $20.4M (13.4% margin), 5.7% ahead of budget. LTM EBITDA stands at $72.7M vs. entry baseline of $37.7M, with net leverage de-levered from 7.2x at entry to 4.7x. The company is actively in an exit process with 5 first-round bids received and 2 strategic buyers shortlisted for final round. Operational KPIs show strong progress: retail distribution points at 70.3K (+85% from entry baseline of 38K) and Better-for-You SKU mix at 40.8% vs. 18% at entry. Close targeted Q1 2026.
- deal_context (confidence=0.92): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Next Quarter Outlook section contains apparent date inconsistencies: references 'Final-round bids target Q3 2025' and 'Definitive agreement Q4 2025' which are in the past relative to the board meeting date of February 6, 2026 — likely copy-paste errors from an earlier draft.
  - Q4 2025 revenue of $151.5M is a single-quarter figure; LTM revenue not explicitly stated (only LTM EBITDA of $72.7M is provided). revenue_ltm_usd left null.
  - Entry EV not explicitly stated; ev_proposed_usd left null. Net leverage at entry was 7.2x on $37.7M EBITDA, implying an approximate entry debt figure but insufficient to derive entry EV without equity component.

  </details>

### `Financial Reporting/Financial_Supplement_Q1_2026.xlsx` → `doc_pinecrest_foods_007` (quarterly_financials)
- Title: Pinecrest Specialty Foods — Quarterly Income Statement / Financial Supplement Q1 2026
- Date: 2026-03-31
- Summary: Q1 2026 financial supplement for Pinecrest Specialty Foods, a held portfolio company in the specialty/packaged food space. The workbook covers four sheets: (1) Income Statement — Q1 2026 actual revenue of $151.3M, EBITDA of $20.4M (13.48% margin), beating budget on both top and bottom line; (2) KPI Dashboard — LTM revenue of $556.3M, LTM EBITDA of $75.1M (13.5% margin), significant improvement vs. entry baseline across distribution points, better-for-you SKU mix, and net leverage down from 7.2x to 4.6x; (3) Balance Sheet Snapshot — total assets $308.3M, total debt $359.5M, net debt $345.5M; (4) Covenant Compliance — all four covenants passing with comfortable headroom (net leverage 4.6x vs. 8.0x covenant, interest coverage 2.74x vs. 1.75x minimum).
- deal_context (confidence=0.88): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Prior-year quarter COGS and SG&A are marked 'N/A — Pre-acq.' — company was acquired between Q1 2025 and Q1 2026; YoY margin comparisons are not available for line items below gross profit.
  - LTM revenue ($556.3M) is substantially higher than Q1 annualized ($605M), suggesting the LTM figure blends pre- and post-acquisition periods; used the KPI Dashboard LTM figures for structured payload as they are explicitly labeled.
  - EBITDA margin % on KPI dashboard shows 13.5% (LTM) vs. 13.48% on the income statement (Q1 only) — both captured appropriately.
  - Net debt computed as Total Debt ($359.5M) minus Cash ($14M) = $345.5M, consistent with KPI Dashboard figure.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2021.xlsx` → `doc_pinecrest_foods_008` (quarterly_financials)
- Title: Pinecrest Specialty Foods — Quarterly Income Statement & Financial Supplement Q4 2021
- Date: 2021-12-31
- Summary: Q4 2021 financial supplement for Pinecrest Specialty Foods covering the income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q4 2021 revenue was $83.4M vs. $80.9M budget (+$2.5M), with EBITDA of $10.4M (12.47% margin) beating budget by $0.5M. LTM revenue was $295.2M and LTM EBITDA was $36.9M (12.5% margin). Net leverage of 6.8x is within the ≤8.0x covenant. All four financial covenants passed with meaningful headroom. Prior-year comparisons are unavailable as the company was pre-acquisition in Q4 2020. Retail distribution points grew from 38K at entry to 43.1K, and better-for-you SKU mix improved from 18% to 21.6%.
- deal_context (confidence=0.82): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Prior-year quarter (Q4 2020) comparisons are unavailable — company was pre-acquisition; YoY growth rates cannot be computed.
  - LTM revenue of $295.2M is below the entry baseline of $306.5M, suggesting revenue underperformance vs. underwriting.
  - Annual LTM row emitted with quarter=null to capture LTM figures from the KPI Dashboard sheet; Q4 standalone row uses quarter=4.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2022.xlsx` → `doc_pinecrest_foods_009` (quarterly_financials)
- Title: Pinecrest Specialty Foods — Quarterly Income Statement & Financial Supplement Q4 2022
- Date: 2022-12-31
- Summary: Q4 2022 financial supplement for Pinecrest Specialty Foods, covering the quarterly income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q4 2022 revenue was $102.7M (vs. $99.6M budget, +$3.1M favorable), EBITDA was $13.1M at 12.76% margin. LTM revenue was $358.3M and LTM EBITDA was $45.5M (12.7% margin). Net leverage stood at 6.5x vs. an 8.0x covenant cap. All four debt covenants were passed with comfortable headroom. Retail distribution points grew to 49.9K from an entry baseline of 38K, and Better-for-You SKU mix rose to 26.4% from 18% at entry.
- deal_context (confidence=0.85): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Prior Year Quarter figures for COGS, SG&A, EBIT, Interest Expense, and Pre-Tax Income are marked 'N/A — Pre-acq.' indicating the company was not yet owned in Q4 2021; YoY comparisons are only available at the revenue and gross profit level.
  - LTM revenue of $358.3M and LTM EBITDA of $45.5M are sourced from the KPI Dashboard sheet; these represent trailing twelve months ending Q4 2022.
  - Balance sheet shows negative equity of -$102M, consistent with a highly leveraged LBO structure.
  - No explicit acquisition date or entry EV is disclosed in this document.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2023.xlsx` → `doc_pinecrest_foods_010` (quarterly_financials)
- Title: Pinecrest Specialty Foods — Quarterly Income Statement & Financial Supplement Q4 2023
- Date: 2023-12-31
- Summary: Q4 2023 financial supplement for Pinecrest Specialty Foods, covering the quarterly income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Revenue of $122.3M in Q4 2023 beat budget by $3.6M and grew $19.6M YoY vs. prior year quarter. Q4 EBITDA of $15.9M (13.0% margin) came in $0.8M above budget. LTM revenue of $421.5M and LTM EBITDA of $54.8M (13.0% margin). Net leverage of 6.1x vs. an 8.0x covenant, with all four covenants passing comfortably. The company has expanded from 4 to 6 manufacturing facilities and grown retail distribution points from 38K to 56.7K since entry.
- deal_context (confidence=0.82): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Prior year quarter (Q4 2022) COGS, SG&A, and below-the-line items are marked 'N/A — Pre-acq.' and could not be extracted — company was apparently acquired during 2022 and pre-acquisition comparables are unavailable.
  - LTM Revenue figure of $421.5385M taken directly from KPI Dashboard; this is an LTM (trailing 12-month) figure, not a single-quarter figure — emitted as an annual FY2023 LTM row with quarter=null.
  - EBITDA Margin % in KPI Dashboard is expressed as a whole-number percentage (13%) rather than a decimal; converted to 0.13 for structured payload.
  - Negative equity (-$108M) noted as a potential going-concern signal but all covenants are currently passing with meaningful headroom.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2024.xlsx` → `doc_pinecrest_foods_011` (quarterly_financials)
- Title: Pinecrest Specialty Foods — Quarterly Income Statement & Financial Supplement Q4 2024
- Date: 2024-12-31
- Summary: Q4 2024 financial supplement for Pinecrest Specialty Foods, covering the quarterly income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q4 2024 revenue was $136.1M (vs. $132M budget, +$4.1M favorable; $122.3M prior year quarter). Q4 EBITDA was $18.0M at a 13.2% margin, beating budget by $0.9M. LTM revenue was $485.6M and LTM EBITDA was $64.1M (13.2% margin). Net leverage stood at 5.2x, down from 7.2x at entry. All four covenants passed with meaningful headroom. Retail distribution points grew to 63.5K from an entry baseline of 38K, and manufacturing facilities expanded from 4 to 6. Better-for-you SKU mix increased from 18% to 36%.
- deal_context (confidence=0.85): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Prior year quarter (Q4 2023) revenue of $122.3M is available, but COGS, SG&A, and other line items are labeled 'N/A — Pre-acq.' indicating the company was acquired and pre-acquisition comparables are not restated.
  - LTM revenue ($485.6M) and LTM EBITDA ($64.1M) are sourced from the KPI Dashboard sheet and represent rolling twelve months through Q4 2024; an annual period_actuals row has been emitted for this LTM figure.
  - Exact fiscal year-end date assumed as December 31, 2024; document does not explicitly state the fiscal year-end date.
  - Net debt of $336.5M implies cash of $14.0M against total debt of $350.5M, consistent with the balance sheet.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2025.xlsx` → `doc_pinecrest_foods_012` (quarterly_financials)
- Title: Pinecrest Specialty Foods — Quarterly Income Statement & Financial Supplement Q4 2025
- Date: 2025-12-31
- Summary: Q4 2025 financial supplement for Pinecrest Specialty Foods covering the quarterly income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q4 2025 revenue was $151.5M vs. budget of $147M (+$4.5M favorable). EBITDA was $20.4M at a 13.47% margin, beating budget of $19.3M. LTM revenue stands at $542.5M and LTM EBITDA at $72.7M (13.4% margin). All four debt covenants are passing with comfortable headroom — net leverage of 4.7x vs. ≤8.0x covenant. Key operating KPIs show significant improvement vs. entry: retail distribution points up 85% to 70.3K, better-for-you SKU mix up to 40.8% from 18%, and manufacturing facilities expanded from 4 to 6.
- deal_context (confidence=0.85): company=Pinecrest Specialty Foods, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Prior year quarter COGS and SG&A are not available (labeled 'N/A — Pre-acq.'), indicating this is a post-acquisition portfolio company and pre-acquisition detailed P&L is unavailable
  - LTM Revenue of $542.5M and LTM EBITDA of $72.7M are from the KPI Dashboard sheet; these are LTM figures not strictly Q4-quarter-only figures
  - Q4 2025 date inferred as end of Q4 2025 (2025-12-31); no explicit date stamp found in the document
  - EBITDA Margin % shown as decimal in Income Statement (0.1347) and as percentage in KPI Dashboard (13.4%) — treated consistently as ~13.4-13.47%

  </details>

## Resolver disagreements

### geography
- Chosen: `national` (plurality 4/6)
- Voters for chosen: ['Board Materials/Board_Package_Q4_2021.pdf', 'Board Materials/Board_Package_Q4_2022.pdf', 'Board Materials/Board_Package_Q4_2023.pdf', 'Board Materials/Board_Package_Q4_2025.pdf']
- Dissent `west_us`: ['Board Materials/Board_Package_Q1_2026.pdf', 'Board Materials/Board_Package_Q4_2024.pdf']

### financials.revenue_ltm_usd
- Chosen: `556296300.0` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Financial Reporting/Financial_Supplement_Q1_2026.xlsx']
- Dissent `421538500.0`: ['Financial Reporting/Financial_Supplement_Q4_2023.xlsx']
- Dissent `358267700.0`: ['Financial Reporting/Financial_Supplement_Q4_2022.xlsx']
- Dissent `295200000.0`: ['Financial Reporting/Financial_Supplement_Q4_2021.xlsx']

### financials.ebitda_ltm_usd
- Chosen: `75100000.0` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf']
- Dissent `54800000.0`: ['Board Materials/Board_Package_Q4_2023.pdf', 'Financial Reporting/Financial_Supplement_Q4_2023.xlsx']
- Dissent `45500000.0`: ['Board Materials/Board_Package_Q4_2022.pdf', 'Financial Reporting/Financial_Supplement_Q4_2022.xlsx']
- Dissent `36900000.0`: ['Board Materials/Board_Package_Q4_2021.pdf', 'Financial Reporting/Financial_Supplement_Q4_2021.xlsx']
