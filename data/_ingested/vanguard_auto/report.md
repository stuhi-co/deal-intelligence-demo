# Ingestion report — vanguard_auto

Deal ID: `deal_vanguard_auto_2021`
Company canonical: `Vanguard Auto Parts`
Sector / subsector: `consumer_products` / `automotive_aftermarket`
Geography: `national`
Deal type: `platform`
Voted with 7 qualifying docs at confidence >= 0.9 (out of 14 tagged).

## Triage

### primary (14)
- `Board Materials/Board_Package_Q1_2026.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2020.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2021.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2022.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2023.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2024.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2025.pdf` [hint: board_package]
- `Financial Reporting/Financial_Supplement_Q1_2026.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2020.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2021.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2022.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2023.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2024.xlsx` [hint: quarterly_financials]
- `Financial Reporting/Financial_Supplement_Q4_2025.xlsx` [hint: quarterly_financials]

### format_duplicate (7)
- `Board Materials/Board_Package_Q1_2026.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2020.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2021.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2022.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2023.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2024.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2025.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Board Materials/Board_Package_Q1_2026.pdf` → `doc_vanguard_auto_001` (board_package)
- Title: Vanguard Auto Parts — Q1 2026 Board of Directors Package
- Date: 2026-05-08
- Summary: Final board package for Vanguard Auto Parts (Atlas Crossing Partners Fund III) covering Q1 2026 performance. Company delivered $289.8M revenue (+10.1% YoY) and $30.4M EBITDA (10.5% margin), beating budget by ~3%. LTM EBITDA reached $121.7M vs. $52.7M at entry, with net leverage compressed from 6.8x to 4.0x. HSR clearance received and transaction on track to close. Fund III gross MOIC estimated ~2.4x. This is noted as Vanguard's final board meeting as an Atlas Crossing portfolio company.
- deal_context (confidence=0.95): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - returns_extract.moic of 2.4x is labeled 'estimated' in the document (Fund III gross MOIC estimated ~2.4x) — not yet a fully realized/final figure; transaction close was still pending as of board meeting date.
  - LTM revenue not explicitly stated; only Q1 2026 quarterly revenue ($289.8M) provided — ebitda_ltm_usd ($121.7M) is explicitly stated in the financial table.
  - Close target listed as 'Q1 2026' in the Strategic Initiatives table, but board meeting is dated May 8, 2026 (Q2 2026); Next Quarter Outlook references 'Q1/Q2 2026' — likely a typographic error in the original document.

  </details>

### `Board Materials/Board_Package_Q4_2020.pdf` → `doc_vanguard_auto_002` (board_package)
- Title: Vanguard Auto Parts — Q4 2020 Board of Directors Package
- Date: 2021-02-06
- Summary: Q4 2020 board package for Vanguard Auto Parts, a portfolio company of Atlas Crossing Partners Fund III. Revenue of $147.0M and EBITDA of $12.4M (8.4% margin) beat budget by 3.1% and 6.0%, respectively. LTM EBITDA of $52.7M unchanged from entry; net leverage at 6.7x. Key initiatives include ERP/NetSuite rollout (Phase 1 live), e-commerce portal build (launch target Q3 2021), SKU rationalization (28,000 SKUs flagged, $18M working capital release expected), and active bolt-on scan of Detroit Auto Supply. Primary risks include COVID-related supply chain disruption and integration pace.
- deal_context (confidence=0.92): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - Prior year quarter figures and YoY comparisons are not populated in the source document — left null.
  - LTM revenue not explicitly stated; LTM EBITDA of $52.7M is provided and matches entry baseline.
  - Q1 2021 revenue outlook of $149.5M is a forward projection and has not been included in period_actuals.

  </details>

### `Board Materials/Board_Package_Q4_2021.pdf` → `doc_vanguard_auto_003` (board_package)
- Title: Vanguard Auto Parts — Q4 2021 Board of Directors Package
- Date: 2022-02-06
- Summary: Q4 2021 board package for Vanguard Auto Parts (Atlas Crossing Partners Fund III portfolio company). Q4 2021 revenue of $164.0M (+11.6% YoY, +3.1% vs. budget) and EBITDA of $14.4M (8.8% margin, +16.1% YoY). FY2021 EBITDA grew 22% vs. entry LTM, driven by SKU rationalization ($6.2M annualized savings), pricing discipline, and volume recovery. LTM EBITDA of $56.8M vs. entry of $52.7M. Net leverage of 6.2x (down from entry 6.8x). Key strategic initiatives include a launched e-commerce portal (12.5% of revenue), completed SKU rationalization, LOI signed for Detroit Auto acquisition (close targeted Q1 2022), and private label expansion underway. Q1 2022 revenue guidance of $176.7M.
- deal_context (confidence=0.92): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - LTM EBITDA of $56.8M is provided directly but corresponding LTM revenue is not stated; revenue_ltm_usd left null.
  - FY2021 full-year revenue is not explicitly stated; only Q4 2021 quarterly revenue ($164.0M) is available. Annual period_actual row populated for EBITDA (LTM) only.
  - EBITDA margin for the LTM/FY2021 annual row cannot be computed without LTM revenue; ebitda_margin left null for that row.

  </details>

### `Board Materials/Board_Package_Q4_2022.pdf` → `doc_vanguard_auto_004` (board_package)
- Title: Vanguard Auto Parts — Q4 2022 Board of Directors Package
- Date: 2023-02-06
- Summary: Q4 2022 board package for Vanguard Auto Parts (Atlas Crossing Partners Fund III portfolio company). The company delivered Q4 revenue of $206.1M (+25.7% YoY) and EBITDA of $19.0M (9.2% margin), beating budget by 3.1% and 5.6% respectively. LTM EBITDA stands at $71.3M vs. $52.7M at entry. Key milestones include: e-commerce reaching 20% of revenue, private label launch with 12 SKUs at 34% reorder rate, and the acquisition of Southeast Parts Network (Atlanta, GA). Net leverage of 6.3x is declining from 6.8x at entry on strong FCF. Q1 2023 revenue guided at $209.0M.
- deal_context (confidence=0.95): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - Q4 2021 EBITDA margin not explicitly stated; only EBITDA dollar ($14.4M) and revenue ($164.0M) for prior year quarter are provided — margin not calculated to avoid introducing derived values.
  - LTM revenue not explicitly stated in the document; only LTM EBITDA ($71.3M) is given.
  - E-commerce % of Revenue in the KPI table shows 16.2% for 'Current Quarter' while the Executive Summary states 20% — possible discrepancy between intra-quarter progress and period-end figure; both noted.

  </details>

### `Board Materials/Board_Package_Q4_2023.pdf` → `doc_vanguard_auto_005` (board_package)
- Title: Vanguard Auto Parts — Q4 2023 Board of Directors Package
- Date: 2024-02-06
- Summary: Q4 2023 board package for Vanguard Auto Parts (Atlas Crossing Partners Fund III portfolio company). The company delivered Q4 2023 revenue of $227.1M and EBITDA of $21.8M (9.6% margin), beating budget by 3.1% on revenue and 5.3% on EBITDA, with 10.2% YoY revenue growth. LTM EBITDA of $86.3M (vs. entry LTM of $52.7M) and net leverage of 5.1x (down from entry 6.8x) signal strong deleveraging. Key strategic updates include: completed Southeast integration with $4.8M annualized synergies, mobile app launch (22% of e-commerce orders), private label expansion (38 SKUs, 6.2% of revenue), and LOI signed for Southwest Auto Depot (bolt-on #3, close targeted Q3 2024). Exit preparation IC review flagged for Q1 2024.
- deal_context (confidence=0.92): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - LTM EBITDA of $86.3M is explicitly stated but LTM revenue is not disclosed; revenue_ltm_usd left null.
  - Q4 2023 prior year EBITDA of $19.0M and revenue of $206.1M are provided as comparison figures but no full FY 2022 or FY 2023 annual rollup table is present — only a single quarterly period_actuals row emitted.
  - Gross profit ($56.1M) and gross margin (24.7%) are Q4 actuals only; not surfaced in structured payload as no LTM equivalents are available.
  - Exit preparation IC review noted for Q1 2024 — deal may be transitioning to exit phase; monitor subsequent documents.

  </details>

### `Board Materials/Board_Package_Q4_2024.pdf` → `doc_vanguard_auto_006` (board_package)
- Title: Vanguard Auto Parts — Q4 2024 Board of Directors Package
- Date: 2025-02-06
- Summary: Q4 2024 board package for Vanguard Auto Parts (Atlas Crossing Partners Fund III). Company delivered Q4 2024 revenue of $259.7M and EBITDA of $26.0M (10.0% margin), beating budget by 3.1% on revenue and 5.3% on EBITDA. LTM EBITDA of $101.1M vs. entry baseline of $52.7M reflects significant earnings growth. Net leverage declined to 4.9x from entry of 6.8x. IC has formally approved exit preparation; Houlihan Lokey shortlisted as sell-side banker targeting H2 2026 exit. Key initiatives include Southwest acquisition integration (Day-1 complete), e-commerce growth (23.5% of revenue vs. 8.0% at entry), and private label expansion (52 SKUs, 8.5% of revenue). Q1 2025 revenue outlook of $263.2M.
- deal_context (confidence=0.95): company=Vanguard Auto Parts, sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue not explicitly stated; only Q4 2024 quarterly revenue ($259.7M) and LTM EBITDA ($101.1M) are disclosed. revenue_ltm_usd left null.
  - The second period_actuals row represents the LTM EBITDA figure ($101.1M) presented in the financial table — quarter set to null to indicate a trailing/annual rollup figure; year assigned 2024 as the LTM period end.
  - EBITDA margin for LTM period cannot be computed without LTM revenue; left null.
  - Geography tagged as west_us based on HQ; national may be more accurate given multi-region operations — see taxonomy_proposals.
  - Exit preparation IC approval noted; H2 2026 exit target with Houlihan Lokey as sell-side banker. This is a held portfolio company actively preparing for exit.
  - Q1 2025 revenue outlook of $263.2M is forward-looking guidance, not a realized figure — not included in period_actuals.

  </details>

### `Board Materials/Board_Package_Q4_2025.pdf` → `doc_vanguard_auto_007` (board_package)
- Title: Vanguard Auto Parts — Q4 2025 Board of Directors Package
- Date: 2026-02-06
- Summary: Q4 2025 board package for Vanguard Auto Parts (codename: vanguard_auto), a portfolio company of Atlas Crossing Partners Fund III. The company delivered Q4 2025 revenue of $285.9M and EBITDA of $29.7M (10.4% margin), 3.1% ahead of budget and +10.1% YoY on revenue. LTM EBITDA stands at $117.9M, up from $52.7M at entry. Net leverage has improved from 6.8x at entry to 4.1x. E-commerce reached 28% of revenue, an industry-leading milestone. The company is actively in an exit process: CIM distributed, first-round bids received, two buyers shortlisted for final round, with a definitive agreement targeted Q4 2025/Q1 2026 and close expected Q1 2026. Private label at 10.5% of revenue, tracking toward a 12% target at close. Q1 2026 revenue outlook is $289.8M.
- deal_context (confidence=0.92): company=Vanguard Auto Parts, sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - Q4 2025 revenue figure ($285.9M) is a single-quarter figure; LTM revenue not explicitly stated in the document — LTM EBITDA of $117.9M is provided but LTM revenue is not, so revenue_ltm_usd left null.
  - The 'E-commerce % of Revenue' KPI shows 27.1% in the table but 28% is cited in both the Executive Summary and Strategic Initiatives section — minor internal inconsistency; 27.1% is the precise Q4 figure while 28% appears to be a rounded/milestone figure.
  - Next Quarter Outlook section references 'Final-round bids Q3 2025' and 'Definitive agreement target Q4 2025' which appear to be historical references or typos given the document date is February 2026; flagged as possible copy-paste artifact.
  - deal_type tagged as 'platform' based on context (Fund III portfolio company in active exit process); not explicitly labeled in the document.
  - customer_concentration risk flag added cautiously given automotive aftermarket distribution; document does not explicitly discuss customer concentration but the B2B distribution model warrants the flag.

  </details>

### `Financial Reporting/Financial_Supplement_Q1_2026.xlsx` → `doc_vanguard_auto_008` (quarterly_financials)
- Title: Vanguard Auto Parts — Quarterly Income Statement & Financial Supplement Q1 2026
- Date: 2026-03-31
- Summary: Q1 2026 quarterly financial supplement for Vanguard Auto Parts covering the income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q1 2026 revenue was $289.8M (+$26.6M YoY vs. $263.2M prior year quarter), EBITDA was $30.4M at a 10.49% margin — beating budget by $1.5M. LTM revenue stands at ~$1.16B and LTM EBITDA at $121.7M (10.5% margin). Net leverage is 4.0x vs. a 7.5x covenant cap, with all covenants passing comfortably. KPI highlights include e-commerce rising to 28% of revenue (vs. 8% at entry), active SKU count at 248K, and warehouse locations expanded to 19 from 12 at entry.
- deal_context (confidence=0.88): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - Prior year quarter COGS, SG&A, EBIT, and below-the-line items are marked 'N/A — Pre-acq.' and thus unavailable for YoY comparison on those line items.
  - LTM revenue ($1,159.0M) and LTM EBITDA ($121.7M) extracted from KPI Dashboard sheet; these are LTM figures, not Q1-only.
  - Date set to 2026-03-31 (Q1 2026 quarter-end) as no explicit date appears in the document; inferred from period label.
  - Negative total equity (-$127.9M) flagged as a balance sheet risk — likely reflects goodwill/intangible step-up from acquisition financing.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2020.xlsx` → `doc_vanguard_auto_009` (quarterly_financials)
- Title: Vanguard Auto Parts — Quarterly Income Statement & Financial Supplement Q4 2020
- Date: 2020-12-31
- Summary: Q4 2020 quarterly financial supplement for Vanguard Auto Parts, covering the income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q4 2020 actual revenue was $147M vs. $142.6M budget (+$4.4M favorable). EBITDA came in at $12.4M (8.44% margin) vs. $11.7M budget. LTM revenue was $627.4M and LTM EBITDA was $52.7M (8.4% margin). Net leverage stands at 6.7x vs. a 7.5x covenant ceiling. All four covenants are passing. Prior-year quarter comparisons are unavailable as the period predates the acquisition. Key operational KPIs show e-commerce at 8.9% of revenue, 12 warehouse locations, and a 94.4% fill rate — all largely in line with entry baseline.
- deal_context (confidence=0.88): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - Prior Year Quarter figures are unavailable for all income statement line items — company notes 'N/A — Pre-acq.' indicating the acquisition closed during or just before Q4 2020; YoY comparisons cannot be computed.
  - LTM revenue of $627.4M is slightly below entry baseline of $634.9M, suggesting modest underperformance vs. acquisition underwrite on top-line.
  - Annual Capex is annualized from quarterly figure ($3.4M x 4 = $13.6M) per the Covenant Compliance sheet; actual full-year figure may differ.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2021.xlsx` → `doc_vanguard_auto_010` (quarterly_financials)
- Title: Vanguard Auto Parts — Quarterly Income Statement & Financial Supplement Q4 2021
- Date: 2021-12-31
- Summary: Q4 2021 financial supplement for Vanguard Auto Parts, covering the quarterly income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q4 2021 actual revenue was $164M vs. budget of $159M, with EBITDA of $14.4M (8.78% margin), beating budget by $0.7M. LTM revenue was $645.5M and LTM EBITDA was $56.8M (8.8% margin). Net leverage of 6.2x is within the 7.5x covenant limit. All four covenants are passing with comfortable headroom. E-commerce as a percentage of revenue reached 12.5%, up from an 8.0% entry baseline, tracking toward a 28% target.
- deal_context (confidence=0.88): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue of $645.5M is presented as a decimal in the source ($645.4545M) — rounded to $645,454,500 for absolute USD conversion.
  - Prior year quarter COGS, SG&A, and EBIT are marked 'N/A — Pre-acq.' and therefore excluded from structured extraction.
  - Annual LTM figures emitted as a separate period_actuals row with quarter=null to distinguish from the Q4 single-quarter row.
  - Negative total equity (-$149.9M) noted as a balance sheet flag consistent with a leveraged buyout structure.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2022.xlsx` → `doc_vanguard_auto_011` (quarterly_financials)
- Title: Vanguard Auto Parts — Quarterly Income Statement & Financial Supplement Q4 2022
- Date: 2022-12-31
- Summary: Q4 2022 quarterly financial supplement for Vanguard Auto Parts, covering the income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q4 2022 revenue was $206.1M vs. budget of $199.9M (+$6.2M), with EBITDA of $19.0M (9.2% margin) beating budget by $1.0M. LTM revenue was $775M and LTM EBITDA was $71.3M (9.2% margin). All four debt covenants passed with comfortable headroom, including net leverage of 6.3x vs. a 7.5x covenant cap. E-commerce penetration reached 16.2% of revenue, up from an 8.0% entry baseline. The company operates 17 warehouse locations vs. 12 at entry.
- deal_context (confidence=0.82): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - Prior year quarter revenue ($164M) is available for YoY comparison but full prior-year income statement detail is marked 'N/A — Pre-acq.' indicating the company was acquired during or before 2021 and pre-acquisition figures are not restated.
  - The second period_actuals row (annual LTM) uses LTM figures from the KPI Dashboard sheet; 'quarter' is set to null to represent the LTM/full-year rollup as distinct from the single Q4 row.
  - Total Debt of $469.7M vs. Net Debt of $447.7M implies ~$22M cash, consistent with the balance sheet's $22M cash balance.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2023.xlsx` → `doc_vanguard_auto_012` (quarterly_financials)
- Title: Vanguard Auto Parts — Quarterly Income Statement & Financial Supplement Q4 2023
- Date: 2023-12-31
- Summary: Q4 2023 financial supplement for Vanguard Auto Parts covering income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q4 2023 revenue of $227.1M beat budget by $6.8M (+3.1%); EBITDA of $21.8M at 9.6% margin, also ahead of budget. LTM revenue of $899.0M and LTM EBITDA of $86.3M (9.6% margin). Net leverage of 5.1x, well within the 7.5x covenant. E-commerce has grown to 19.8% of revenue vs. 8.0% at entry. All four covenants pass with comfortable headroom. Goodwill and intangibles have grown materially since entry ($157M vs. $85M), reflecting add-on activity. Negative equity of $(142.4)M reflects leveraged buyout capital structure.
- deal_context (confidence=0.88): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - Prior Year Quarter COGS, SG&A, EBIT, Interest Expense, and Pre-Tax Income are labeled 'N/A — Pre-acq.' — prior-year comparisons are unavailable for most line items below gross profit.
  - LTM revenue ($898.96M) derived from KPI Dashboard sheet; Q4-only revenue ($227.1M) from Income Statement sheet — both captured as separate period_actuals rows (Q4 standalone and LTM annual rollup).
  - Balance sheet shows goodwill & intangibles grew from $85M at entry to $157M at Q4 2023, suggesting add-on acquisitions post-close; integration_risk flag considered but omitted as no explicit integration issues are cited.
  - Negative equity (-$142.4M) is structural to leveraged buyout and does not indicate financial distress given strong covenant headroom.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2024.xlsx` → `doc_vanguard_auto_013` (quarterly_financials)
- Title: Vanguard Auto Parts — Quarterly Income Statement & Financial Supplement Q4 2024
- Date: 2024-12-31
- Summary: Q4 2024 financial supplement for Vanguard Auto Parts, a held automotive aftermarket portfolio company. The workbook covers four sheets: Income Statement (Q4 actuals vs. budget and prior year), KPI Dashboard (e-commerce mix, SKU count, warehouse footprint, LTM revenue/EBITDA), Balance Sheet Snapshot (vs. entry), and Covenant Compliance. Q4 2024 revenue was $259.7M (+14.4% YoY vs. $227.1M prior year quarter) and EBITDA was $26.0M (10.0% margin), beating budget by $1.3M. LTM revenue reached $1,011M and LTM EBITDA was $101.1M (10.0% margin). Net leverage stood at 4.9x, well within the 7.5x covenant. All four covenants pass with meaningful headroom. Key operational KPIs show significant improvement vs. entry: e-commerce mix up from 8% to 23.5%, SKU count up ~28%, and warehouse locations expanded from 12 to 19.
- deal_context (confidence=0.88): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - Prior year quarter COGS and SG&A are labeled 'N/A — Pre-acq.' indicating company was not yet owned in Q4 2023; YoY comparisons are partial (revenue and gross profit only).
  - LTM annual row emitted using KPI Dashboard LTM figures ($1,011M revenue, $101.1M EBITDA); these are trailing twelve months ending Q4 2024, so quarter is set to null.
  - EBITDA margin on LTM row expressed as 10.0% (0.10) per KPI Dashboard; Q4 standalone margin is 10.01% (0.1001) per Income Statement.
  - Net debt of $499.1M implies cash of $22M against total debt of $521.1M, consistent with Balance Sheet. Entry net debt was ~$358M.

  </details>

### `Financial Reporting/Financial_Supplement_Q4_2025.xlsx` → `doc_vanguard_auto_014` (quarterly_financials)
- Title: Vanguard Auto Parts — Quarterly Income Statement & Financial Supplement Q4 2025
- Date: 2025-12-31
- Summary: Q4 2025 quarterly financial supplement for Vanguard Auto Parts, covering an income statement, KPI dashboard, balance sheet snapshot, and covenant compliance. Q4 2025 revenue was $285.9M with EBITDA of $29.7M (10.4% margin), beating budget by $1.5M on EBITDA. LTM revenue was $1,133.7M and LTM EBITDA was $117.9M (10.4% LTM margin). Net leverage stands at 4.1x, well within the 7.5x covenant. All four covenants are passing with substantial headroom. Operational KPIs show strong progress vs. entry: e-commerce mix grew from 8% to 27.1%, warehouse footprint expanded from 12 to 19 locations, and fill rate improved to 97.6%.
- deal_context (confidence=0.85): company=Vanguard Auto Parts, sector=consumer_products, subsector=automotive_aftermarket
- <details><summary>⚠ extraction warnings</summary>

  - Prior year quarter COGS and SG&A are marked 'N/A — Pre-acq.' and are unavailable for comparison.
  - LTM revenue of $1,133.6538M converted to $1,133,653,800 USD from the KPI Dashboard sheet.
  - EBITDA margin % (LTM) displayed as 10.4 in KPI dashboard (interpreted as 10.4%, stored as 0.104 decimal).
  - Q4 2025 date inferred as fiscal year-end 2025 (December 31, 2025) from 'Q4 2025' label; no explicit cover date in document.
  - Goodwill & intangibles increased from $85M at entry to $185M, suggesting add-on acquisitions completed post-platform entry.

  </details>

## Resolver disagreements

### sector
- Chosen: `consumer_products` (plurality 5/7)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf', 'Board Materials/Board_Package_Q4_2020.pdf', 'Board Materials/Board_Package_Q4_2021.pdf', 'Board Materials/Board_Package_Q4_2022.pdf', 'Board Materials/Board_Package_Q4_2023.pdf']
- Dissent `industrial_distribution`: ['Board Materials/Board_Package_Q4_2024.pdf', 'Board Materials/Board_Package_Q4_2025.pdf']

### subsector
- Chosen: `automotive_aftermarket` (plurality 5/7)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf', 'Board Materials/Board_Package_Q4_2020.pdf', 'Board Materials/Board_Package_Q4_2021.pdf', 'Board Materials/Board_Package_Q4_2022.pdf', 'Board Materials/Board_Package_Q4_2023.pdf']
- Dissent `specialty_distribution`: ['Board Materials/Board_Package_Q4_2024.pdf', 'Board Materials/Board_Package_Q4_2025.pdf']

### geography
- Chosen: `national` (plurality 6/7)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf', 'Board Materials/Board_Package_Q4_2020.pdf', 'Board Materials/Board_Package_Q4_2021.pdf', 'Board Materials/Board_Package_Q4_2022.pdf', 'Board Materials/Board_Package_Q4_2023.pdf', 'Board Materials/Board_Package_Q4_2025.pdf']
- Dissent `west_us`: ['Board Materials/Board_Package_Q4_2024.pdf']

### financials.revenue_ltm_usd
- Chosen: `1159047600.0` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Financial Reporting/Financial_Supplement_Q1_2026.xlsx']
- Dissent `898958300.0`: ['Financial Reporting/Financial_Supplement_Q4_2023.xlsx']
- Dissent `775000000.0`: ['Financial Reporting/Financial_Supplement_Q4_2022.xlsx']
- Dissent `645454500.0`: ['Financial Reporting/Financial_Supplement_Q4_2021.xlsx']
- Dissent `627381000.0`: ['Financial Reporting/Financial_Supplement_Q4_2020.xlsx']

### financials.ebitda_ltm_usd
- Chosen: `121700000.0` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf']
- Dissent `86300000.0`: ['Board Materials/Board_Package_Q4_2023.pdf', 'Financial Reporting/Financial_Supplement_Q4_2023.xlsx']
- Dissent `71300000.0`: ['Board Materials/Board_Package_Q4_2022.pdf', 'Financial Reporting/Financial_Supplement_Q4_2022.xlsx']
- Dissent `56800000.0`: ['Board Materials/Board_Package_Q4_2021.pdf', 'Financial Reporting/Financial_Supplement_Q4_2021.xlsx']
- Dissent `52700000.0`: ['Board Materials/Board_Package_Q4_2020.pdf', 'Financial Reporting/Financial_Supplement_Q4_2020.xlsx']

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- geography: proposed=`west_us` (used `west_us`, confidence=0.65)
  - rationale: Atlas Crossing Partners is headquartered at 2 Embarcadero Center, San Francisco, CA; however the company operates nationally with a Southwest acquisition underway. 'west_us' was selected as closest given HQ location, but 'national' may be more appropriate given multi-region warehouse footprint (19 locations) and Southwest expansion.
- subsector: proposed=`automotive_aftermarket_distribution` (used `specialty_distribution`, confidence=0.75)
  - rationale: Vanguard Auto Parts is an automotive aftermarket parts distributor. The taxonomy has 'automotive_aftermarket' under consumer_products but no automotive aftermarket subsector under industrial_distribution. 'specialty_distribution' is the closest fit under industrial_distribution.
