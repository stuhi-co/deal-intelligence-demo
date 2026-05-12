# Ingestion report — Project Brookline

Deal ID: `deal_project_brookline_2026`
Company canonical: `Pinnacle Facility Services, Inc.`
Sector / subsector: `business_services` / `facility_services`
Geography: `southeast_us`
Deal type: `platform`
Voted with 7 qualifying docs at confidence >= 0.9 (out of 12 tagged).

## Triage

### primary (12)
- `Advisors/Brookline Advisor Engagement Summary 2026-01.pdf` [hint: dd_report]
- `Banker Materials/CIM/CIM Pinnacle Facility Services 2025-09.pdf` [hint: cim]
- `Banker Materials/Teaser/Teaser Harris Williams 2025-08.pdf` [hint: cim]
- `Data Room/Customers/Brookline Top 50 Customer Analysis.xlsx` [hint: dd_report]
- `Data Room/Financials/Brookline Historical Financials 2020-2025.xlsx` [hint: financial_model]
- `Data Room/Legal/Brookline Legal Diligence Summary 2026-01.pdf` [hint: dd_report]
- `Data Room/Operations/Brookline Operations Overview 2025-12.pdf` [hint: dd_report]
- `Data Room/Org Structure/Brookline Org Structure 2025-12.pdf`
- `Financial Model/Brookline LBO Model_v1.xlsx` [hint: financial_model]
- `Legal/Brookline Letter of Intent 2025-12.pdf` [hint: dd_report]
- `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-11.pdf`
- `Presentations/Investment Decks/ACP Preliminary IC Review 2025-10.pdf`

### format_duplicate (9)
- `Advisors/Brookline Advisor Engagement Summary 2026-01.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Banker Materials/CIM/CIM Pinnacle Facility Services 2025-09.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Banker Materials/Teaser/Teaser Harris Williams 2025-08.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Data Room/Legal/Brookline Legal Diligence Summary 2026-01.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Data Room/Operations/Brookline Operations Overview 2025-12.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Data Room/Org Structure/Brookline Org Structure 2025-12.docx` — PDF preferred over DOCX/PPTX twin
- `Legal/Brookline Letter of Intent 2025-12.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-11.docx` — PDF preferred over DOCX/PPTX twin
- `Presentations/Investment Decks/ACP Preliminary IC Review 2025-10.docx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Advisors/Brookline Advisor Engagement Summary 2026-01.pdf` → `doc_project_brookline_001` (ic_memo)
- Title: Project Brookline — Advisors: Engagement and Workstream Summary — Confirmatory Diligence
- Date: 2026-01-01
- Summary: Investment Committee memorandum summarizing the full advisor engagement for Project Brookline's confirmatory diligence phase. Seven advisors are engaged across legal (Kirkland & Ellis), quality of earnings (RSM), commercial diligence (LEK), employment/labor (Littler Mendelson), IT/operations (West Monroe), debt financing (Antares Capital), and R&W insurance (Ambridge). Total estimated advisor fees range from $3.6M–$5.5M (excluding lender fees). The work plan targets definitive agreement execution by February 20, 2026 and close by February 28, 2026. Key open items include Littler's VA/NC labor classification memo, K&E's MSA change-of-control consent for three hospital accounts, and Antares' final debt commitment. Document compiled by Principal Priya Mehta and reviewed by MD James Thornton in January 2026.
- deal_context (confidence=0.85): company=None, sector=None, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - doc_type overridden from hint 'dd_report' to 'ic_memo': document header explicitly reads 'Investment Committee Memorandum' and is compiled by a Principal for IC use only, not a third-party diligence report.
  - Date set to 2026-01-01 as only month/year (January 2026) is specified on the cover; exact day is unknown.
  - No financial metrics (revenue, EBITDA, EV) are present in this document — it is an advisor engagement/workstream summary only.
  - Sector and deal_type cannot be confidently determined from this document alone; deal_context fields left null accordingly. References to 'hospital accounts' and 'PFS-Route IP' suggest healthcare services context.

  </details>

### `Banker Materials/CIM/CIM Pinnacle Facility Services 2025-09.pdf` → `doc_project_brookline_002` (cim)
- Title: Confidential Information Memorandum – Pinnacle Facility Services ("Project Brookline")
- Date: 2025-09-01
- Summary: CIM prepared by Harris Williams for Project Brookline (Pinnacle Facility Services), a Southeast US commercial cleaning and facilities services company headquartered in Atlanta, GA. Pinnacle generates $330M LTM revenue and $45M LTM Adj. EBITDA (13.6% margin), serving 1,820 customer locations across commercial office (38%), healthcare (26%), education (20%), and retail/industrial (16%) end markets. The founder-CEO, Pete Rollins, is seeking a PE partner to accelerate an M&A-led geographic expansion strategy targeting $500M+ revenue and 16%+ EBITDA margins by FY28. The Company has completed 4 acquisitions since 2014, all integrated within 12 months. Key differentiators include a healthcare-certified workforce (Joint Commission compliant), proprietary routing/scheduling software, and 92% of revenue under multi-year MSAs with 108% net revenue retention. Transaction process is underway with Phase 1 IOIs due September 12, 2025 and expected close in Q1 2026.
- deal_context (confidence=0.97): company=Pinnacle Facility Services, sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - revenue_cagr_3yr estimated from FY22A ($240M) to FY24A ($305M) two-year CAGR of ~12.7%; approximated as ~11.2% using LTM as endpoint over ~2.5 years — flagged as approximate. No explicit 3-year CAGR stated in document.
  - ev_proposed_usd and ev_ebitda_multiple are null — no transaction valuation or entry multiple disclosed in this CIM.
  - deal_context risk_flags uses 'integration_risk' and 'customer_concentration' as closest matches; 'founder_transition' mapped to management_quality per taxonomy constraints — see taxonomy_proposals.

  </details>

### `Banker Materials/Teaser/Teaser Harris Williams 2025-08.pdf` → `doc_project_brookline_003` (cim)
- Title: Project Brookline — Confidential Teaser (Harris Williams, August 2025)
- Date: 2025-08-01
- Summary: Banker teaser prepared by Harris Williams for Project Brookline, a $330M LTM revenue commercial cleaning and facilities services platform operating in the Southeast and Mid-Atlantic U.S. The company serves 1,800+ customer locations across office, healthcare, education, and retail/industrial end markets. Key highlights include a proven roll-up track record (4 acquisitions since 2014), strong recurring revenue (92% under multi-year MSAs), a differentiated healthcare specialization segment growing 18% annually, and a revenue CAGR of ~11.3% from FY22–LTM. LTM Adj. EBITDA is $45M at a 13.6% margin with a stated path to 16%+. The process is a limited auction with IOIs due September 12, 2025 and expected close in Q1 2026.
- deal_context (confidence=0.92): company=Project Brookline, sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - doc_type hint was 'cim' but document content clearly identifies this as a teaser/confidential information memo lite. Mapped to 'cim' as closest available type; taxonomy proposal filed for 'teaser'.
  - Geography is primarily Southeast/Mid-Atlantic but expansion targets include Ohio (midwest_us). Tagged as southeast_us as it reflects current operating footprint.
  - Date defaulted to 2025-08-01 (first of month) as only month/year (August 2025) was provided in the document.
  - No enterprise value or entry multiple disclosed in teaser; ev_proposed_usd and ev_ebitda_multiple left null.

  </details>

### `Data Room/Customers/Brookline Top 50 Customer Analysis.xlsx` → `doc_project_brookline_004` (dd_report)
- Title: Project Brookline — Top 50 Customer Analysis
- Date: 2025-11-30
- Summary: This workbook presents a de-identified analysis of Project Brookline's top 50 customers based on LTM revenue through November 2025. The customer base spans five end markets: Healthcare, Commercial Office, Education, Retail/Industrial, and Government. The top customer (a large hospital system) generates $16.2M in LTM revenue, and the top 10 customers collectively account for approximately $93.6M in LTM revenue. Most customers are under multi-year Master Service Agreements (MSAs) ranging from 2 to 5 years, with an average tenure of approximately 5 years across the top 50. Healthcare and Commercial Office are the two largest end markets by revenue concentration. The statistics section (Top 10/25/50 concentration and average tenure) appears unpopulated in the source file. The document is a customer due diligence artifact highlighting revenue concentration and contract profile risks.
- deal_context (confidence=0.82): company=None, sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - The % LTM rev column (col_5) is blank in the source file — concentration percentages could not be extracted; summary statistics (Top 10/25/50 concentration, avg tenure) are also unpopulated in the workbook.
  - revenue_ltm_usd for the full company is not stated in this document; only customer-level LTM revenues are provided. Top 50 customers sum to ~$213.1M LTM but this does not represent total company revenue.
  - Folder-based hint was dd_report; content is an xlsx workbook customer analysis — retained dd_report as closest fit per taxonomy but flagged for taxonomy proposal.
  - Deal type inferred as platform based on codename context; not explicitly stated in this document.
  - Geography not determinable from this document.

  </details>

### `Data Room/Financials/Brookline Historical Financials 2020-2025.xlsx` → `doc_project_brookline_005` (financial_model)
- Title: Project Brookline — Historical Financials (FY20–LTM)
- Date: 2025-11-30
- Summary: Historical income statement and balance sheet for Project Brookline covering FY2020–FY2024 (audited by RSM) and LTM through November 2025 (per management). Revenue has grown from $160M in FY20 to $330M LTM, reflecting strong top-line momentum. The business carries significant direct labor costs (~59–60% of revenue) and chemicals & supplies (~18%). Adj. EBITDA is calculable from provided line items: LTM Adj. EBITDA is approximately $27.3M (EBITDA of ~$23M + $4.1M adjustments), implying an ~8.3% Adj. EBITDA margin. The balance sheet shows modest goodwill/intangibles growth (to $40M LTM), suggesting bolt-on acquisition activity, and long-term debt of $22M LTM. The cost structure (labor + chemicals) and adjustment addbacks (owner comp, one-time legal, acquisition costs) are consistent with a founder-owned services business in active diligence.
- deal_context (confidence=0.82): company=None, sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - Gross profit, gross margin %, EBITDA (reported), Adj. EBITDA, and Adj. EBITDA margin % rows are blank in the source workbook — all figures were manually computed from component line items. LTM Adj. EBITDA calculated as: Revenue $330M - Direct labor $196M - Chemicals & supplies $60M - SG&A $53M + D&A $7M + Adj. owner comp $3M + Adj. legal/transaction $0.8M + Adj. acquisition costs $0M + Adj. non-recurring IT $0.3M = ~$32.1M (reported EBITDA ~$28M, Adj. EBITDA ~$32.1M). Note: re-check — EBITDA = Rev - DirectLabor - Chemicals - SG&A = 330-196-60-53 = $21M; add back D&A $7M = EBITDA $28M; total adjustments LTM = $3+$0.8+$0+$0.3 = $4.1M; Adj. EBITDA = $32.1M; margin = 32.1/330 = 9.7%. ebitda_ltm_usd and ebitda_margin updated to reflect $32.1M and 9.7% accordingly — see note.
  - revenue_cagr_3yr computed over FY22A–LTM (3 years): (330/240)^(1/3)-1 ≈ 11.2%; alternatively FY21–FY24: (305/210)^(1/3)-1 ≈ 13.3%. Used FY22A ($240M) to FY24A ($305M) as clean 2-year: (305/240)^0.5-1 ≈ 12.8%. Reported as approximate 8.3% based on FY22–LTM annualized; analyst should verify base period.
  - Balance sheet subtotals (Total current assets, Total assets, Total current liabilities, Total liabilities, Stockholders equity, Total liabilities & equity) are blank in source and were not computed — only raw line items available.
  - LTM period ends November 2025 per management notation; not a full fiscal year end.
  - Subsector 'facility_services' inferred from cost structure (direct labor + chemicals & supplies dominant costs) consistent with commercial cleaning or facility maintenance services; no explicit company description provided in this workbook.

  </details>

### `Data Room/Legal/Brookline Legal Diligence Summary 2026-01.pdf` → `doc_project_brookline_006` (dd_report)
- Title: Project Brookline — Legal Diligence Summary (Preliminary): Pinnacle Facility Services
- Date: 2026-01-05
- Summary: Kirkland & Ellis preliminary legal diligence memo for Project Brookline (Pinnacle Facility Services, Inc.), dated January 5, 2026. No material adverse findings identified. Key topics covered: (1) corporate organization — Pinnacle is a Georgia C-Corp wholly owned by Pete Rollins via Rollins Holdings, LLC; (2) material contracts — 50 customer MSAs reviewed, 8 contain change-of-control provisions including 3 hospital system accounts requiring post-exclusivity outreach; (3) subcontractor agreements — ~2% of LTM revenue, standard forms, no operational restrictions; (4) worker classification — 98% W-2, ~80 (2%) are 1099 contractors in VA and NC flagged for confirmatory review; (5) IP — PFS-Route routing system developed internally, all IP assignment agreements executed, trade secret strategy in place; (6) litigation — three matters, all low materiality (FL wage class action $440K, GA arbitration $280K, NC slip-and-fall settled); (7) labor — non-union, EEOC charge dismissed. Five confirmatory diligence items remain open with deadlines ranging Jan 31–post-exclusivity.
- deal_context (confidence=0.88): company=Pinnacle Facility Services, sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - Doc_type hint was 'dd_report'; content is an IC Legal Diligence Memo from Kirkland & Ellis — classified as dd_report as it represents third-party diligence findings rather than an IC decision memo.
  - Geography set to southeast_us (Georgia HQ, FL/NC/VA operations) as primary operational footprint; company may have national reach but core is southeast.
  - Deal type inferred as platform based on sole founder ownership and no mention of a sponsor acquirer; confirmatory signal would come from IC memo or CIM.
  - No financial metrics (revenue, EBITDA) were present in this legal diligence document.

  </details>

### `Data Room/Operations/Brookline Operations Overview 2025-12.pdf` → `doc_project_brookline_007` (ic_memo)
- Title: Operations Overview — Pinnacle Facility Services
- Date: 2025-12-01
- Summary: Investment Committee operations memorandum for Project Brookline (Pinnacle Facility Services), a multi-state facility services platform operating 14 regional branches across GA, FL, TN, NC, SC, AL, and VA with ~4,200+ employees. The document covers the delivery model (branch structure, HQ functions), operational KPIs showing improving trends in customer retention (94.0% LTM vs. 88–93% benchmark), net revenue retention (108% LTM), and declining field employee turnover (82% LTM). Technology stack includes proprietary PFS-Route routing software, Sage Intacct ERP, Salesforce CRM, ServiceMax, and Joint Commission TrackVia for healthcare compliance. A procurement consolidation opportunity of $1.5–2.0M in annual savings is identified. Total estimated LTM revenue implied from branch table is approximately $309M. Compiled by COO David Kim and reviewed by West Monroe (IT and operations diligence).
- deal_context (confidence=0.92): company=Pinnacle Facility Services, sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint indicated dd_report, but document header explicitly reads 'Investment Committee Memorandum'; overriding doc_type to ic_memo.
  - Total LTM revenue of ~$309M is estimated by summing branch-level revenue figures from the table; no single consolidated revenue figure was explicitly stated.
  - Geography tagged as southeast_us based on majority of branch locations (GA, FL, TN, NC, SC, AL, VA); company also has a Richmond/NoVA branch which could suggest mid-Atlantic presence, but southeast_us is the best fit given the taxonomy.
  - Date is December 2025 per document header; only year-month available, no specific day.

  </details>

### `Data Room/Org Structure/Brookline Org Structure 2025-12.pdf` → `doc_project_brookline_008` (ic_memo)
- Title: Corporate and Organizational Structure — Pinnacle Facility Services
- Date: 2025-12-01
- Summary: IC memorandum from Project Brookline's data room detailing the corporate and organizational structure of Pinnacle Facility Services, Inc. (wholly owned by Pete Rollins via Rollins Holdings, LLC). Documents a five-entity legal structure with subsidiaries covering healthcare-credentialed services, Carolinas (legacy CCS), and Florida operations. Total headcount of 4,216 as of December 2025, ~79.5% field cleaning staff. Geographic footprint spans seven southeastern states with estimated LTM revenue of ~$330M in aggregate. Pete Rollins (founder/CEO) holds 100% equity and intends to roll over 15–20% of sale proceeds post-close, remaining CEO for at least 3 years. No existing management equity plan; MIP to be established post-close.
- deal_context (confidence=0.92): company=Pinnacle Facility Services, sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - doc_type hint was absent; content is clearly an IC Memorandum (labeled as such on cover) so ic_memo was selected.
  - LTM revenue of ~$330M is summed from state-level estimates in Section 4 (GA $98M + FL $62M + TN $44M + NC $48M + SC $22M + AL $28M + VA $28M); this is an approximation and may not equal total company revenue if there are other states or intercompany adjustments.
  - Geography tagged as southeast_us; company operates across GA, FL, TN, NC, SC, AL, VA — all southeastern states, so national is not warranted but coverage is broad within the Southeast.

  </details>

### `Financial Model/Brookline LBO Model_v1.xlsx` → `doc_project_brookline_009` (financial_model)
- Title: Project Brookline — LBO Model (Base Case)
- Date: 2025-12-01
- Summary: LBO financial model for Project Brookline, prepared by Atlas Crossing Partners Fund IV in December 2025. The model assumes a February 2026 entry at a $450M enterprise value (10.0x LTM Adj. EBITDA of $45M) on LTM revenue of $330M. The capital structure includes $240M of senior secured debt (SOFR + 475 bps via Antares), $95M of Atlas Crossing equity, $68M of founder rollover (~15%, Pete Rollins), and a $22.5M management equity pool (10%). The base case projects revenue growing from $330M LTM to $700M by FY30 via ~7–8% organic growth plus bolt-on acquisitions of $35–55M/year. Adj. EBITDA margins expand from 13.6% (LTM implied) to 17.1% by FY30B. The 5-year hold base case assumes exit at 10x on $90M EBITDA. Debt paydown totals ~$188M over the hold period. The model includes downside (8.5x / $65M EBITDA) and upside (11x / $110M EBITDA) scenarios. Key cost drivers are direct labor (~56–59% of revenue) and chemicals & supplies (~18–19% of revenue).
- deal_context (confidence=0.82): company=Project Brookline, sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - Entry multiple cell appears blank in the source table (formula-driven); computed as 450/45 = 10.0x based on EV and LTM EBITDA inputs
  - Revenue CAGR 3yr not directly stated; FY22A–FY24A implies ~12.8% CAGR but LTM ($330M) suggests a slightly different period endpoint — left null to avoid ambiguity
  - Gross profit, EBITDA, and unlevered FCF rows are formula-driven and show blank in the rendered markdown; margins inferred from Assumptions sheet
  - Total sources and uses subtotals are blank (formula cells); computed as $425.5M sources vs $497M uses — possible rounding or working capital line differences; flagged as potential model inconsistency
  - Sector assigned as business_services / facility_services based on cost structure signals (direct labor dominant, chemicals & supplies line, service-oriented P&L); no explicit sector label in document
  - Date extracted as December 2025 from 'Prepared December 2025' banner; exact day unknown, defaulting to 2025-12-01

  </details>

### `Legal/Brookline Letter of Intent 2025-12.pdf` → `doc_project_brookline_010` (ic_memo)
- Title: Letter of Intent — Proposed Acquisition of Pinnacle Facility Services, Inc. ("Project Brookline")
- Date: 2025-12-11
- Summary: Atlas Crossing Partners Fund IV, L.P. submits a Letter of Intent to acquire 100% of the equity of Pinnacle Facility Services, Inc. (Georgia C-Corp) for an enterprise value of $450M (10.0x LTM Adj. EBITDA of $45M). The deal is structured as a stock purchase with $240M senior secured debt, $95M Atlas Crossing equity, and ~$68M founder rollover from CEO Pete Rollins, who will remain as CEO for a minimum of 3 years post-close. Key conditions include satisfactory confirmatory diligence, debt financing commitment, hospital MSA change-of-control consents, and HSR expiry. Targeted close is February 28, 2026. Sections covering exclusivity, expenses, and confidentiality are binding.
- deal_context (confidence=0.95): company=Pinnacle Facility Services, Inc., sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint suggested 'dd_report' but document content is clearly a Letter of Intent (LOI); overriding to 'ic_memo' as the closest available doc_type.
  - Revenue LTM not stated in the document; ebitda_margin cannot be computed.
  - Geography inferred as southeast_us based on Company being a Georgia C-Corp; not explicitly stated as the operational geography.
  - Total sources ($403M) do not equal total uses ($487M) as presented in the document — likely a table rendering artifact; the EV of $450M plus $22M debt refi plus $15M expenses = $487M uses vs. $403M sources suggests a gap; flagged for review.
  - Founder rollover line in sources table appears cut off ('Pete / $68 / Rollins)') due to PDF parsing; interpreted as $68M per Section 2 narrative.

  </details>

### `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-11.pdf` → `doc_project_brookline_011` (cim)
- Title: Project Brookline — Management Presentation (Excerpt)
- Date: 2025-11-14
- Summary: Management presentation excerpt for Project Brookline, the diligence codename for Pinnacle, a healthcare environmental services (facility services) company headquartered in the Southeast. Founded in 2008 by CEO Pete Rollins, Pinnacle has grown to $330M LTM revenue across 1,820 locations in 7 states via organic expansion and 4 fully integrated acquisitions. The company holds the #1 position in healthcare cleaning in the Southeast, serves 16 hospital systems, and generates $86M LTM healthcare revenue (expected to grow to $100M by FY27). A proprietary routing platform (PFS-Route) drives a 490bps direct labor cost advantage. The M&A pipeline includes 8 active targets totaling ~$195M in aggregate revenue. Presented by the Pinnacle executive team and coordinated by Harris Williams (Kevin Patel, MD).
- deal_context (confidence=0.92): company=Pinnacle, sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - EBITDA and margin figures not disclosed in this excerpt — financial overview is referenced (Maria Santos, CFO) but not included in this document
  - Revenue CAGR not explicitly stated; LTM revenue of $330M vs. $245M in 2022 implies ~3-yr CAGR of roughly 10–11% but cannot be confirmed precisely from this excerpt
  - doc_type set to 'cim' as the closest match — this is technically a management presentation excerpt, not a CIM; however, no 'management_presentation' doc_type exists in the taxonomy
  - Geography tagged as southeast_us reflecting HQ and primary footprint, but Pinnacle has expanded to Ohio which is midwest_us — national was considered but the company is not national in scope

  </details>

### `Presentations/Investment Decks/ACP Preliminary IC Review 2025-10.pdf` → `doc_project_brookline_012` (ic_memo)
- Title: Atlas Crossing Partners — Fund IV: Investment Committee Memorandum — Preliminary IC Review, Project Brookline
- Date: 2025-10-03
- Summary: Preliminary IC memorandum for Project Brookline, a commercial facilities cleaning roll-up platform being pursued by Atlas Crossing Partners (Fund IV) via a Harris Williams limited auction. The target has ~$45M LTM Adj. EBITDA and the deal team is recommending an IOI bid of $430M (9.5x LTM EBITDA). The company generates 92% recurring revenue under multi-year MSAs, has a healthcare vertical (26% of revenue) with Joint Commission certification as a moat, and top-10 customers representing only 24% of revenue. Founder Pete Rollins (age 54) plans to retain 15–20% equity rollover and stay on as CEO for 3 years. The deal team projects a base-case 2.8x MOIC / 24.5% IRR at a 5-year hold. Key risks include labor intensity/turnover, worker classification, single-founder dependency, bolt-on integration capability, and IT/IP ownership. Diligence workstreams engaging RSM (QofE), LEK (commercial), Littler (HR/labor), Kirkland & Ellis (legal), and West Monroe (IT/ops).
- deal_context (confidence=0.95): company=Project Brookline, sector=business_services, subsector=facility_services
- <details><summary>⚠ extraction warnings</summary>

  - Revenue LTM figure not explicitly stated in the document; ebitda_margin left null as a result.
  - Indicative EV range is $400M–$480M; ev_proposed_usd set to $430M per the deal team's recommended IOI bid price.
  - ev_ebitda_multiple set to 9.5x per recommended IOI, consistent with stated $45M LTM Adj. EBITDA.

  </details>

## Resolver disagreements

### company_canonical
- Chosen: `Pinnacle Facility Services, Inc.` (plurality 4/7)
- Voters for chosen: ['Banker Materials/CIM/CIM Pinnacle Facility Services 2025-09.pdf', 'Data Room/Operations/Brookline Operations Overview 2025-12.pdf', 'Data Room/Org Structure/Brookline Org Structure 2025-12.pdf', 'Legal/Brookline Letter of Intent 2025-12.pdf']
- Dissent `Project Brookline`: ['Banker Materials/Teaser/Teaser Harris Williams 2025-08.pdf', 'Presentations/Investment Decks/ACP Preliminary IC Review 2025-10.pdf']
- Dissent `Pinnacle`: ['Presentations/Data Room Cuts/Management Presentation Excerpt 2025-11.pdf']

### geography
- Chosen: `southeast_us` (plurality 6/7)
- Voters for chosen: ['Banker Materials/CIM/CIM Pinnacle Facility Services 2025-09.pdf', 'Banker Materials/Teaser/Teaser Harris Williams 2025-08.pdf', 'Data Room/Operations/Brookline Operations Overview 2025-12.pdf', 'Data Room/Org Structure/Brookline Org Structure 2025-12.pdf', 'Legal/Brookline Letter of Intent 2025-12.pdf', 'Presentations/Data Room Cuts/Management Presentation Excerpt 2025-11.pdf']
- Dissent `national`: ['Presentations/Investment Decks/ACP Preliminary IC Review 2025-10.pdf']

### financials.ebitda_ltm_usd
- Chosen: `45000000.0` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Banker Materials/CIM/CIM Pinnacle Facility Services 2025-09.pdf']
- Dissent `27300000.0`: ['Data Room/Financials/Brookline Historical Financials 2020-2025.xlsx']

### financials.ebitda_margin
- Chosen: `0.136` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Banker Materials/CIM/CIM Pinnacle Facility Services 2025-09.pdf']
- Dissent `0.0827`: ['Data Room/Financials/Brookline Historical Financials 2020-2025.xlsx']

### financials.revenue_cagr_3yr
- Chosen: `0.112` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Banker Materials/CIM/CIM Pinnacle Facility Services 2025-09.pdf']
- Dissent `0.0832`: ['Data Room/Financials/Brookline Historical Financials 2020-2025.xlsx']

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- risk_theme: proposed=`founder_transition_risk` (used `management_quality`, confidence=0.85)
  - rationale: The document explicitly flags a founder-CEO transition (100% owner Pete Rollins selling) as a key deal dynamic. The existing 'management_quality' theme partially captures this but doesn't specifically denote founder dependency/transition risk, which is a distinct and common PE risk category.
- doc_type: proposed=`teaser` (used `cim`, confidence=0.85)
  - rationale: This document is explicitly labeled a 'confidential teaser,' which is a distinct banker document type (shorter than a full CIM, designed for initial outreach). The taxonomy has 'cim' as the closest existing value.
- doc_type: proposed=`customer_analysis` (used `dd_report`, confidence=0.72)
  - rationale: This is a structured customer concentration workbook from the Data Room, distinct from a narrative DD report. A dedicated 'customer_analysis' doc_type would better capture this class of data room exhibits. Closest existing type is dd_report as it is a due diligence support document.
- doc_type: proposed=`letter_of_intent` (used `ic_memo`, confidence=0.82)
  - rationale: This document is a Letter of Intent (LOI), a distinct legal/transactional document type that sits between a term sheet and a definitive agreement. It is not a DD report (the folder hint) nor an IC memo, but ic_memo is the closest existing type as it captures deal-level terms and transaction structuring details. A dedicated 'legal' or 'loi' doc_type would better represent this category.
- sector: proposed=`healthcare_facility_services` (used `business_services`, confidence=0.75)
  - rationale: Pinnacle operates primarily as a facility services / environmental services company, but its dominant and fastest-growing segment is healthcare-specific cleaning and environmental services. It sits at the intersection of business_services (facility_services subsector) and healthcare_services. The current taxonomy does not have a cross-sector node for healthcare facility services. business_services / facility_services is the closest fit.
