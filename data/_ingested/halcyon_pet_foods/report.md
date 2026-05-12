# Ingestion report — Halcyon Pet Foods

Deal ID: `deal_halcyon_pet_foods_2017`
Company canonical: `Halcyon Pet Foods, Inc.`
Sector / subsector: `consumer_products` / `pet_food`
Geography: `national`
Deal type: `platform`
Voted with 4 qualifying docs at confidence >= 0.9 (out of 4 tagged).

## Triage

### primary (4)
- `Historical Performance/Comps_Analysis_Entry_2017-09.xlsx`
- `Historical Performance/Final_Returns_Summary_2023-03.xlsx`
- `Historical Performance/IC_Memo_Entry_2017-09.pdf`
- `Historical Performance/IC_Memo_Exit_2023-03.pdf`

### format_duplicate (2)
- `Historical Performance/IC_Memo_Entry_2017-09.docx` — PDF preferred over DOCX/PPTX twin
- `Historical Performance/IC_Memo_Exit_2023-03.docx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Historical Performance/Comps_Analysis_Entry_2017-09.xlsx` → `doc_halcyon_pet_foods_001` (financial_model)
- Title: Halcyon Pet Foods — Valuation Analysis: Entry Investment Committee Materials — September 2017
- Date: 2017-09-15
- Summary: Comps analysis and entry valuation workbook prepared by Atlas Crossing Partners Fund II deal team for the Halcyon Pet Foods entry IC in September 2017. The workbook includes a public comparable companies set (premium pet pure-plays: Blue Buffalo, Freshpet; diversified pet/consumer: Central Garden & Pet, Spectrum Brands, J.M. Smucker, TreeHouse Foods), a precedent M&A transaction set covering premium pet food deals from 2010–2017, and a valuation sensitivity table. LTM Adjusted EBITDA per EY QofE is $25.9M. The selected entry multiple is 11.0x, implying an enterprise value of approximately $285M. Public comps trade at 11.5–16.0x NTM EBITDA and 13.0–18.5x LTM EBITDA; the selected entry multiple represents a ~30% discount to public comps and ~20% discount to recent strategic transactions. The upside exit case assumes 14.0x.
- deal_context (confidence=0.92): company=Halcyon Pet Foods, sector=consumer_products, subsector=pet_food
- <details><summary>⚠ extraction warnings</summary>

  - Doc type hint was '(none)'; classified as 'financial_model' based on content (comps analysis / valuation sensitivity workbook for entry IC materials).
  - Implied EV at selected case ($25.9M × 11.0x = $284.9M) — the Summary sheet lists the cell as blank but the Valuation Sensitivity note confirms $285M; used $284.9M for precision.
  - EV/LTM and EV/NTM EBITDA multiples for individual public comps and transaction comps are blank in the workbook (formula cells not rendered); median/mean statistics rows are also blank.
  - No LTM revenue figure for Halcyon is disclosed in this workbook, so revenue_ltm_usd and revenue_cagr_3yr remain null.
  - Date set to 2017-09-15 based on trading data date disclosed in the Public Comps sheet header; filename suffix corroborates September 2017.

  </details>

### `Historical Performance/Final_Returns_Summary_2023-03.xlsx` → `doc_halcyon_pet_foods_002` (returns_summary)
- Title: Halcyon Pet Foods — Final Returns Summary
- Date: 2023-03-01
- Summary: Final returns summary for Atlas Crossing Partners Fund II's investment in Halcyon Pet Foods, a premium pet food platform acquired in September 2017 and exited via strategic sale to Cabrillo Holdings (Mars-affiliated) in April 2023. The deal produced a 3.5x gross MOIC and 28.4% gross IRR over a 5.6-year hold, representing the highest gross MOIC in Fund II. Value creation was driven by organic revenue growth, margin/mix improvement, multiple expansion (11.0x → 14.5x), and one bolt-on acquisition (Vesta Treats, Jun 2020). DTC channel revenue grew from 14.6% to 42.1% of total revenue. Realized outcomes fell between base and upside underwrite cases on most metrics, with DTC penetration and exit multiple exceeding the base case.
- deal_context (confidence=0.97): company=Halcyon Pet Foods, sector=consumer_products, subsector=pet_food
- <details><summary>⚠ extraction warnings</summary>

  - Holding period reported as 5.6 years; holding_period_years rounded to 6 (integer field). Exact figure is 5.6.
  - IRR extracted as gross IRR (28.4%); net IRR is 23.1% — only gross used in returns_extract per instructions on realized figures.
  - MOIC extracted as gross MOIC (3.5x); net MOIC is 2.8x — only gross used in returns_extract.
  - FY23 KPI row reflects partial year LTM through exit (Apr 14, 2023); excluded from period_actuals as it is not a full fiscal year.
  - Escrow release of $14M expected Oct 2024 is not yet realized; excluded from returns_extract.
  - Revenue CAGR 3yr not calculable from a clean 3-year window without additional context on fiscal year definitions; left null.

  </details>

### `Historical Performance/IC_Memo_Entry_2017-09.pdf` → `doc_halcyon_pet_foods_003` (ic_memo)
- Title: Investment Committee Memorandum — Initial Investment Recommendation: Halcyon Pet Foods, Inc.
- Date: 2017-09-18
- Summary: Atlas Crossing Partners Fund II entry IC memo recommending approval of the acquisition of Halcyon Pet Foods, Inc. (Boulder, CO), a premium/natural pet food maker, at an enterprise value of $285M (11.0x LTM Adj. EBITDA of $25.9M). Atlas Crossing commits $95M of equity alongside a $190M Antares Capital unitranche, with founder Dr. Marcus Reyes rolling over 12% of proceeds. The investment thesis centers on the premium pet food category's structural tailwinds (~9% CAGR), an underdeveloped DTC channel (14.6% → 35%+ target), gross margin expansion (~530bps), management gap-filling (CFO, COO, Head of DTC hires), and a bolt-on M&A path in adjacent premium categories. Base case projects a 5-year hold delivering 2.6x gross MOIC and ~22% gross IRR on a $648M exit EV at 12.0x. Key risks include customer concentration (PetSmart + Petco = 59% of revenue), founder dependency, private label encroachment, and commodity input volatility. IC approval is recommended subject to confirmatory diligence, final debt papers, and founder rollover documentation.
- deal_context (confidence=0.97): company=Halcyon Pet Foods, Inc., sector=consumer_products, subsector=pet_food
- <details><summary>⚠ extraction warnings</summary>

  - FY2017 is presented as an estimate (FY17E), not a confirmed actual; LTM Adj. EBITDA of $25.9M is used as the anchor for entry multiple. FY17E revenue of $132M treated as near-actual for structured payload given proximity to close.
  - year_5_exit EBITDA in underwriting_case_extract uses the base case exit EBITDA ($54M) per the returns sensitivity table, not the FY22B P&L line ($67M); the difference likely reflects timing and base-case conservatism vs. full-year projection.
  - Revenue CAGR 3yr computed over FY15A–FY17E (78→132M ≈ 30% CAGR); actual 3-year realized CAGR may differ given FY17 is estimated.
  - Downside and upside case returns figures extracted into key_quotes only; only base case populated in underwriting_case_extract per instructions.
  - period_actuals limited to FY15A and FY16A — the only confirmed historical actuals in the document; FY17E excluded as it is a projection.

  </details>

### `Historical Performance/IC_Memo_Exit_2023-03.pdf` → `doc_halcyon_pet_foods_004` (ic_memo)
- Title: Exit Recommendation — Halcyon Pet Foods, Inc. | Atlas Crossing Partners Fund II IC Memorandum
- Date: 2023-03-22
- Summary: Atlas Crossing Partners Fund II exit IC memo recommending sale of Halcyon Pet Foods, Inc. to Cabrillo Holdings (Mars-affiliated) for $890M enterprise value (14.5x LTM Adj. EBITDA of $61.4M). The all-cash stock purchase transaction is targeting an April 14, 2023 close. Fund II invested $104M in equity (initial $95M in Sep 2017 + $9M bolt-on for Vesta Treats in Jun 2020) and expects cumulative proceeds of $355M (including $21M Q3 2021 dividend recap), yielding 3.5x gross MOIC and 28.4% gross IRR on a ~5.5-year hold. Net MOIC is 2.8x and net IRR is 23.1%. Key value creation drivers include DTC channel build (subscriber count grew 6.5x), organic revenue growth (51% of equity value creation), multiple expansion from 11.0x to 14.5x (29%), and the Vesta Treats bolt-on (8%). Revenue grew from $132M to $328M and EBITDA from $25.9M to $61.4M over the hold period. The memo notes three competing final bids and recommends Cabrillo for highest bid, all-cash structure, and strategic synergies with Mars global distribution.
- deal_context (confidence=0.98): company=Halcyon Pet Foods, sector=consumer_products, subsector=pet_food
- <details><summary>⚠ extraction warnings</summary>

  - entry_ev_usd not explicitly stated in the document; entry multiple cited as 11.0x at the 2017 acquisition on $25.9M EBITDA implies ~$285M EV — not extracted as it is inferred rather than explicitly labeled as realized entry EV
  - holding_period_years set to 6 (rounded from 5.5-year stated hold) per schema integer type; document states '5.5-year hold' and '~28.4% (5.5-year hold)'
  - period_actuals populated for entry year (2017) and exit year (2022/2023 LTM) only — intermediate annual figures not available in this document
  - net MOIC 2.8x and net IRR 23.1% are after fees and carry; returns_extract captures gross figures (3.5x / 28.4%) per schema guidance to use realized/actual figures; net figures noted here for completeness

  </details>

## Resolver disagreements

### geography
- Chosen: `national` (plurality 2/3)
- Voters for chosen: ['Historical Performance/Final_Returns_Summary_2023-03.xlsx', 'Historical Performance/IC_Memo_Exit_2023-03.pdf']
- Dissent `west_us`: ['Historical Performance/IC_Memo_Entry_2017-09.pdf']

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- geography: proposed=`mountain_west_us` (used `west_us`, confidence=0.75)
  - rationale: Halcyon Pet Foods is headquartered in Boulder, CO, which is geographically in the Mountain West. The existing taxonomy does not have a mountain_west_us value; west_us is the closest available option.
