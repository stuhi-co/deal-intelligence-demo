# Ingestion report — Cardinal Filtration Co.

Deal ID: `deal_cardinal_filtration_co_2014`
Company canonical: `Cardinal Filtration Co.`
Sector / subsector: `industrial_distribution` / `specialty_distribution`
Geography: `national`
Deal type: `platform`
Voted with 11 qualifying docs at confidence >= 0.9 (out of 20 tagged).

## Triage

### primary (20)
- `Deal Performance/Final_Returns_Summary_2019-09.xlsx`
- `Deal Performance/IC_Memo_Entry_2014-04.pdf`
- `Deal Performance/IC_Memo_Exit_2019-08.pdf`
- `Exit Process Materials/Bids/Final Bid Comparison 2019-08.xlsx` [hint: final_bid_comparison]
- `Exit Process Materials/Bids/IOI Tracker 2019-06.xlsx` [hint: ioi_tracker]
- `Exit Process Materials/Bids/Management Presentation — Buyer Shortlist 2019-06.pdf` [hint: management_presentation]
- `Exit Process Materials/Closing Execution/Closing Checklist 2019-09.xlsx` [hint: dd_report]
- `Exit Process Materials/Closing Execution/Funds Flow and Closing Statement 2019-09-20.pdf` [hint: funds_flow]
- `Exit Process Materials/Closing Execution/HSR Filing Summary 2019-08.pdf` [hint: dd_report]
- `Exit Process Materials/Diligence/Data Room Index 2019-04.pdf` [hint: dd_report]
- `Exit Process Materials/Diligence/Sell-Side QofE Summary 2019-05.pdf` [hint: qofe]
- `Exit Process Materials/Diligence/VDD Financial Model 2019-05.xlsx` [hint: vdd_model]
- `Exit Process Materials/Marketing/CIM — Cardinal Filtration Co. 2019-05.pdf` [hint: cim]
- `Exit Process Materials/Marketing/Final Round Process Letter 2019-07.pdf`
- `Exit Process Materials/Marketing/First Round Process Letter 2019-05.pdf`
- `Exit Process Materials/Marketing/Teaser — Baird 2019-04.pdf` [hint: teaser]
- `Exit Process Materials/Post Exit Compliance/Escrow Agreement Summary 2019-09.pdf` [hint: dd_report]
- `Exit Process Materials/Post Exit Compliance/Escrow Release Notice 2021-03.pdf` [hint: dd_report]
- `Exit Process Materials/Post Exit Compliance/GP-LP Distribution Notice 2019-09.pdf` [hint: dd_report]
- `Exit Process Materials/Post Exit Compliance/Indemnity Holdback Tracker.xlsx` [hint: dd_report]

### format_duplicate (14)
- `Deal Performance/IC_Memo_Entry_2014-04.docx` — PDF preferred over DOCX/PPTX twin
- `Deal Performance/IC_Memo_Exit_2019-08.docx` — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Bids/Management Presentation — Buyer Shortlist 2019-06.docx` [hint: management_presentation] — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Closing Execution/Funds Flow and Closing Statement 2019-09-20.docx` [hint: funds_flow] — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Closing Execution/HSR Filing Summary 2019-08.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Diligence/Data Room Index 2019-04.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Diligence/Sell-Side QofE Summary 2019-05.docx` [hint: qofe] — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Marketing/CIM — Cardinal Filtration Co. 2019-05.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Marketing/Final Round Process Letter 2019-07.docx` — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Marketing/First Round Process Letter 2019-05.docx` — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Marketing/Teaser — Baird 2019-04.docx` [hint: teaser] — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Post Exit Compliance/Escrow Agreement Summary 2019-09.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Post Exit Compliance/Escrow Release Notice 2021-03.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Exit Process Materials/Post Exit Compliance/GP-LP Distribution Notice 2019-09.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Deal Performance/Final_Returns_Summary_2019-09.xlsx` → `doc_cardinal_filtration_co_001` (returns_summary)
- Title: Cardinal Filtration Co. — Final Returns Summary
- Date: 2019-09-20
- Summary: Final returns summary workbook for Cardinal Filtration Co. (Atlas Crossing Partners Fund I). Exit closed September 20, 2019 via strategic sale to Donaldson Company (NYSE: DCI). The fund held Cardinal for ~5 years (Sept 2014–Sept 2019), completing 4 bolt-on acquisitions (Phoenix Industrial, Apex Filter, Filtration Pros, EnvioGuard). Entry EV of $175M at 7.5x EBITDA; exit EV of $560M at 9.5x EBITDA. Gross MOIC of 3.2x and Gross IRR of 26.1%. Revenue grew from $186M at entry to $472M at exit; Adj. EBITDA from $23.3M to $58.9M. Value creation driven primarily by bolt-on acquisitions ($98M equity contribution), organic growth ($72M), and multiple expansion ($70M).
- deal_context (confidence=0.95): company=Cardinal Filtration Co., sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - Net cash flow and cumulative net CF columns are blank in the Cash Flows & IRR sheet — IRR/MOIC calculation rows also blank; headline figures taken from Returns Summary sheet instead.
  - Escrow release of $20M (2021-03-20) is included in gross distributions on the Returns Summary sheet ($221M total = $31M dividend recap + $170M exit proceeds + $20M escrow); IRR of 26.1% (labeled 5.3-year hold) likely accounts for the 2021 escrow cash flow timing.
  - Revenue CAGR 3yr not explicitly stated; omitted rather than calculated from KPI table to avoid conflating organic vs. acquisition-driven growth.
  - Hold period shown as both 5.0 years (Deal Statistics) and 5.3 years (IRR label) — IRR calculation likely uses 5.3 years inclusive of escrow tail; entry_ev_usd and exit_ev_usd taken from explicitly labeled Deal Statistics rows.

  </details>

### `Deal Performance/IC_Memo_Entry_2014-04.pdf` → `doc_cardinal_filtration_co_002` (ic_memo)
- Title: Investment Committee Memorandum — Initial Investment Recommendation: Cardinal Filtration Co.
- Date: 2014-04-24
- Summary: Atlas Crossing Partners Fund I entry IC memo recommending the acquisition of Cardinal Filtration Co., a regional industrial filtration distributor headquartered in Akron, OH, at an enterprise value of $175M (7.5x LTM Adj. EBITDA of $23.3M). The investment thesis centers on a disciplined roll-up strategy in the highly fragmented ~$8B US industrial filtration distribution market, private-label penetration expansion (9% → 25%), supplier consolidation, and organic revenue growth in defensive end markets. The base case underwrites 4 bolt-on acquisitions over a 5-year hold, targeting exit EBITDA of $52M at an 8.5x multiple ($442M EV), implying a 4.0x MOIC and 32% gross IRR. Deal team: S. Kowalski (MD), R. Patel (Principal), L. Chen (VP).
- deal_context (confidence=0.97): company=Cardinal Filtration Co., sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - FY13A EBITDA of $23M (table row) appears rounded; the memo text and deal snapshot consistently reference $23.3M LTM Adj. EBITDA — structured fields use $23.3M.
  - period_actuals EBITDA for FY2013 set to $23M per the table row; LTM figure of $23.3M used elsewhere may include stub-period adjustments.
  - Geography tagged as midwest_us (HQ Akron, OH) but company operates nationally across 18 states with DCs in Memphis, Dallas, and Phoenix — a taxonomy_proposals entry has been added.
  - Downside and upside scenario returns are present in the document but only the base case has been captured in underwriting_case_extract per instructions (base case = year_5_exit). Downside: 1.9x MOIC / 14.0% IRR / $231M EV; Upside: 5.8x MOIC / 42.0% IRR / $589M EV.

  </details>

### `Deal Performance/IC_Memo_Exit_2019-08.pdf` → `doc_cardinal_filtration_co_003` (ic_memo)
- Title: Exit Recommendation — Cardinal Filtration Co.
- Date: 2019-08-08
- Summary: Atlas Crossing Partners Fund I IC exit memo recommending the sale of Cardinal Filtration Co. to Donaldson Company, Inc. (NYSE: DCI) for $560M enterprise value (9.5x LTM Adj. EBITDA of $58.9M). The deal represents a 5.3-year hold from September 2014, delivering 3.2x gross MOIC and ~26.1% gross IRR (2.6x / 21.2% net). Entry thesis centered on industrial filtration roll-up was largely delivered: 4 bolt-ons completed, gross margin expanded 320bps, private-label penetration grew from 9% to 28%, and revenue scaled from $186M to $472M. Operating margin was flat (thesis miss due to bolt-on mix shift). Sale process run by Baird yielded three final bids; Donaldson selected at $560M all-cash, no financing condition.
- deal_context (confidence=0.97): company=Cardinal Filtration Co., sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - Holding period stated as 5.3 years; returns_extract holding_period_years rounded to integer 5 per schema type constraint.
  - Entry EV at acquisition (2014) not explicitly stated in the document; entry_ev_usd left null.
  - IRR stored as decimal (0.261) per schema convention; gross IRR is ~26.1%.
  - Net MOIC (2.6x) and Net IRR (21.2%) noted but returns_extract uses gross figures as primary; net figures captured in structured summary.

  </details>

### `Exit Process Materials/Bids/Final Bid Comparison 2019-08.xlsx` → `doc_cardinal_filtration_co_004` (final_bid_comparison)
- Title: Cardinal Filtration Co. — Final Round Bid Comparison
- Date: 2019-08-09
- Summary: Final round bid comparison for the exit sale of Cardinal Filtration Co., prepared by ACP/Baird in August 2019. Three bids were received: Donaldson (DCI) at $560M EV (9.5x LTM EBITDA, 100% cash, no financing condition) was selected as the highest value and highest certainty bid; Parker (Strategic B) at $530M (9.0x) was the runner-up; and Sponsor X (PE) at $520M (8.8x, with earnout and management rollover requirements) was declined. Anticipated close dates ranged from September 20–30, 2019. Seller recommendation was Donaldson based on superior value and deal certainty.
- deal_context (confidence=0.82): company=Cardinal Filtration Co., sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - LTM EBITDA was back-calculated from the $560M EV at 9.5x multiple (implied LTM EBITDA ≈ $58.95M); not explicitly stated in the document.
  - Sector and subsector inferred from company name 'Cardinal Filtration Co.' — no explicit sector classification in the document.
  - returns_extract populated with the winning bid EV ($560M, Donaldson/DCI) as the exit EV; this is the selected bid price, not a confirmed closing figure.
  - Deal type defaulted to 'platform' as no explicit platform/add-on classification is present; this is a sell-side exit process.

  </details>

### `Exit Process Materials/Bids/IOI Tracker 2019-06.xlsx` → `doc_cardinal_filtration_co_005` (ioi_tracker)
- Title: Cardinal Filtration Co. — IOI Tracker
- Date: 2019-06-14
- Summary: First-round IOI tracker for Cardinal Filtration Co.'s exit process, prepared by Robert W. Baird & Co. with bids received by June 14, 2019. Nine parties submitted indications of interest — five strategics and four financial sponsors. EV ranges span $410M–$560M (6.9x–9.5x implied EBITDA multiple). Donaldson Company (DCI) submitted the highest bid at $530–560M (9.0–9.5x) and was selected as preferred buyer; Parker Hannifin and one financial sponsor (Fund VI) were also shortlisted. Four parties were not advanced due to low valuation, excessive conditionality, strategic misfit, or financing concerns.
- deal_context (confidence=0.9): company=Cardinal Filtration Co., sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - ev_proposed_usd and ev_ebitda_multiple set to midpoint of preferred buyer (Donaldson Company) range: ($530M+$560M)/2=$545M, (9.0x+9.5x)/2=9.25x
  - Implied EBITDA multiple denominators suggest LTM EBITDA ~$59M but not explicitly stated in document — not populated
  - deal_type set to 'platform' as the exit process involves the full company sale; no add-on or carve-out signals present
  - Sector assigned as industrial_distribution / specialty_distribution based on filtration products company and bidder interest in 'distribution footprint' (Grainger noted)

  </details>

### `Exit Process Materials/Bids/Management Presentation — Buyer Shortlist 2019-06.pdf` → `doc_cardinal_filtration_co_006` (management_presentation)
- Title: Cardinal Filtration Co. — Management Presentation
- Date: 2019-06-01
- Summary: Management presentation prepared for final-round buyer meetings in June–July 2019 as part of Cardinal Filtration Co.'s exit process. Cardinal is a national industrial filtration products distributor headquartered in Akron, OH, founded in 1987 and acquired by Atlas Crossing Partners in September 2014. Over the ~5-year hold, the company grew revenue from $186M to $472M LTM through organic growth and four bolt-on acquisitions, with EBITDA expanding from $23.3M to $58.9M. Key value creation levers include a disciplined roll-up M&A playbook, private-label (CardinalGuard) expansion from 9% to 28% of revenue with a 600bps GM premium, and geographic DC footprint growth from 4 to 12 locations. Future opportunities highlighted include further geographic expansion, private-label penetration to 35–40%, engineered solutions/service revenue growth, and a potential Canadian distribution hub.
- deal_context (confidence=0.95): company=Cardinal Filtration Co., sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - EBITDA margin of 12.47% calculated from disclosed Revenue ($472M) and Adj. EBITDA ($58.9M) LTM figures — not explicitly stated as a percentage in the document.
  - Revenue CAGR not directly calculable from the document; only FY14 entry ($186M) and FY19 LTM ($472M) figures provided across a ~5-year period.
  - No EV or purchase price multiples disclosed in this management presentation; document is prepared for buyer meetings as part of the exit process.
  - doc_type confirmed as management_presentation consistent with folder hint and document content.

  </details>

### `Exit Process Materials/Closing Execution/Closing Checklist 2019-09.xlsx` → `doc_cardinal_filtration_co_007` (funds_flow)
- Title: Cardinal Filtration Co. — Closing Checklist
- Date: 2019-09-20
- Summary: Closing checklist for the sale of Cardinal Filtration Co. to Donaldson, managed by Kirkland & Ellis LLP on behalf of ACP, targeting a close of September 20, 2019. All 20 line items are marked complete. Key milestones include execution of the Stock Purchase Agreement (Aug 21), HSR early termination (Sep 5), lien releases from Madison Capital, R&W insurance binding ($28M limit), and closing wire of $560M purchase price on Sep 20. Debt payoff to Madison Capital totaled $185M; net equity proceeds to ACP Fund I were $190M; $20M placed in indemnity escrow; and $221M total LP distribution (including 2017 recap) was issued Sep 23 and distributed Sep 27. Transaction expenses totaled ~$15M (Baird $11.2M, K&E $2.8M, other $1.0M).
- deal_context (confidence=0.92): company=Cardinal Filtration Co., sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - doc_type overridden from folder hint 'dd_report' to 'funds_flow': document is a closing checklist with funds flow and wire details for an M&A exit transaction, not a due diligence report.
  - subsector 'industrial_components' assigned under 'manufacturing' for a filtration products company — closest available subsector. A more specific 'filtration_products' or 'industrial_equipment' subsector would be more precise.
  - Entry EV, IRR, and MOIC are not present in this document; only exit-side wire amounts are captured.
  - Net equity proceeds to ACP Fund I from closing wire: $190M. Total LP distribution including 2017 recap: $221M — the $31M delta reflects the prior recap distribution and is not a separate closing payment.
  - R&W insurance: Policy #RW-2019-7741, $28M limit, $1.4M premium (Marsh McLennan).
  - Indemnity escrow: $20M to Wells Fargo, 18-month term.

  </details>

### `Exit Process Materials/Closing Execution/Funds Flow and Closing Statement 2019-09-20.pdf` → `doc_cardinal_filtration_co_008` (funds_flow)
- Title: Cardinal Filtration Co. — Funds Flow Memorandum
- Date: 2019-09-20
- Summary: Closing funds flow memorandum prepared by Kirkland & Ellis LLP for the sale of Cardinal Filtration Co. to Donaldson Company on September 20, 2019. Enterprise value agreed at $560M. After repaying $185.4M of Madison Capital debt, $15M in transaction expenses, and a $20M indemnity escrow holdback, net equity proceeds to ACP Fund I totaled ~$339.6M. The equity waterfall shows return of $69M invested capital (platform + 4 bolt-ons), an 8% preferred return hurdle of $47.2M, and remaining carry split 80/20 between LPs ($178.7M) and GP ($44.7M). Combined with a 2017 dividend recap LP share of $27.9M, cumulative LP proceeds total $323.8M.
- deal_context (confidence=0.92): company=Cardinal Filtration Co., sector=None, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - Entry EV, IRR, and MOIC are not stated in this document; returns_extract is partially populated with exit EV only. Cross-reference with returns_summary or entry IC memo to complete.
  - Holding period can be inferred as approximately 5.3 years (per preferred return note) but is not explicitly stated as an integer; left null.
  - Sector/subsector not determinable from this closing document alone; deal_context sector left null.
  - NWC adjustment noted as $0 at peg ($66.2M actual vs. $66.0M peg); final adjustment TBD per document.

  </details>

### `Exit Process Materials/Closing Execution/HSR Filing Summary 2019-08.pdf` → `doc_cardinal_filtration_co_009` (dd_report)
- Title: Cardinal Filtration Co. — HSR Filing Summary
- Date: 2019-08-22
- Summary: HSR Filing Summary prepared by Kirkland & Ellis LLP for the acquisition of Cardinal Filtration Co. by Donaldson Company, Inc. at a transaction value of $560M. The filing was made on August 22, 2019; early termination of the 30-day waiting period was granted by the DOJ Antitrust Division on September 5, 2019 (Day 14), with the transaction closing on September 20, 2019. Clearance was granted on the basis of no competitive overlap — Donaldson is a manufacturer and Cardinal is a distributor, presenting a vertical rather than horizontal combination with minimal antitrust risk.
- deal_context (confidence=0.92): company=Cardinal Filtration Co., sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint was 'dd_report' but this document is an HSR antitrust regulatory filing summary, not a diligence report. Retaining dd_report as closest available doc_type since no 'regulatory_filing' type exists in the taxonomy.
  - Transaction value of $560M is the stated deal consideration (SPA executed), treated as exit_ev_usd in returns_extract; entry EV, IRR, and MOIC are not present in this document.
  - Seller identified as Atlas Crossing Partners Fund I, L.P. — implies this is an exit transaction for the PE sponsor.
  - Closing date September 20, 2019 is confirmed in the timeline; date field set to HSR filing date August 22, 2019 per document header.

  </details>

### `Exit Process Materials/Diligence/Data Room Index 2019-04.pdf` → `doc_cardinal_filtration_co_010` (dd_report)
- Title: Cardinal Filtration Co. — Virtual Data Room Index
- Date: 2019-04-01
- Summary: Virtual Data Room (VDR) index prepared by Robert W. Baird & Co. for Cardinal Filtration Co.'s exit process, dated April 2019. The document catalogues 12 top-level VDR sections covering corporate records, audited financials (FY14–FY18), adjusted EBITDA/QofE workpapers, management projections, legal/bolt-on acquisition agreements (4 bolt-ons), customer detail, supplier MSAs, operations, HR/equity, tax, environmental (12 DCs), insurance, IT/ERP (NetSuite/WMS), and a private-label product line (CardinalGuard). Access permissions are granted to five parties: Donaldson Company, Parker Hannifin, Sponsor X (full access), Strategic C (3M) and Sponsor Y (limited pre-IOI access). The Technology/IT section (11.0) is still in progress.
- deal_context (confidence=0.8): company=Cardinal Filtration Co., sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - Doc_type overridden from folder hint 'dd_report': this is a VDR index/table of contents, not a substantive DD report. Closest existing type remains dd_report per taxonomy. A taxonomy_proposals entry has been added.
  - No financial figures present in document — all structured financial fields are null.
  - Technology/IT section (11.0) explicitly marked 'In progress' — cybersecurity assessment incomplete at time of document preparation.
  - Five bidder parties identified: Donaldson Company, Parker Hannifin, Sponsor X (full access); 3M (Strategic C) and Sponsor Y (limited pre-IOI access) — suggests active exit sale process as of May 2019.
  - Date derived from document header ('April 2019'); access permissions granted May 20, 2019 — minor date discrepancy noted (index prepared April, access granted May).

  </details>

### `Exit Process Materials/Diligence/Sell-Side QofE Summary 2019-05.pdf` → `doc_cardinal_filtration_co_011` (qofe)
- Title: Cardinal Filtration Co. — Sell-Side Quality of Earnings Summary
- Date: 2019-05-01
- Summary: Grant Thornton Transaction Advisory Services prepared this sell-side Quality of Earnings (VDD QofE) for Cardinal Filtration Co. on behalf of Atlas Crossing Partners (ACP) in support of the May 2019 exit/sale process. The report bridges LTM March 2019 reported EBITDA of $52.4M to a preliminary adjusted EBITDA of $58.9M through $6.5M in addbacks (CEO comp normalization, EnvioGuard integration costs, non-recurring legal/advisory, phantom equity amortization, D&A reclassification) offset by a $0.6M revenue timing haircut. Key findings confirm high revenue quality (87% recurring, no customer >6% of revenue), supportable and well-documented adjustments, normalized working capital (NWC peg of $66M), and a structural private-label margin premium for the CardinalGuard product line (40.8% GM vs. 34.3% branded).
- deal_context (confidence=0.88): company=Cardinal Filtration Co., sector=manufacturing, subsector=process_manufacturing
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue figure not explicitly stated in the document; ebitda_margin and revenue_cagr_3yr cannot be calculated.
  - Reported EBITDA (pre-addbacks) is $52.4M; adjusted/normalized EBITDA per GT VDD conclusion is $58.9M — structured payload reflects the adjusted figure as ebitda_ltm_usd per QofE convention.
  - Geography not identified in the document.
  - deal_type set to 'platform' inferred from context (ACP as PE sponsor, EnvioGuard add-on acquisition referenced); not explicitly stated in this doc.
  - founder_dependency risk flag inferred from 'Brandt family' CEO comp normalization addback.

  </details>

### `Exit Process Materials/Diligence/VDD Financial Model 2019-05.xlsx` → `doc_cardinal_filtration_co_012` (vdd_model)
- Title: Cardinal Filtration Co. — VDD Financial Analysis (Grant Thornton)
- Date: 2019-05-01
- Summary: Vendor due diligence financial model prepared by Grant Thornton for Cardinal Filtration Co.'s exit process. Covers FY14–LTM March 2019 income statement with reported and adjusted EBITDA build (CEO comp excess, one-time M&A/integration, non-recurring legal, phantom equity, revenue timing, and D&A reclassification adjustments), plus a trailing 12-month net working capital peg analysis across FY16–LTM Mar-19. LTM March 2019 revenue was $472M; key adjustments total approximately $6.5M for the LTM period. Net working capital peg is proposed based on the FY17–LTM average.
- deal_context (confidence=0.78): company=Cardinal Filtration Co., sector=manufacturing, subsector=process_manufacturing
- <details><summary>⚠ extraction warnings</summary>

  - EBITDA (reported) and Adj. EBITDA rows are blank/formula-driven in the workbook — actual computed values were not rendered in the markdown. Adj. EBITDA and margin cannot be directly extracted.
  - revenue_cagr_3yr estimated from FY15–FY18 ($232M to $428M), yielding ~22.9% CAGR; alternatively FY16–LTM used to compute ~16.1% — used FY16 to LTM Mar-19 as the most meaningful 3-year window available.
  - NWC peg totals and NWC as % revenue rows are blank/formula-driven and were not rendered.
  - doc_type confirmed as vdd_model consistent with folder hint and content (sell-side QoE / VDD prepared by Grant Thornton).

  </details>

### `Exit Process Materials/Marketing/CIM — Cardinal Filtration Co. 2019-05.pdf` → `doc_cardinal_filtration_co_013` (cim)
- Title: Project Titan — Confidential Information Memorandum
- Date: 2019-05-01
- Summary: CIM prepared by Robert W. Baird & Co. on behalf of Atlas Crossing Partners Fund I for the sale of Cardinal Filtration Co. ("Project Titan"). Cardinal is a national industrial filtration products distributor headquartered in Akron, OH, serving 11,200 customers across manufacturing, power generation, water treatment, F&B, and HVAC. ACP acquired the business in 2014 at ~$186M revenue and grew it to $472M LTM revenue / $58.9M Adj. EBITDA through four bolt-on acquisitions, private-label expansion (CardinalGuard now 28% of revenue), and supplier consolidation across 12 distribution centers. The process is a targeted sell-side with IOI deadline June 14, 2019 and anticipated close September 20, 2019. Strategic rationale for a buyer centers on cross-sell into Cardinal's 11,200 mid-market accounts and continued private-label penetration toward 35–40%.
- deal_context (confidence=0.95): company=Cardinal Filtration Co., sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - No explicit EV or EV/EBITDA entry multiple disclosed in this CIM; ev_proposed_usd and ev_ebitda_multiple left null.
  - Revenue CAGR not explicitly stated; period_actuals populated from the financial summary table instead.
  - LTM figures are as of March 2019 (not a full fiscal year); tagged under period_actuals as a separate note but not assigned a year row to avoid double-counting with FY2018.
  - EnvioGuard Industries bolt-on listed as 'synergies in progress' — integration_risk flagged accordingly.

  </details>

### `Exit Process Materials/Marketing/Final Round Process Letter 2019-07.pdf` → `doc_cardinal_filtration_co_014` (process_letter)
- Title: Final Round Process Letter – Cardinal Filtration Co.
- Date: 2019-07-15
- Summary: Final round process letter issued by Robert W. Baird & Co. on behalf of Atlas Crossing Partners Fund I for the sale of Cardinal Filtration Co. The letter establishes the final round timeline (bids due August 9, 2019; anticipated close September 20, 2019), specifies binding bid requirements (executed NBO with stated EV, marked SPA, committed financing, rollover summary, diligence confirmation), and outlines seller preferences including 100% cash at close, no earnout, ≤5% escrow with 18-month tail, R&W insurance preferred, no financing condition, and HSR clearance within 30 days.
- deal_context (confidence=0.85): company=Cardinal Filtration Co., sector=None, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - No financial figures (EV, revenue, EBITDA) are stated in this process letter — structured financials are all null.
  - Deal type is ambiguous from taxonomy perspective: this is a sell-side exit process; 'platform' was selected as closest existing value but a proposed 'exit_sale' taxonomy entry has been flagged.
  - Sector could not be determined from this document alone; 'Filtration' in company name suggests manufacturing/industrial but sector left unset due to insufficient evidence.

  </details>

### `Exit Process Materials/Marketing/First Round Process Letter 2019-05.pdf` → `doc_cardinal_filtration_co_015` (process_letter)
- Title: First Round Process Letter – Cardinal Filtration Co.
- Date: 2019-05-17
- Summary: First-round sale process letter issued by Robert W. Baird & Co. on behalf of Atlas Crossing Partners Fund I for the sale of Cardinal Filtration Co. The letter invites prospective buyers to submit Indications of Interest by June 14, 2019, outlines the full process timeline (CIM distribution through final round invitations in July 2019), specifies IOI content requirements (proposed EV range, EBITDA multiple, transaction structure, financing approach, diligence requirements, management rollover assumptions, and strategic/financial rationale), and notes that VDR access has been granted via Intralinks containing FY2014–FY2018 audited financials and LTM management accounts.
- deal_context (confidence=0.85): company=Cardinal Filtration Co., sector=None, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - Deal type set to 'platform' as a proxy — this is an exit/sell-side process letter and no 'exit' deal_type exists in the taxonomy.
  - No financial metrics (EV, EBITDA, revenue) are disclosed in this document; IOI requirements reference EV range and EBITDA multiple but do not provide actual figures.
  - Sector and subsector cannot be determined from this document alone; 'Cardinal Filtration Co.' name suggests industrial/filtration but no explicit sector is stated.

  </details>

### `Exit Process Materials/Marketing/Teaser — Baird 2019-04.pdf` → `doc_cardinal_filtration_co_016` (teaser)
- Title: Project Titan — Confidential Teaser
- Date: 2019-04-01
- Summary: Sell-side teaser prepared by Robert W. Baird & Co. in April 2019 for Cardinal Filtration Co. (Project Titan), a category-leading industrial filtration distributor headquartered in Akron, OH. The teaser markets the exit of Atlas Crossing Partners Fund I's investment, highlighting a successful roll-up of 4 bolt-on acquisitions since 2015, strong recurring revenue (87% repeat customers), private-label expansion from 9% to 28%, and LTM revenue of $472M with Adj. EBITDA of $58.9M (12.5% margin). A targeted sell-side process is underway with final bids expected August 2019 and close anticipated September 2019.
- deal_context (confidence=0.95): company=Cardinal Filtration Co., sector=industrial_distribution, subsector=specialty_distribution
- <details><summary>⚠ extraction warnings</summary>

  - Revenue CAGR labeled as FY14–LTM (approximately 5 years), not a standard 3-year CAGR; mapped to revenue_cagr_3yr field as best available — interpret with caution.
  - No EV or EV/EBITDA multiple disclosed in teaser; ev_proposed_usd and ev_ebitda_multiple left null.
  - Entry year stated as 2014; exit anticipated September 2019 implying ~5-year hold by Atlas Crossing Partners Fund I.

  </details>

### `Exit Process Materials/Post Exit Compliance/Escrow Agreement Summary 2019-09.pdf` → `doc_cardinal_filtration_co_017` (funds_flow)
- Title: Cardinal Filtration Co. — Escrow Agreement Summary
- Date: 2019-09-20
- Summary: Post-exit escrow agreement summary for Cardinal Filtration Co. documenting a $20M indemnity holdback (3.57% of EV, implying ~$560M total EV) held by Wells Fargo Bank under the SPA between ACP Fund I (Seller) and Donaldson Company (Buyer). The 18-month escrow was funded at closing on September 20, 2019 and released in full on March 20, 2021 with $412K in accrued interest ($20.412M total), as no indemnification claims were received. An AIG R&W insurance policy ($28M limit, $1.4M premium) was bound concurrently. Governing law is Delaware with JAMS arbitration.
- deal_context (confidence=0.82): company=Cardinal Filtration Co., sector=None, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint was 'dd_report' but document content is clearly a post-exit escrow agreement summary; overridden to 'funds_flow' as the closest taxonomy match.
  - EV of ~$560M is back-calculated from the escrow amount ($20M = 3.57% of EV); not explicitly stated as a total EV figure.
  - Exit year is inferred as 2019 from the closing/funding date of September 20, 2019.
  - Exit type 'strategic_sale' is inferred from the buyer being Donaldson Company, an industrial strategic acquirer, not explicitly labeled in the document.
  - Returns extract is partially populated; IRR, MOIC, entry EV, and holding period are not available in this document.

  </details>

### `Exit Process Materials/Post Exit Compliance/Escrow Release Notice 2021-03.pdf` → `doc_cardinal_filtration_co_018` (funds_flow)
- Title: Escrow Release Notice — Cardinal Filtration Co.
- Date: 2021-03-20
- Summary: Atlas Crossing Partners Fund I, L.P. escrow release notice confirming the full release of the $20M indemnity escrow established at the September 2019 sale of Cardinal Filtration Co. to Donaldson Company, Inc. No claims were paid; accrued interest of $412K was credited to sellers, resulting in a total escrow release of $20,412,000. The notice also summarizes final realized returns for the investment: $69M invested capital, $31M 2017 dividend recapitalization, $170M net exit proceeds, and $20.4M escrow release, yielding a total of $221.4M cumulative proceeds, a 3.21x gross MOIC, and ~26.2% gross IRR. Described as the highest absolute-return deal in Fund I history.
- deal_context (confidence=0.82): company=Cardinal Filtration Co., sector=manufacturing, subsector=process_manufacturing
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint was dd_report, but document is clearly a post-exit escrow release / LP notice with realized returns summary — classified as funds_flow.
  - IRR stated as '~26.2%' (approximate); stored as 0.262.
  - Exit EV and entry EV not explicitly stated in the document; only net exit proceeds ($170M) and total invested capital ($69M) are disclosed — entry_ev_usd and exit_ev_usd left null.
  - Holding period not explicitly stated; entry year not directly disclosed (only 2019 exit and 2017 dividend recap mentioned).
  - Subsector 'process_manufacturing' selected under manufacturing as best fit for a filtration company; a more precise subsector (e.g., industrial_filtration) is not in the taxonomy — see taxonomy_proposals.

  </details>

### `Exit Process Materials/Post Exit Compliance/GP-LP Distribution Notice 2019-09.pdf` → `doc_cardinal_filtration_co_019` (funds_flow)
- Title: Limited Partner Distribution Notice — Cardinal Filtration Co. Exit
- Date: 2019-09-23
- Summary: Atlas Crossing Partners Fund I, L.P. distribution notice to LPs announcing the completed sale of Cardinal Filtration Co. to Donaldson Company, Inc. (NYSE: DCI) for $560M EV. The notice details gross/net MOIC and IRR, a breakdown of LP distributions (including 2017 dividend recap, return of capital, preferred return, and residual carry), a $20M escrow holdback expected to release March 2021, and net LP distributions of ~$302.8M wired September 27, 2019. Gross MOIC was 3.2x and gross IRR was ~26.1% over a ~5.3-year hold period.
- deal_context (confidence=0.92): company=Cardinal Filtration Co., sector=manufacturing, subsector=process_manufacturing
- <details><summary>⚠ extraction warnings</summary>

  - Folder-based doc_type hint was 'dd_report' but content is clearly a GP-LP distribution/funds flow notice; overriding to 'funds_flow'.
  - IRR stored as decimal (0.261) representing ~26.1%; holding_period_years rounded to 5 from stated 5.3 years.
  - Entry EV not explicitly stated in this document; total invested capital was $69M but this reflects equity, not EV.
  - Subsector 'process_manufacturing' selected for industrial filtration manufacturing — a taxonomy_proposals entry has been added.
  - Gross MOIC 3.2x used in returns_extract; net MOIC 2.6x and net IRR 21.2% are also present but only gross figures placed in returns_extract per convention.

  </details>

### `Exit Process Materials/Post Exit Compliance/Indemnity Holdback Tracker.xlsx` → `doc_cardinal_filtration_co_020` (funds_flow)
- Title: Cardinal Filtration Co. — Indemnity Escrow Tracker
- Date: 2021-03-20
- Summary: Post-exit indemnity escrow tracker for Cardinal Filtration Co. (ACP Fund I). A $20M escrow was funded at closing on Sep 20, 2019 per SPA §9.2, held with Wells Fargo Bank N.A. One informal claim (Claim-01, raised by Donaldson for a pre-close customer contract dispute) was filed in Aug 2020 but withdrawn in Oct 2020 as it fell below the $2.8M basket threshold. No other claims were made. The escrow period expired after 18 months on Mar 20, 2021, and the full balance of $20.41M (including ~$412K in accrued interest) was released and wired to ACP Fund I's distribution account.
- deal_context (confidence=0.75): company=Cardinal Filtration Co., sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint was 'dd_report' but content is a post-exit indemnity escrow tracker workbook; classified as 'funds_flow' as the closest matching doc_type.
  - Subsector 'industrial_components' selected under 'manufacturing' as best available proxy — Cardinal Filtration Co. is a filtration/industrial products company; no dedicated filtration subsector exists in taxonomy.
  - returns_extract populated with exit_year=2019 (closing/escrow-funded date) but entry EV, exit EV, IRR, and MOIC are not present in this document.
  - Escrow release amount of $20.41M is a holdback return to ACP Fund I, not the full exit proceeds — total exit EV cannot be inferred from this document alone.

  </details>

## Resolver disagreements

### sector
- Chosen: `industrial_distribution` (plurality 8/10)
- Voters for chosen: ['Deal Performance/Final_Returns_Summary_2019-09.xlsx', 'Deal Performance/IC_Memo_Entry_2014-04.pdf', 'Deal Performance/IC_Memo_Exit_2019-08.pdf', 'Exit Process Materials/Bids/IOI Tracker 2019-06.xlsx', 'Exit Process Materials/Bids/Management Presentation — Buyer Shortlist 2019-06.pdf', 'Exit Process Materials/Closing Execution/HSR Filing Summary 2019-08.pdf', 'Exit Process Materials/Marketing/CIM — Cardinal Filtration Co. 2019-05.pdf', 'Exit Process Materials/Marketing/Teaser — Baird 2019-04.pdf']
- Dissent `manufacturing`: ['Exit Process Materials/Closing Execution/Closing Checklist 2019-09.xlsx', 'Exit Process Materials/Post Exit Compliance/GP-LP Distribution Notice 2019-09.pdf']

### subsector
- Chosen: `specialty_distribution` (plurality 8/10)
- Voters for chosen: ['Deal Performance/Final_Returns_Summary_2019-09.xlsx', 'Deal Performance/IC_Memo_Entry_2014-04.pdf', 'Deal Performance/IC_Memo_Exit_2019-08.pdf', 'Exit Process Materials/Bids/IOI Tracker 2019-06.xlsx', 'Exit Process Materials/Bids/Management Presentation — Buyer Shortlist 2019-06.pdf', 'Exit Process Materials/Closing Execution/HSR Filing Summary 2019-08.pdf', 'Exit Process Materials/Marketing/CIM — Cardinal Filtration Co. 2019-05.pdf', 'Exit Process Materials/Marketing/Teaser — Baird 2019-04.pdf']
- Dissent `industrial_components`: ['Exit Process Materials/Closing Execution/Closing Checklist 2019-09.xlsx']
- Dissent `process_manufacturing`: ['Exit Process Materials/Post Exit Compliance/GP-LP Distribution Notice 2019-09.pdf']

### geography
- Chosen: `national` (plurality 7/8)
- Voters for chosen: ['Deal Performance/Final_Returns_Summary_2019-09.xlsx', 'Deal Performance/IC_Memo_Exit_2019-08.pdf', 'Exit Process Materials/Bids/Management Presentation — Buyer Shortlist 2019-06.pdf', 'Exit Process Materials/Closing Execution/HSR Filing Summary 2019-08.pdf', 'Exit Process Materials/Marketing/CIM — Cardinal Filtration Co. 2019-05.pdf', 'Exit Process Materials/Marketing/Teaser — Baird 2019-04.pdf', 'Exit Process Materials/Post Exit Compliance/GP-LP Distribution Notice 2019-09.pdf']
- Dissent `midwest_us`: ['Deal Performance/IC_Memo_Entry_2014-04.pdf']

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- geography: proposed=`midwest_us_multiregional` (used `midwest_us`, confidence=0.72)
  - rationale: Cardinal is headquartered in Akron, OH (Midwest) but operates 4 distribution centers across Akron, Memphis, Dallas, and Phoenix, serving 18 states. The deal is effectively national in footprint but headquartered in the Midwest. 'national' could also apply, but the HQ and primary operations are Midwest-centric, so midwest_us is used as the closest match.
- subsector: proposed=`filtration_components` (used `industrial_components`, confidence=0.65)
  - rationale: Cardinal Filtration Co. appears to be a filtration products manufacturer. The taxonomy lacks a filtration-specific subsector under manufacturing; industrial_components is the closest available match.
- doc_type: proposed=`closing_checklist` (used `funds_flow`, confidence=0.75)
  - rationale: This document is a closing checklist that tracks M&A execution steps and includes funds flow wire details. 'funds_flow' is the closest existing type, but a dedicated 'closing_checklist' doc_type would better capture this category of closing execution document.
- subsector: proposed=`filtration_products` (used `industrial_components`, confidence=0.8)
  - rationale: Cardinal Filtration Co. is a filtration company sold to Donaldson (a major filtration/separation products manufacturer). 'filtration_products' would be the ideal subsector under manufacturing, but it does not exist in the taxonomy. 'industrial_components' is the closest available option.
- doc_type: proposed=`regulatory_filing_summary` (used `dd_report`, confidence=0.88)
  - rationale: This document is an HSR antitrust filing summary prepared by outside counsel (Kirkland & Ellis), documenting the Hart-Scott-Rodino filing process, timeline, and competition analysis. It is a regulatory/legal closing execution document, not a due diligence report. No existing doc_type in the taxonomy covers regulatory filing summaries.
- doc_type: proposed=`vdr_index` (used `dd_report`, confidence=0.85)
  - rationale: This document is a Virtual Data Room index/table of contents, not a due diligence report itself. It catalogues the contents of the data room but contains no analytical findings. A dedicated 'vdr_index' doc type would be more precise; mapping to dd_report as closest existing.
- subsector: proposed=`filtration_manufacturing` (used `process_manufacturing`, confidence=0.62)
  - rationale: Cardinal Filtration Co. manufactures filtration products including a proprietary private-label line (CardinalGuard). 'process_manufacturing' is the closest available subsector under 'manufacturing', though 'filtration_manufacturing' or 'industrial_components' could also apply. 'process_manufacturing' is selected as the best fit.
- deal_type: proposed=`exit_sale` (used `platform`, confidence=0.6)
  - rationale: This document governs an exit/sale process by a PE fund (Atlas Crossing Partners Fund I) selling Cardinal Filtration Co. None of the deal_type values directly represent a sell-side exit; 'platform' is the closest as Cardinal is presumed to have been the fund's platform company.
- thesis_theme: proposed=`private_label_expansion` (used `premiumization`, confidence=0.72)
  - rationale: The document heavily emphasizes private-label penetration growth from 9% to 28% as a core value creation lever. 'premiumization' is the closest existing theme but does not fully capture the private-label margin expansion dynamic common in distribution businesses.
- doc_type: proposed=`escrow_agreement_summary` (used `funds_flow`, confidence=0.6)
  - rationale: This document is a post-closing escrow and indemnification summary, which is a post-exit compliance document type not captured by any existing taxonomy value. 'funds_flow' is the closest match as it relates to capital movement and closing mechanics, but a dedicated 'escrow_agreement_summary' or 'post_closing_compliance' type would better describe this document.
- doc_type: proposed=`escrow_release_notice` (used `funds_flow`, confidence=0.75)
  - rationale: This document is a post-closing escrow release notice to LPs, distinct from a funds flow at closing but closest to funds_flow among available types. A dedicated 'escrow_release_notice' or 'lp_notice' type would better capture this category.
- subsector: proposed=`industrial_filtration` (used `process_manufacturing`, confidence=0.72)
  - rationale: Cardinal Filtration Co. is an industrial filtration manufacturer, which fits better under a dedicated 'industrial_filtration' subsector. 'process_manufacturing' is the closest available option under 'manufacturing'.
- doc_type: proposed=`indemnity_escrow_tracker` (used `funds_flow`, confidence=0.72)
  - rationale: This document tracks post-closing indemnity escrow events, claims, and the final escrow release — it is a post-exit compliance/legal instrument, distinct from a traditional funds flow statement but most analogous to funds_flow given the cash movement tracking.
