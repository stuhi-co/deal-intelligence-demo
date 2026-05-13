# Ingestion report — crestview_coffee

Deal ID: `deal_crestview_coffee_2019`
Company canonical: `Crestview Coffee Roasters`
Sector / subsector: `consumer_products` / `specialty_beverage`
Geography: `west_us`
Deal type: `platform`
Voted with 8 qualifying docs at confidence >= 0.9 (out of 9 tagged).

## Triage

### primary (9)
- `Board Materials/Board_Package_Q1_2026.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2019.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2020.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2021.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2022.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2023.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2024.pdf` [hint: board_package]
- `Board Materials/Board_Package_Q4_2025.pdf` [hint: board_package]
- `Deal Materials/IC_Memo_Entry_2019-04.pdf`

### format_duplicate (9)
- `Board Materials/Board_Package_Q1_2026.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2019.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2020.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2021.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2022.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2023.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2024.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Board Materials/Board_Package_Q4_2025.docx` [hint: board_package] — PDF preferred over DOCX/PPTX twin
- `Deal Materials/IC_Memo_Entry_2019-04.docx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Board Materials/Board_Package_Q1_2026.pdf` → `doc_crestview_coffee_001` (board_package)
- Title: Crestview Coffee Roasters — Q1 2026 Board of Directors Package
- Date: 2026-05-08
- Summary: Final board package for Crestview Coffee Roasters as an Atlas Crossing Partners Fund II portfolio company ahead of an imminent exit transaction. Q1 2026 revenue was $146.7M (+9.2% YoY) and EBITDA was $23.5M (16.0% margin), both ahead of budget by ~3–5%. HSR clearance was received with no second request and close was targeted for April 30, 2026. Key KPIs — 118K subscription customers and 44% DTC mix — hit exit targets. Fund II gross MOIC is estimated at ~2.8x. This is explicitly noted as the final Crestview board package.
- deal_context (confidence=0.92): company=Crestview Coffee Roasters, sector=consumer_products, subsector=specialty_beverage
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue not explicitly stated; only Q1 2026 quarterly revenue ($146.7M) and LTM EBITDA ($88.4M) are disclosed — LTM revenue left null.
  - MOIC of ~2.8x is described as 'estimated' / 'gross' and is presented in an outlook section, not as a finalized realized figure; populated in returns_extract given the transaction close was imminent (April 30, 2026) and all conditions were satisfied, but flagged as potentially still a projection.
  - Geography inferred as west_us based on San Francisco HQ address of sponsor; Crestview's own operating footprint geography is not specified.
  - Holding period years and entry/exit EVs not disclosed in this document.

  </details>

### `Board Materials/Board_Package_Q4_2019.pdf` → `doc_crestview_coffee_002` (board_package)
- Title: Crestview Coffee Roasters — Q4 2019 Board of Directors Package
- Date: 2020-02-06
- Summary: Q4 2019 board package for Crestview Coffee Roasters (Atlas Crossing Partners Fund II). Revenue of $77.2M and EBITDA of $10.6M (13.7% margin) came in 3.1% and 6.0% ahead of budget, respectively. LTM EBITDA of $37.7M vs. entry baseline of $36.5M; net leverage of 5.8x vs. entry 5.9x. DTC channel and subscription growth are primary strategic initiatives, alongside a Pacific Northwest bolt-on scan with 5 regional roasters under NDA (Cascade Roasting management meeting held January 2020). ERP/NetSuite rollout on track. Q1 2020 revenue guidance of $76.8M with Cascade Roasting LOI targeted.
- deal_context (confidence=0.92): company=Crestview Coffee Roasters, sector=consumer_products, subsector=specialty_beverage
- <details><summary>⚠ extraction warnings</summary>

  - Prior year quarter revenue and YoY growth metrics are blank in the source document; cannot populate YoY comparison.
  - LTM Revenue not explicitly stated; only Q4 2019 quarterly revenue ($77.2M) and LTM EBITDA ($37.7M) provided.
  - Geography tagged as west_us based on headquarters in San Francisco and Pacific Northwest operations focus; company may have national reach.

  </details>

### `Board Materials/Board_Package_Q4_2020.pdf` → `doc_crestview_coffee_003` (board_package)
- Title: Crestview Coffee Roasters — Q4 2020 Board of Directors Package
- Date: 2021-02-06
- Summary: Q4 2020 board package for Crestview Coffee Roasters (Fund II portfolio company). The company delivered Q4 revenue of $89.6M and EBITDA of $12.6M (14.1% margin), beating budget by ~3–5%. The Cascade Roasting bolt-on acquisition closed in Q4, adding Seattle production capacity and 18,000 DTC subscribers. DTC mix expanded to 26.9% of revenue vs. 22% at entry. LTM EBITDA stands at $44.7M vs. $36.5M at entry. Key risks include COVID-driven corporate channel weakness (–35% YoY) offset by DTC outperformance, freight cost inflation, and Cascade integration (tracking well). Q1 2021 revenue guidance of $89.1M; Blue Mountain Coffee bolt-on pipeline active.
- deal_context (confidence=0.88): company=Crestview Coffee Roasters, sector=consumer_products, subsector=specialty_beverage
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue not explicitly stated; only LTM EBITDA of $44.7M is provided. LTM revenue left null in structured payload.
  - The period_actuals LTM row (year=2020, quarter=null) captures only LTM EBITDA — revenue_usd and ebitda_margin are null as they cannot be derived from the document.
  - Geography set to west_us based on San Francisco HQ and Seattle production mention; company may operate nationally — geography signal is partial.
  - Q4 2020 EBITDA margin (14.1%) is for the single quarter; LTM EBITDA margin cannot be computed without LTM revenue.

  </details>

### `Board Materials/Board_Package_Q4_2021.pdf` → `doc_crestview_coffee_004` (board_package)
- Title: Crestview Coffee Roasters — Q4 2021 Board of Directors Package
- Date: 2022-02-06
- Summary: Q4 2021 board package for Crestview Coffee Roasters (Atlas Crossing Partners Fund II). The company delivered Q4 revenue of $98.1M (+9.5% YoY) and EBITDA of $14.2M (14.4% margin), beating budget by 3.0% and 6.0% respectively. LTM EBITDA stands at $51.7M vs. $36.5M at entry; net leverage improved to 5.2x from entry 5.9x. Key strategic highlights include subscription growth exceeding plan (73,926 subscribers vs. 75K plan), a corporate channel relaunch with 14 new accounts, approval of Portland 2 roasting facility, and an advanced LOI on the Blue Mountain Coffee add-on acquisition. Green coffee commodity inflation (+18% YoY) is the primary near-term risk.
- deal_context (confidence=0.92): company=Crestview Coffee Roasters, sector=consumer_products, subsector=specialty_beverage
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue not explicitly stated; only Q4 2021 quarterly revenue ($98.1M) and LTM EBITDA ($51.7M) are provided. LTM revenue left null in structured payload.
  - Q1 2022 revenue outlook of $97.5M is a forward projection and has been excluded from period_actuals.
  - Geography set to west_us based on HQ location (San Francisco) and Portland facility, but subscription/DTC business likely has national reach — may warrant 'national' designation at deal level.
  - Blue Mountain Coffee LOI mentioned as strategic initiative; this appears to be a prospective add-on acquisition. No financial details for Blue Mountain Coffee are provided in this document.

  </details>

### `Board Materials/Board_Package_Q4_2022.pdf` → `doc_crestview_coffee_005` (board_package)
- Title: Crestview Coffee Roasters — Q4 2022 Board of Directors Package
- Date: 2023-02-06
- Summary: Q4 2022 board package for Crestview Coffee Roasters (Fund II portfolio company). Q4 revenue of $113.8M (+16.0% YoY) and EBITDA of $16.8M (14.8% margin) beat budget by 3.2% and 5.0%, respectively. LTM EBITDA of $60.7M vs. entry baseline of $36.5M reflects strong growth. Net leverage improved to 5.2x from entry of 5.9x. Key strategic progress includes Blue Mountain acquisition integration, a Canada international DTC pilot (3,200 subscribers in 8 weeks), pricing power realization (+11% net revenue per subscriber), and completion of the Portland 2 roasting facility. DTC mix at 33.4% (up from 22.0% at entry) and subscription customers at 84,296 (up from 48,000 at entry). Key risks include input cost inflation and international execution complexity.
- deal_context (confidence=0.92): company=Crestview Coffee Roasters, sector=consumer_products, subsector=specialty_beverage
- <details><summary>⚠ extraction warnings</summary>

  - Q4 2022 revenue of $113.8M is a single-quarter figure, not LTM; LTM revenue is not explicitly stated in the document — only LTM EBITDA ($60.7M) is provided.
  - The 'Blue Mountain integration' target date in the Strategic Initiatives table reads 'Q3 2022' but is likely a typo for Q3 2023 given the document date is February 2023 and integration is described as still 'In progress'.
  - Subscription customer KPI value (84,296.3) appears to include an erroneous decimal — likely 84,296 customers.
  - ebitda_margin in structured payload reflects Q4 2022 quarter margin (14.8%); LTM margin is not directly calculable from available data.

  </details>

### `Board Materials/Board_Package_Q4_2023.pdf` → `doc_crestview_coffee_006` (board_package)
- Title: Crestview Coffee Roasters — Q4 2023 Board of Directors Package
- Date: 2024-02-06
- Summary: Q4 2023 board package for Crestview Coffee Roasters (Atlas Crossing Partners Fund II). The company delivered Q4 2023 revenue of $124.0M and EBITDA of $18.8M (15.2% margin), beating budget by 3.1% on revenue and 5.0% on EBITDA. LTM EBITDA stands at $68.8M vs. entry of $36.5M, with net leverage improved to 4.7x from entry of 5.9x. DTC mix has grown to 36.7% of revenue (from 22.0% at entry), subscription customers at ~94.7K vs. 48K at entry. The IC has approved exit preparation targeting an H2 2025 sell-side process; banker shortlist is being prepared and Houlihan Lokey engagement is targeted for Q1 2024. Key strategic initiatives include a Whole Foods retail channel pilot (320 stores live), ESG/B-Corp certification in progress, and international subscription scaling (Canada 14K subs, UK pilot live).
- deal_context (confidence=0.92): company=Crestview Coffee Roasters, sector=consumer_products, subsector=specialty_beverage
- <details><summary>⚠ extraction warnings</summary>

  - ESG/B-Corp certification detail reads 'expected Q2 2023' — likely a typo in the source document; probably intended Q2 2024.
  - Geography tagged as west_us based on HQ address (San Francisco, CA); company may operate nationally.
  - LTM revenue not explicitly stated; LTM EBITDA of $68.8M is provided. Q4 2023 revenue ($124.0M) is a single-quarter figure, not LTM.
  - Retail channel pilot geography (Whole Foods national) suggests national footprint, but HQ is west_us.

  </details>

### `Board Materials/Board_Package_Q4_2024.pdf` → `doc_crestview_coffee_007` (board_package)
- Title: Crestview Coffee Roasters — Q4 2024 Board of Directors Package
- Date: 2025-02-06
- Summary: Q4 2024 board package for Crestview Coffee Roasters (Atlas Crossing Partners Fund II). Company delivered Q4 revenue of $135.3M and EBITDA of $21.0M (15.5% margin), both ahead of budget. LTM EBITDA stands at $76.9M, net leverage at 4.4x (down from 5.9x at entry). DTC represents ~40% of revenue with 105K+ subscription customers tracking toward 110K+ exit milestone. Houlihan Lokey engaged as sell-side advisor; CIM outline complete with management presentation IC review planned for Q2. Board package covers financial performance, operational KPIs, strategic initiatives (exit process, subscription growth, retail expansion, management equity refresh), and risk review. Exit process underway with first-round bids targeted Q4 2024 per the timeline.
- deal_context (confidence=0.92): company=Crestview Coffee Roasters, sector=consumer_products, subsector=specialty_beverage
- <details><summary>⚠ extraction warnings</summary>

  - Q1 2025 outlook section contains inconsistent year references ('CIM distribution target Q2 2024', 'Management presentations Q3 2024', 'First-round bids target Q4 2024') — these likely should read 2025, not 2024; treated as typographical errors.
  - Revenue LTM figure not explicitly stated; only Q4 quarterly revenue ($135.3M) and LTM EBITDA ($76.9M) are provided.
  - DTC % of Revenue shows 39.9% in KPI table vs. 42% cited in Executive Summary — minor discrepancy; used 39.9% as the precise KPI figure.
  - Geography set to west_us based on San Francisco HQ address; company may operate nationally.

  </details>

### `Board Materials/Board_Package_Q4_2025.pdf` → `doc_crestview_coffee_008` (board_package)
- Title: Crestview Coffee Roasters — Q4 2025 Board of Directors Package
- Date: 2026-02-06
- Summary: Q4 2025 board package for Crestview Coffee Roasters (Atlas Crossing Partners Fund II). The company delivered Q4 2025 revenue of $147.7M (+9.2% YoY) and EBITDA of $23.5M (15.9% margin), both ahead of budget by ~3–5%. LTM EBITDA stands at $85.9M vs. an entry baseline of $36.5M, reflecting significant hold-period growth. Net leverage has decreased from 5.9x at entry to 4.2x. The company is actively in a final-round exit process with three shortlisted buyers, a definitive agreement targeted for Q1 2026, and close expected Q2 2026. DTC revenue mix has grown from 22% to 43.2%, and subscription customers have more than doubled from 48,000 to 115,407. Operational KPIs are at or near targets. Key exit-readiness milestones (VDR population, management presentations) are complete.
- deal_context (confidence=0.95): company=Crestview Coffee Roasters, sector=consumer_products, subsector=specialty_beverage
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue not explicitly stated; only Q4 2025 quarterly revenue ($147.7M) and LTM EBITDA ($85.9M) are provided — revenue_ltm_usd left null.
  - Geography inferred as west_us based on Atlas Crossing Partners San Francisco office address; company headquarters not separately stated.
  - Entry EV not disclosed in this document; entry LTM EBITDA provided as $36.5M for reference.
  - Exit process is clearly underway but no realized exit figures exist yet — returns_extract left null as transaction has not closed.

  </details>

### `Deal Materials/IC_Memo_Entry_2019-04.pdf` → `doc_crestview_coffee_009` (ic_memo)
- Title: Investment Committee Memorandum — Entry — Crestview Coffee Roasters, Inc.
- Date: 2019-04-17
- Summary: Atlas Crossing Partners Fund III entry IC memo recommending acquisition of Crestview Coffee Roasters, Inc. at $493M enterprise value (13.5x LTM Adj. EBITDA). Crestview is a vertically integrated DTC premium coffee brand with $270M LTM revenue and $36.5M LTM EBITDA. The investment thesis centers on subscription flywheel recurring revenue, DTC channel expansion (22% to 44% of mix), roasting capacity-driven margin expansion, and fragmented specialty coffee market consolidation. Base case projects a Year 5 exit at ~$1.01B EV yielding 2.7x MoIC and 22% gross IRR. Total sources/uses of $509M funded by $213M senior secured debt, $264M sponsor equity, and $32M management rollover. IC recommendation is unanimous: INVEST — PROCEED TO CLOSE.
- deal_context (confidence=0.95): company=Crestview Coffee Roasters, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - revenue_cagr_3yr not directly stated; could be computed from projections but was left null as only forward projections (not 3-year historical CAGR) are presented
  - underwriting_case_extract ltm_entry row uses a non-standard key 'ltm_entry' as the document presents the entry LTM period separately from projection years 2019A–2023E
  - exit EV for year_5_exit computed as 13.5x × $75M = $1,012.5M per base case scenario table
  - subsector 'packaged_food' is an imperfect fit; taxonomy proposal submitted for 'dtc_premium_coffee_subscription'

  </details>

## Resolver disagreements

### subsector
- Chosen: `specialty_beverage` (plurality 7/8)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf', 'Board Materials/Board_Package_Q4_2019.pdf', 'Board Materials/Board_Package_Q4_2021.pdf', 'Board Materials/Board_Package_Q4_2022.pdf', 'Board Materials/Board_Package_Q4_2023.pdf', 'Board Materials/Board_Package_Q4_2024.pdf', 'Board Materials/Board_Package_Q4_2025.pdf']
- Dissent `packaged_food`: ['Deal Materials/IC_Memo_Entry_2019-04.pdf']

### geography
- Chosen: `west_us` (plurality 6/8)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf', 'Board Materials/Board_Package_Q4_2019.pdf', 'Board Materials/Board_Package_Q4_2021.pdf', 'Board Materials/Board_Package_Q4_2023.pdf', 'Board Materials/Board_Package_Q4_2024.pdf', 'Board Materials/Board_Package_Q4_2025.pdf']
- Dissent `national`: ['Board Materials/Board_Package_Q4_2022.pdf', 'Deal Materials/IC_Memo_Entry_2019-04.pdf']

### financials.ebitda_ltm_usd
- Chosen: `88400000.0` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Board Materials/Board_Package_Q1_2026.pdf']
- Dissent `68800000.0`: ['Board Materials/Board_Package_Q4_2023.pdf']
- Dissent `60700000.0`: ['Board Materials/Board_Package_Q4_2022.pdf']
- Dissent `51700000.0`: ['Board Materials/Board_Package_Q4_2021.pdf']
- Dissent `44700000.0`: ['Board Materials/Board_Package_Q4_2020.pdf']
- Dissent `37700000.0`: ['Board Materials/Board_Package_Q4_2019.pdf']
- Dissent `36500000.0`: ['Deal Materials/IC_Memo_Entry_2019-04.pdf']

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- geography: proposed=`west_us` (used `west_us`, confidence=0.75)
  - rationale: Company headquarters and board meeting location is San Francisco, CA (2 Embarcadero Center); Portland 2 facility also in the Pacific Northwest. 'west_us' is the best fit, though the company appears to have national DTC reach via subscriptions.
- geography: proposed=`national` (used `west_us`, confidence=0.72)
  - rationale: Crestview Coffee Roasters operates a Whole Foods retail pilot across 320 stores (likely national) and has international subs in Canada and UK, suggesting a national or broader footprint despite HQ being in San Francisco. However, 'national' is available in the taxonomy and may be more appropriate.
- subsector: proposed=`dtc_premium_coffee_subscription` (used `packaged_food`, confidence=0.65)
  - rationale: Crestview Coffee Roasters is a vertically integrated DTC premium coffee subscription brand — a distinct business model not captured by any existing consumer_products subsector. 'packaged_food' is the closest available option, but the subscription/DTC delivery mechanic and premium positioning are materially different from traditional packaged food distribution.
