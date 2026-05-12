# Ingestion report — Project Driftwood

Deal ID: `deal_project_driftwood_2026`
Company canonical: `BlueCrest Marine Holdings, Inc.`
Sector / subsector: `manufacturing` / `industrial_components`
Geography: `national`
Deal type: `platform`
Voted with 5 qualifying docs at confidence >= 0.9 (out of 12 tagged).

## Triage

### primary (12)
- `Advisors/Driftwood Advisor Engagement Summary 2025-12.pdf` [hint: dd_report]
- `Banker Materials/CIM/CIM BlueCrest Marine Holdings 2025-08.pdf` [hint: cim]
- `Banker Materials/Teaser/Teaser Baird 2025-07.pdf` [hint: cim]
- `Data Room/Customers/Driftwood Top 50 Customer Analysis.xlsx` [hint: dd_report]
- `Data Room/Financials/Driftwood Historical Financials 2020-2025.xlsx` [hint: financial_model]
- `Data Room/Legal/Driftwood QofE Summary 2025-12.pdf` [hint: dd_report]
- `Data Room/Operations/Driftwood Operations Overview 2025-11.pdf` [hint: dd_report]
- `Data Room/Org Structure/Driftwood Org Structure 2025-11.pdf`
- `Financial Model/Driftwood LBO Model_v1.xlsx` [hint: financial_model]
- `Legal/Driftwood Draft LOI 2026-01.pdf` [hint: dd_report]
- `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-10.pdf`
- `Presentations/Investment Decks/ACP Preliminary IC Review 2025-09.pdf`

### format_duplicate (9)
- `Advisors/Driftwood Advisor Engagement Summary 2025-12.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Banker Materials/CIM/CIM BlueCrest Marine Holdings 2025-08.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Banker Materials/Teaser/Teaser Baird 2025-07.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Data Room/Legal/Driftwood QofE Summary 2025-12.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Data Room/Operations/Driftwood Operations Overview 2025-11.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Data Room/Org Structure/Driftwood Org Structure 2025-11.docx` — PDF preferred over DOCX/PPTX twin
- `Legal/Driftwood Draft LOI 2026-01.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-10.docx` — PDF preferred over DOCX/PPTX twin
- `Presentations/Investment Decks/ACP Preliminary IC Review 2025-09.docx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Advisors/Driftwood Advisor Engagement Summary 2025-12.pdf` → `doc_project_driftwood_001` (ic_memo)
- Title: Project Driftwood — Advisors: Engagement and Workstream Summary — Confirmatory Diligence
- Date: 2025-12-01
- Summary: Investment Committee memorandum summarizing all engaged advisors and key milestones for Project Driftwood's confirmatory diligence phase. Seven advisors are active across workstreams including legal (Kirkland & Ellis), Quality of Earnings (Deloitte), commercial diligence (LEK Consulting), IT/ERP (West Monroe), tax structuring (KPMG), debt financing (Antares Capital), and R&W insurance (Aon). Key open items include OEM consent outreach for four agreements, Fort Lauderdale property resolution, and final LOI execution. Target close is March 31, 2026. Compiled by Elena Rodriguez (Principal) and reviewed by James Thornton (MD).
- deal_context (confidence=0.82): company=None, sector=None, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint was 'dd_report' but content is clearly an Investment Committee memorandum summarizing advisor engagements — classified as 'ic_memo' instead.
  - Date defaulted to 2025-12-01 (month-level precision only; no specific day stated in document).
  - No financial metrics (revenue, EBITDA, EV) present in this document — structured financials are all null.
  - Sector and deal_type cannot be determined from this document alone; deal_context fields left null accordingly.

  </details>

### `Banker Materials/CIM/CIM BlueCrest Marine Holdings 2025-08.pdf` → `doc_project_driftwood_002` (cim)
- Title: Confidential Information Memorandum – BlueCrest Marine Holdings, Inc. ("Project Driftwood")
- Date: 2025-08-01
- Summary: BlueCrest Marine Holdings, Inc. is the leading independent manufacturer and distributor of marine hardware and accessories in North America, with $420M LTM revenue and $56M LTM Adj. EBITDA (13.3% margin). Founded in 1978 and headquartered in Fort Lauderdale, FL, the company serves 800+ customers across OEM (65%), specialty retail (29%), and DTC/Amazon (6%) channels, with 2,800+ active SKUs across 14 product categories. The Halverson family (2nd generation ownership) is seeking a sale for liquidity and to pursue institutional-capital-backed growth. Key investment highlights include: #1/#2 market share in 8 of 14 categories, blue-chip OEM relationships averaging 18-year tenure, 22% YoY branded retail growth, significant DTC upside ($35–50M accessible), and $8–12M EBITDA improvement opportunity from ERP/procurement modernization. Revenue CAGR from FY22–LTM is ~7.3%. The process is managed by Baird Industrial & Services, with Phase 1 IOIs due August 2025 and expected close in Q2 2026.
- deal_context (confidence=0.97): company=BlueCrest Marine Holdings, Inc., sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - No enterprise value or EV/EBITDA multiple is stated in the CIM; ev_proposed_usd and ev_ebitda_multiple left null.
  - Revenue CAGR calculated manually from FY22A ($340M) to LTM ($420M) over ~2.5 years, approximated as 3-year CAGR (~7.3%); exact fiscal year end dates not specified.
  - Geography tagged as southeast_us based on HQ and primary manufacturing in Fort Lauderdale and Tampa, FL; company has national OEM/retail reach but operations are Florida-concentrated.
  - CFO Karen Halverson's dual role (company CFO + family office) flagged as management_quality risk; not explicitly listed as a risk in the CIM.

  </details>

### `Banker Materials/Teaser/Teaser Baird 2025-07.pdf` → `doc_project_driftwood_003` (cim)
- Title: Project Driftwood — Confidential Teaser (Baird Industrial & Services, July 2025)
- Date: 2025-07-01
- Summary: Confidential sell-side teaser prepared by Baird Industrial & Services for Project Driftwood, the codename for BlueCrest Marine Holdings — the largest independent manufacturer and distributor of marine hardware and accessories in North America. The company generates $420M LTM revenue and $56M LTM Adj. EBITDA (13.3% margin), with ~65% of revenue from long-term OEM relationships with top boat builders. The business is founder-owned (2nd generation, Steve Halverson), has no prior PE sponsorship, and presents meaningful operational upside via ERP modernization, procurement consolidation, and DTC channel build-out. The teaser outlines a structured sale process targeting LOI/final bids in January 2026 and expected close in Q2 2026.
- deal_context (confidence=0.95): company=BlueCrest Marine Holdings, sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - Doc_type hint was 'cim' but this document is technically a teaser (shorter, earlier-stage than a full CIM). Retained 'cim' as the closest matching doc_type since no 'teaser' value exists in the taxonomy. Revenue CAGR (3yr) estimated from FY22A–LTM: ($420M / $340M)^(1/3) – 1 ≈ 7.3%; LTM period is partial-year so this is approximate. EV/entry multiple not disclosed in teaser; ev_proposed_usd and ev_ebitda_multiple left null.

  </details>

### `Data Room/Customers/Driftwood Top 50 Customer Analysis.xlsx` → `doc_project_driftwood_004` (dd_report)
- Title: Project Driftwood — Top 50 Customer Analysis
- Date: 2025-09-30
- Summary: This workbook provides a ranked analysis of Project Driftwood's top 50 customers by LTM revenue through September 2025, covering both OEM accounts and aftermarket/dealer customers. The top 50 customers span marine OEM manufacturers (outboard, inboard, pontoon, electric/hybrid, commercial/workboat), national and regional dealer networks, government/military contracts, commercial operators (fishing, towing, ferry), and export distributors. The top 2 customers (Marine OEM Client A and Client B) account for $52.4M and $38.6M in LTM revenue respectively, with Client A being a sole-source relationship at 2,800 units/year and Client B under a 3-year fixed-pricing contract through 2027. Top 10 customers collectively represent ~$215.5M of LTM revenue. The customer base reflects a marine propulsion/components manufacturer with a national and international footprint, long-tenured key accounts, and meaningful government contract exposure.
- deal_context (confidence=0.75): company=Project Driftwood, sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - doc_type overridden from dd_report hint to dd_report (confirmed — this is a data room customer analysis supporting due diligence, consistent with dd_report classification even though it is an xlsx workbook; key_quotes left empty per rules for xlsx workbooks)
  - LTM revenue for the full company is not stated in this sheet; only individual customer line items are shown — revenue_ltm_usd left null
  - % LTM rev column (col_5) is blank in the source data — concentration percentages could not be validated
  - Deal type defaulted to 'platform' as no explicit deal structure is indicated in this document

  </details>

### `Data Room/Financials/Driftwood Historical Financials 2020-2025.xlsx` → `doc_project_driftwood_005` (financial_model)
- Title: Project Driftwood — Historical Financials (FY20–LTM)
- Date: 2025-09-30
- Summary: Historical income statement and revenue segmentation workbook for Project Driftwood covering FY2020–FY2024 (audited by Grant Thornton) and LTM through September 2025 (management-prepared). Revenue grew from $268M in FY20 to $420M LTM, implying a ~5-year CAGR of roughly 9.4%. Segments include OEM (domestic), Aftermarket/Parts, Export, and Government/Commercial. Reported EBITDA cells are unpopulated in the workbook; Adj. EBITDA is calculable from reported lines plus four addback items (family comp excess, below-market lease reversal, one-time/non-recurring, insurance/legal). LTM Adj. EBITDA is estimated at ~$58.5M (Revenue $420M − COGS $272M − SG&A $92M + net addbacks of ~$2.7M), implying an Adj. EBITDA margin of ~13.9%.
- deal_context (confidence=0.8): company=None, sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - EBITDA (reported), Gross profit, Gross margin %, Adj. EBITDA, and Adj. EBITDA margin % cells are blank in the workbook; LTM Adj. EBITDA (~$58.5M) and margin (~13.9%) were computed manually from available line items: Revenue $420M − COGS $272M − SG&A $92M + addbacks ($3.2M − $2.8M + $1.6M + $0.7M = $2.7M).
  - revenue_cagr_3yr computed from FY22A ($320M) to LTM ($420M) over ~3 years ≈ 9.6%; used as proxy for 3-year CAGR.
  - Segment CAGR column is blank in the workbook and was not computed.
  - Subsector 'industrial_components' inferred from OEM, Aftermarket/Parts, Export, and Government segments suggesting a manufactured component/parts business; no explicit sector confirmation in the document.

  </details>

### `Data Room/Legal/Driftwood QofE Summary 2025-12.pdf` → `doc_project_driftwood_006` (dd_report)
- Title: Project Driftwood — Quality of Earnings Summary (Preliminary): BlueCrest Marine Holdings, Inc.
- Date: 2025-12-05
- Summary: Deloitte's preliminary Quality of Earnings review of BlueCrest Marine Holdings, Inc. (Project Driftwood). LTM Reported EBITDA of $51.8M bridges to Deloitte's preliminary Adj. EBITDA of $54.0M after $4.2M in add-backs (Halverson family excess compensation, one-time legal/ERP/marketing/pre-opening costs) offset by a $2.0M below-market rent normalization. Management's Adj. EBITDA is $56.0M; a $2.0M gap remains under review related to DTC fulfillment cost reclassification. LTM revenue is ~$420M (OEM 65%, retail 29%, DTC 6%). Key confirmatory items include the DTC cost reclassification, LIFO reserve impact on working capital peg ($14.8M), Asian contract manufacturer pricing step-ups in Q1 2026, Halverson family property market rent substantiation, and large OEM custom order revenue recognition review. Working capital peg proposed at $72M LTM average.
- deal_context (confidence=0.85): company=BlueCrest Marine Holdings, Inc., sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - Document is titled 'Investment Committee Memorandum' but content is clearly a Quality of Earnings summary prepared by Deloitte — classified as dd_report per content, consistent with folder hint.
  - LTM revenue of ~$420M is inferred by summing disclosed channel revenues: OEM $273M + Retail $122M + DTC $25M = $420M; not explicitly stated as a single figure.
  - Deloitte preliminary Adj. EBITDA is $54.0M; management claims $56.0M — used $54.0M as the more conservative/verified figure for ebitda_ltm_usd.
  - ebitda_margin calculated on $54M EBITDA / $420M revenue = 12.86%; subject to revision pending confirmatory procedures.
  - Deal type defaulted to 'platform' as no explicit deal type is stated; founder/family ownership (Halverson family) and transition signals support this assumption.

  </details>

### `Data Room/Operations/Driftwood Operations Overview 2025-11.pdf` → `doc_project_driftwood_007` (ic_memo)
- Title: Project Driftwood — Operations Overview: BlueCrest Marine Holdings, Inc.
- Date: 2025-11-01
- Summary: IC memorandum covering the operational profile of BlueCrest Marine Holdings, Inc. (Project Driftwood). Details a two-facility manufacturing footprint in Fort Lauderdale, FL (primary, 220k sq ft, 74% utilization, leased below-market from Halverson family LLC) and Tampa, FL (secondary, 95k sq ft, 68% utilization, owned). Products span deck hardware, anchoring/fender systems, marine lighting, and dock hardware. Contract manufacturing accounts for ~52% of COGS across four partners (two domestic, two China-based). Key raw materials include marine-grade stainless steel (24% of COGS, no volume contract), aluminum alloy (18%), marine plastics (12%), and electrical components (8%) — all procured largely on spot terms, representing a meaningful cost-reduction opportunity via volume contracting. Operational KPIs show consistent improvement across FY22–LTM: OEM on-time delivery reached 94.1%, fill rate 97.8%, inventory turns 5.9x, and defect/warranty rate down to 1.1%. Below-market lease ($3.8M vs. ~$5.8M market) is flagged as a post-close normalization item.
- deal_context (confidence=0.85): company=BlueCrest Marine Holdings, Inc., sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint was 'dd_report' but document header clearly states 'Investment Committee Memorandum' — classified as ic_memo.
  - No revenue or EBITDA figures present in this document; financial metrics left null.
  - Geography set to southeast_us based on primary facility in Fort Lauderdale, FL; company may have broader national reach given Midwest and Georgia CM partners.
  - Date defaulted to 2025-11-01 (month precision only) based on 'November 2025' in document header.

  </details>

### `Data Room/Org Structure/Driftwood Org Structure 2025-11.pdf` → `doc_project_driftwood_008` (ic_memo)
- Title: Project Driftwood — Corporate and Organizational Structure: BlueCrest Marine Holdings, Inc.
- Date: 2025-11-01
- Summary: This IC memorandum documents the corporate legal entity structure and organizational leadership of BlueCrest Marine Holdings, Inc. (Project Driftwood). The top-level holdco is Halverson Marine Holdings, LLC (Florida), majority-owned by Steve Halverson (68%) with the remainder held in family trusts. BlueCrest Marine Holdings, Inc. (Delaware) is the primary operating entity, with wholly-owned subsidiaries for Florida-based manufacturing (Fort Lauderdale + Tampa), an Asia sourcing/import entity, and a Canadian sales and distribution arm. Total headcount is 1,100, heavily weighted toward manufacturing (~49%). Key leadership includes CEO Steve Halverson (2nd-generation, staying post-close), CFO Karen Halverson (departing post-close — transition risk flagged), COO Brad Tanner (Brunswick background, retention priority), VP Sales Lisa Park, VP Engineering Mike Reyes, and VP Supply Chain Dan Wu. The document is dated November 2025 and marked confidential for IC use only.
- deal_context (confidence=0.82): company=BlueCrest Marine Holdings, Inc., sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - doc_type hint was absent; content is clearly an IC memorandum covering org/legal structure, classified as ic_memo.
  - Date defaulted to 2025-11-01 (first of month) since only month/year (November 2025) is provided on the cover.
  - No financial figures are present in this document — all financial structured fields are null.
  - Geography tagged as southeast_us based on Florida HQ and manufacturing locations; Canadian subsidiary noted but not primary geography.

  </details>

### `Financial Model/Driftwood LBO Model_v1.xlsx` → `doc_project_driftwood_009` (financial_model)
- Title: Project Driftwood — LBO Model (Base Case)
- Date: 2026-02-01
- Summary: LBO financial model for Project Driftwood prepared by Atlas Crossing Partners Fund IV in February 2026. The model reflects a June 30, 2026 entry at a $580M enterprise value on $56M LTM Adj. EBITDA (implying a ~10.4x entry multiple). LTM revenue is $420M. The capital structure consists of $320M senior secured TLB (Golub Capital), $110M Atlas Crossing equity, $110M Halverson family rollover (~19%), and $48M management equity pool (8%). The QofE bridge (Deloitte preliminary) reconciles reported EBITDA of $39.4M to $56.6M Adj. EBITDA through add-backs including D&A normalization, excess family compensation, one-time legal/IP costs, and restructuring charges. Base case P&L projections show revenue growing from $420M (LTM) to $604M by FY30B, with EBITDA margins expanding from ~14.5% to ~18.5%. Returns sensitivity runs across downside (exit EV at 8.5x on $68M EBITDA), base (10.5x on $95M), and upside (12x on $120M) scenarios over a 5-year hold. Key growth drivers include OEM and aftermarket/parts revenue growth, with aftermarket mix rising from 38% to 42% of total revenue. Automation capex is a notable investment theme.
- deal_context (confidence=0.82): company=Project Driftwood, sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - Entry multiple cell in Summary sheet is blank (formula not rendered); computed manually as $580M EV / $56M EBITDA = ~10.36x — used this for ev_ebitda_multiple.
  - Total sources/uses cells are blank (formula rows not rendered); individual line items sum to $588M sources vs $630M uses — likely working capital / fee line items are incomplete in the extracted text.
  - QofE preliminary Adj. EBITDA is $56.6M (Deloitte) vs. $58M (management estimate); model uses $56M round figure in Summary sheet — used $56M for ebitda_ltm_usd.
  - revenue_cagr_3yr estimated from FY22A ($320M) to FY24A ($392M): CAGR ~10.6%; used ~0.10 as approximation.
  - ebitda_margin computed as $56M / $420M = 13.3% (LTM); note that projected FY26B margin is 14.5% per Assumptions sheet.
  - Geography inferred as southeast_us based on mention of Ft. Lauderdale HQ; not explicitly stated as company headquarters.
  - Sector/subsector inferred as manufacturing / industrial_components based on references to OEM revenue, aftermarket/parts, manufacturing equipment, and automation capex — no explicit sector label in document.
  - Halverson family risk flagged under founder_transition thesis theme and risk_flags, though no formal risk_theme enum exists for founder_transition — mapped to integration_risk as closest proxy in risk_flags.

  </details>

### `Legal/Driftwood Draft LOI 2026-01.pdf` → `doc_project_driftwood_010` (ic_memo)
- Title: Letter of Intent (Draft) — Proposed Acquisition of BlueCrest Marine Holdings, Inc. ("Project Driftwood")
- Date: 2026-01-08
- Summary: Draft Letter of Intent submitted by Atlas Crossing Partners Fund IV, L.P. for the proposed acquisition of 100% of the equity of BlueCrest Marine Holdings, Inc. ("Project Driftwood") on a cash-free, debt-free basis at an enterprise value of $580M, implying a 10.7x multiple of LTM Adj. EBITDA of ~$54M (per Deloitte preliminary QofE). The document outlines proposed sources & uses, key deal terms including management retention (Steve Halverson as CEO for 2+ years, Karen Halverson as transition CFO, Brad Tanner as COO), R&W insurance terms, an NWC peg of $72M, and key closing conditions including OEM consent from Brunswick, Malibu, MasterCraft, and Grady-White. Exclusivity runs through March 31, 2026. Target close is Q1 2026.
- deal_context (confidence=0.95): company=BlueCrest Marine Holdings, Inc., sector=consumer_products, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - doc_type hint was 'dd_report' (folder: Legal/) but content is clearly a draft Letter of Intent; overriding to 'ic_memo' as the closest available taxonomy value. A dedicated 'loi' doc_type is proposed.
  - Revenue LTM is not disclosed in this document; only LTM Adj. EBITDA ($54M per Deloitte QofE preliminary, $56M per management) is referenced.
  - Sector classified as 'consumer_products' based on marine recreational products context (OEM relationships with Brunswick, Malibu, MasterCraft, Grady-White), but no subsector under consumer_products fits marine products; subsector left null with taxonomy proposal filed.
  - Geography set to 'southeast_us' based on Fort Lauderdale, FL facility reference for the Halverson family property; national footprint cannot be confirmed from this document alone.
  - Sources ($525M) and Uses ($649M) do not balance as presented in the document — this appears to be an error or incomplete draft; flagged for deal team review.
  - EBITDA LTM of $54M is a Deloitte preliminary QofE figure, not a final audited number; management figure is $56M.

  </details>

### `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-10.pdf` → `doc_project_driftwood_011` (cim)
- Title: Project Driftwood — Management Presentation (Excerpt)
- Date: 2025-10-09
- Summary: Management presentation excerpt for Project Driftwood, the codename for BlueCrest Marine Supply — a 47-year-old manufacturer of marine deck hardware and OEM-supplied accessories with $420M in LTM revenue. The presentation covers company history under the Halverson family, deep OEM relationships (Brunswick, Malibu, MasterCraft, Grady-White, and others representing ~$273M in identified OEM revenue), and a three-lever value creation roadmap: ERP modernization (~$3–4M EBITDA), procurement consolidation (~$4–6M EBITDA), and a DTC channel build-out ($35–50M incremental revenue). Coordinated by Baird Industrial & Services as sell-side advisor.
- deal_context (confidence=0.92): company=BlueCrest Marine Supply, sector=manufacturing, subsector=industrial_components
- <details><summary>⚠ extraction warnings</summary>

  - Doc type hinted as none; classified as 'cim' (closest to management presentation in taxonomy) — see taxonomy_proposals for proposed 'management_presentation' doc_type.
  - LTM EBITDA not explicitly stated in the excerpt; ebitda_ltm_usd and ebitda_margin left null.
  - EV and entry multiple not disclosed in this excerpt; ev_proposed_usd and ev_ebitda_multiple left null.
  - Revenue CAGR not explicitly stated; implied growth from $180M (2008) to $420M (2025) is ~5% CAGR over 17 years, but no 3-year CAGR was disclosed — left null.
  - OEM revenue line items sum to ~$273M across named partners; remaining ~$147M is indirect/unattributed — customer concentration risk may be understated.
  - Founder-transition risk flagged: Harold Halverson founded company, Steve Halverson (son, presumed) is CEO; Karen Halverson (CFO) suggests continued family control — management_quality risk flagged accordingly.

  </details>

### `Presentations/Investment Decks/ACP Preliminary IC Review 2025-09.pdf` → `doc_project_driftwood_012` (ic_memo)
- Title: Atlas Crossing Partners — Fund IV Investment Committee Memorandum: Preliminary IC Review — Project Driftwood
- Date: 2025-09-05
- Summary: Preliminary IC memorandum from Atlas Crossing Partners (Fund IV) recommending advancing to IOI for Project Driftwood (BlueCrest), a 47-year-old family-owned marine equipment & accessories manufacturer and category leader. ACP recommends a $560M indicative bid (10.0x LTM EBITDA) in a Baird-run limited auction. LTM Adj. EBITDA is $56M on a revenue base not explicitly stated. Key value-creation levers include ERP implementation, procurement optimization, and DTC channel build-out. Primary risks include CFO transition, OEM consent requirements on change-of-control, China sourcing concentration, ERP implementation risk, and cyclicality. Diligence is active across Deloitte (QoE), LEK (commercial), Kirkland & Ellis (legal), West Monroe (IT/ops), and KPMG (tax). Base case projects 2.9x MOIC / 23.5% IRR over a 5-year hold.
- deal_context (confidence=0.95): company=BlueCrest, sector=consumer_products, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - Revenue LTM figure is not explicitly stated in the document; only LTM Adj. EBITDA ($56M) is provided.
  - Indicative EV range is $520M–$640M; the recommended IOI bid of $560M (10.0x) is used as ev_proposed_usd and ev_ebitda_multiple.
  - Subsector left null — no consumer_products subsector in taxonomy fits marine equipment & accessories; taxonomy proposal submitted.
  - The document references 'consumer / light industrial — marine equipment & accessories' as the sector, which does not cleanly map to any existing sector enum; consumer_products used as closest match.

  </details>

## Resolver disagreements

### company_canonical
- Chosen: `BlueCrest Marine Holdings, Inc.` (plurality 3/5)
- Voters for chosen: ['Banker Materials/CIM/CIM BlueCrest Marine Holdings 2025-08.pdf', 'Banker Materials/Teaser/Teaser Baird 2025-07.pdf', 'Legal/Driftwood Draft LOI 2026-01.pdf']
- Dissent `BlueCrest Marine Supply`: ['Presentations/Data Room Cuts/Management Presentation Excerpt 2025-10.pdf']
- Dissent `BlueCrest`: ['Presentations/Investment Decks/ACP Preliminary IC Review 2025-09.pdf']

### sector
- Chosen: `manufacturing` (plurality 3/5)
- Voters for chosen: ['Banker Materials/CIM/CIM BlueCrest Marine Holdings 2025-08.pdf', 'Banker Materials/Teaser/Teaser Baird 2025-07.pdf', 'Presentations/Data Room Cuts/Management Presentation Excerpt 2025-10.pdf']
- Dissent `consumer_products`: ['Legal/Driftwood Draft LOI 2026-01.pdf', 'Presentations/Investment Decks/ACP Preliminary IC Review 2025-09.pdf']

### geography
- Chosen: `national` (plurality 3/5)
- Voters for chosen: ['Banker Materials/Teaser/Teaser Baird 2025-07.pdf', 'Presentations/Data Room Cuts/Management Presentation Excerpt 2025-10.pdf', 'Presentations/Investment Decks/ACP Preliminary IC Review 2025-09.pdf']
- Dissent `southeast_us`: ['Banker Materials/CIM/CIM BlueCrest Marine Holdings 2025-08.pdf', 'Legal/Driftwood Draft LOI 2026-01.pdf']

### financials.revenue_cagr_3yr
- Chosen: `0.073` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Banker Materials/CIM/CIM BlueCrest Marine Holdings 2025-08.pdf']
- Dissent `0.1`: ['Financial Model/Driftwood LBO Model_v1.xlsx']
- Dissent `0.096`: ['Data Room/Financials/Driftwood Historical Financials 2020-2025.xlsx']

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- subsector: proposed=`marine_hardware_manufacturing` (used `industrial_components`, confidence=0.75)
  - rationale: BlueCrest Marine Supply is a specialized manufacturer of marine deck hardware, OEM accessories, and related marine products. The taxonomy does not include a marine-specific subsector; 'industrial_components' under 'manufacturing' is the closest fit.
- sector: proposed=`consumer_durables_manufacturing` (used `manufacturing`, confidence=0.65)
  - rationale: BlueCrest manufactures branded consumer-facing marine accessories sold via OEM, retail, and DTC channels. It straddles manufacturing and consumer products. 'manufacturing' was selected as primary because production and distribution are the core value-drivers, but a 'consumer_durables' sector tag would better capture the branded retail/DTC thesis.
- subsector: proposed=`marine_hardware_and_accessories` (used `industrial_components`, confidence=0.8)
  - rationale: BlueCrest manufactures and distributes marine deck hardware, anchoring systems, fender systems, and dock equipment — a distinct marine accessories niche that does not cleanly map to 'industrial_components' (which implies broader industrial B2B parts). A dedicated 'marine_hardware_and_accessories' subsector under manufacturing would better capture this vertical.
- subsector: proposed=`marine_propulsion_components` (used `industrial_components`, confidence=0.8)
  - rationale: Project Driftwood appears to be a marine propulsion/drivetrain components manufacturer serving OEM boat builders, commercial operators, and aftermarket dealers. 'industrial_components' is the closest available subsector under manufacturing, but a dedicated 'marine_propulsion_components' subsector would better capture this vertical.
- subsector: proposed=`oem_components_and_aftermarket` (used `industrial_components`, confidence=0.72)
  - rationale: The business has distinct OEM domestic, aftermarket/parts, export, and government segments typical of a manufactured components supplier with aftermarket distribution. 'industrial_components' is the closest existing subsector under manufacturing, but a more specific 'oem_components_and_aftermarket' subsector would better capture this business model.
- subsector: proposed=`marine_products_manufacturing` (used `industrial_components`, confidence=0.6)
  - rationale: BlueCrest Marine Holdings manufactures marine/boat OEM and aftermarket products. There is no marine or consumer durables subsector in the taxonomy; industrial_components is the closest available under manufacturing.
- doc_type: proposed=`operations_ic_memo` (used `ic_memo`, confidence=0.8)
  - rationale: Document is explicitly labeled 'Investment Committee Memorandum — Operations Overview,' a hybrid ops diligence / IC memo format not cleanly captured by either 'ic_memo' or 'dd_report' in the taxonomy. Classified as ic_memo given the IC header designation.
- subsector: proposed=`marine_manufacturing` (used `industrial_components`, confidence=0.65)
  - rationale: BlueCrest is a marine products manufacturer. The taxonomy has no marine-specific subsector under manufacturing; 'industrial_components' is the closest available fit but does not fully capture the marine OEM/consumer marine hardware nature of the business.
- risk_theme: proposed=`founder_retention_risk` (used `management_quality`, confidence=0.75)
  - rationale: The Halverson family holds ~19% rollover equity and the QofE includes excess family compensation add-back for CEO + 2 family members. This represents a distinct founder/family retention and transition risk that is not fully captured by management_quality or integration_risk.
- doc_type: proposed=`loi` (used `ic_memo`, confidence=0.85)
  - rationale: This document is a draft Letter of Intent, a distinct deal document type not present in the current taxonomy. It is closest to ic_memo as it contains proposed deal terms, valuation, and key conditions reviewed at the investment committee / deal team level. A dedicated 'loi' doc_type would be appropriate for future taxonomy expansion.
- subsector: proposed=`marine_products_distribution` (used `packaged_food`, confidence=0.8)
  - rationale: BlueCrest Marine Holdings is a marine products company (likely a boat/marine dealer or distributor based on OEM relationships with Brunswick, Malibu, MasterCraft, Grady-White). No subsector under consumer_products fits marine products. The closest existing consumer_products subsector is packaged_food, which does not fit. A new subsector such as 'marine_products' or 'powersports_products' under consumer_products (or potentially a separate sector) would be more appropriate.
- doc_type: proposed=`management_presentation` (used `cim`, confidence=0.82)
  - rationale: This document is explicitly a 'Management Presentation' (sell-side prepared, presented by company management at a banker-coordinated data room process). While it overlaps with CIM-like content, a distinct 'management_presentation' doc_type would better capture this format. Mapped to 'cim' as the closest existing type.
- subsector: proposed=`marine_equipment_accessories` (used `packaged_food`, confidence=0.85)
  - rationale: BlueCrest is a marine equipment & accessories manufacturer/brand. The consumer_products sector has subsectors pet_food, pet_supplies, and packaged_food — none of which map to marine/light industrial consumer goods. A 'marine_equipment_accessories' or broader 'branded_consumer_durables' subsector would be more appropriate.
- sector: proposed=`consumer_durables` (used `consumer_products`, confidence=0.8)
  - rationale: BlueCrest operates in marine equipment & accessories, which is more accurately classified as consumer durables / light industrial branded goods rather than the food/pet-focused consumer_products sector. consumer_products is the closest available enum but a 'consumer_durables' or 'branded_consumer_goods' sector would better capture this business.
