# Ingestion report — Project Aurora

Deal ID: `deal_project_aurora_2026`
Company canonical: `Helix Specialty Chemicals, Inc.`
Sector / subsector: `specialty_chemicals` / `specialty_intermediates`
Geography: `national`
Deal type: `platform`
Voted with 5 qualifying docs at confidence >= 0.9 (out of 12 tagged).

## Triage

### primary (12)
- `Advisors/Aurora_Advisor_Engagement_Summary_2026-01.pdf` [hint: dd_report]
- `Banker Materials/cim/CIM_Helix_Specialty_Chemicals_2025-12.pdf` [hint: cim]
- `Banker Materials/teaser/Teaser_Lazard_2025-11.pdf` [hint: cim]
- `Data Room/customers/Aurora_Top50_Customer_Analysis.xlsx` [hint: dd_report]
- `Data Room/financials/Aurora_Historical_Financials_2020-2025.xlsx` [hint: financial_model]
- `Data Room/legal/Aurora_Legal_Diligence_Summary_2026-01.pdf` [hint: dd_report]
- `Data Room/operations/Aurora_Operations_Overview_2026-01.pdf` [hint: dd_report]
- `Data Room/org-structure/Aurora_Org_Structure_2025-12.pdf` [hint: dd_report]
- `Financial Model/Aurora_LBO_Model_v1.xlsx` [hint: financial_model]
- `Legal/Aurora_Term_Sheet_2026-01.pdf` [hint: dd_report]
- `Presentations/data-room-cuts/Management_Presentation_Excerpt_2025-12.pdf` [hint: ic_memo]
- `Presentations/investment-decks/ACP_Preliminary_IC_Review_2025-11.pdf` [hint: ic_memo]

### format_duplicate (9)
- `Advisors/Aurora_Advisor_Engagement_Summary_2026-01.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Banker Materials/cim/CIM_Helix_Specialty_Chemicals_2025-12.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Banker Materials/teaser/Teaser_Lazard_2025-11.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Data Room/legal/Aurora_Legal_Diligence_Summary_2026-01.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Data Room/operations/Aurora_Operations_Overview_2026-01.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Data Room/org-structure/Aurora_Org_Structure_2025-12.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Legal/Aurora_Term_Sheet_2026-01.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Presentations/data-room-cuts/Management_Presentation_Excerpt_2025-12.docx` [hint: ic_memo] — PDF preferred over DOCX/PPTX twin
- `Presentations/investment-decks/ACP_Preliminary_IC_Review_2025-11.docx` [hint: ic_memo] — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Advisors/Aurora_Advisor_Engagement_Summary_2026-01.pdf` → `doc_project_aurora_001` (ic_memo)
- Title: Project Aurora — Advisors: Engagement and Workstream Summary — Confirmatory Diligence
- Date: 2026-01-01
- Summary: This IC memorandum summarizes the advisor engagement landscape for Project Aurora's confirmatory diligence phase as of January 2026. Eight advisory firms are engaged across legal (Kirkland & Ellis), quality of earnings (EY), commercial diligence (Bain), IT/ops (Crowe), insurance/risk (Marsh), tax (PwC), debt commitment (Antares Capital and Twin Brook Capital), and R&W insurance (Ambridge). The document details workstream status, key milestones targeting a close by April 14, 2026, estimated advisor fees totaling $8.3–10.5M out-of-pocket, and four open issues requiring IC decisions — including debt structure, R&W retention, founder rollover percentage, and management equity pool size. The memo was compiled by Marcus Chen (Principal) and reviewed by Sarah Lemberg (MD).
- deal_context (confidence=0.85): company=None, sector=None, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint was 'dd_report' but document content is clearly an IC Memorandum (header: 'Investment Committee Memorandum'); classified as 'ic_memo' instead.
  - Date defaulted to 2026-01-01 as only month/year (January 2026) is specified in the document.
  - No sector, geography, or financial metrics (revenue, EBITDA, EV) are identifiable from this advisor engagement summary alone; deal_context fields left null accordingly.
  - Codename 'Aurora' detected; 'Helix internal' referenced in milestone table may be a company-related name but insufficient evidence to confirm as company_canonical.

  </details>

### `Banker Materials/cim/CIM_Helix_Specialty_Chemicals_2025-12.pdf` → `doc_project_aurora_002` (cim)
- Title: Confidential Information Memorandum — Helix Specialty Chemicals ("Project Aurora")
- Date: 2025-12-01
- Summary: Lazard Middle Market CIM for Helix Specialty Chemicals ("Project Aurora"), a 39-year-old independent specialty chemicals distributor headquartered in Cleveland, OH. Helix is the #3 independent distributor by revenue in North America and #1 in its core Midwest/Southeast geography, with $725M LTM revenue and $95M LTM Adj. EBITDA (13.1% margin). The business is 100% family-owned (3rd generation Beckwith family) and is being brought to market as a full sale, with CEO Tom Beckwith open to rollover equity. Key investment highlights include strong customer diversification (top 10 = 14% of revenue), 94% customer retention, a 14.8% revenue CAGR (FY22–FY25 LTM), expanding EBITDA margins (10.9% → 13.1%), a differentiated technical sales force, and a robust M&A pipeline of 10+ proprietary targets. The transaction process targets IOIs in January 2026 and closing in Q2 2026.
- deal_context (confidence=0.95): company=Helix Specialty Chemicals, sector=specialty_chemicals, subsector=specialty_intermediates
- <details><summary>⚠ extraction warnings</summary>

  - No enterprise value or EV/EBITDA multiple is stated in the CIM; ev_proposed_usd and ev_ebitda_multiple left null.
  - Deal type mapped to 'platform' as the closest taxonomy fit; this is a full family exit of a scaled platform business — see taxonomy_proposals for a more precise proposed value.
  - Subsector mapped to 'specialty_intermediates' (closest available under specialty_chemicals) but Helix is a distributor, not a manufacturer — see taxonomy_proposals.
  - Date set to 2025-12-01 based on 'December 2025' cover page date; exact day not specified in document.

  </details>

### `Banker Materials/teaser/Teaser_Lazard_2025-11.pdf` → `doc_project_aurora_003` (cim)
- Title: Project Aurora — Confidential Teaser
- Date: 2025-11-01
- Summary: Lazard Middle Market teaser for Project Aurora, a 3rd-generation family-owned ($725M LTM revenue) specialty chemicals distributor with operations across 18 US states and 4 Canadian provinces. The company serves water treatment, paints & coatings, oil & gas, industrial manufacturing, and food & personal care end markets. Key investment highlights include a 13.1% LTM Adj. EBITDA margin, 14.8% 3-year revenue CAGR, a diversified 3,200-customer base (top 10 = 14% of revenue), 87% repeat/contracted revenue, and a bolt-on M&A platform with 10+ identified targets. CEO Tom Beckwith (age 62) is motivated to transition with rollover equity and an 18-month transition role. Process is a limited auction with Round 1 IOIs due November 18, 2025 and expected close Q2 2026.
- deal_context (confidence=0.92): company=Project Aurora (Beckwith family specialty chemicals distributor), sector=specialty_chemicals, subsector=process_chemicals
- <details><summary>⚠ extraction warnings</summary>

  - Doc_type hint was 'cim' but document content is explicitly a teaser (Confidential Teaser), which is a shorter pre-CIM marketing document. Classified as 'cim' per closest available doc_type, but a 'teaser' sub-type would be more precise — added taxonomy proposal.
  - No enterprise value or EV/EBITDA multiple disclosed in the teaser; ev_proposed_usd and ev_ebitda_multiple left null.
  - Geography set to 'national' to reflect US + Canada footprint; the taxonomy does not have a 'north_america' or 'canada' option — national_us_canada would be more precise.
  - subsector 'process_chemicals' is the closest existing value but does not accurately reflect a distribution business model; taxonomy proposal filed.

  </details>

### `Data Room/customers/Aurora_Top50_Customer_Analysis.xlsx` → `doc_project_aurora_004` (dd_report)
- Title: Project Aurora — Top 50 Customer Analysis
- Date: 2025-11-01
- Summary: Customer concentration analysis workbook for Project Aurora covering the top 50 de-identified customers based on LTM revenue through November 2025. The customer base spans five end markets: Industrial Manufacturing, Water Treatment, Paints & Coatings, Oil & Gas, and Food & Personal Care. The top customer (Customer A, large industrial manufacturer) accounts for $20.3M in LTM revenue, and the top 10 customers collectively generate approximately $104.4M. Average customer tenure across the top 50 is notable, with several customers having 10+ year relationships. Contract types are predominantly master supply agreements and multi-year supply agreements, suggesting reasonable revenue predictability. Concentration statistics (top 10, top 25, top 50 as % of total revenue) are not populated in the workbook. A small number of spot-purchase customers (Customers LL and UU) represent minimal revenue and lower stickiness.
- deal_context (confidence=0.82): company=None, sector=specialty_chemicals, subsector=process_chemicals
- <details><summary>⚠ extraction warnings</summary>

  - doc_type overridden to dd_report per folder hint; content is an xlsx data room workbook (customer analysis), which could reasonably be classified as financial_model but is more accurately a due diligence support file
  - Top 10/25/50 concentration % cells and tenure statistics are blank in the source workbook — cannot compute without total LTM revenue denominator
  - Total LTM revenue for the company is not present in this workbook; revenue_ltm_usd left null
  - Customer names are de-identified; sector/subsector inferred from end-market descriptions (industrial mfg, water treatment, paints & coatings, oil & gas, food & personal care) which are consistent with a specialty chemicals supplier
  - Subsector set to process_chemicals as best fit under specialty_chemicals given the industrial/process end-market mix; a more precise subsector (e.g., process_chemicals or treatment_chemicals) could be proposed

  </details>

### `Data Room/financials/Aurora_Historical_Financials_2020-2025.xlsx` → `doc_project_aurora_005` (financial_model)
- Title: Project Aurora — Historical Financials (FY20-FY25 LTM)
- Date: 2025-11-30
- Summary: Historical income statement and balance sheet for Project Aurora covering FY2020 through FY2025 LTM (through November 2025). Audited by EY for FY20–FY24; LTM per management. Revenue grew from $405M in FY20 to $725M LTM, implying a ~12.4% 3-year CAGR (FY22–FY25 LTM). Calculated Adj. EBITDA for LTM is approximately $96.5M (revenue $725M minus COGS $501M minus S&M $93M minus G&A $35M = reported EBITDA $96M, plus addbacks of $3M family expenses + $1M legal one-time – $1.5M non-recurring trading gains = ~$98.5M Adj. EBITDA), yielding an Adj. EBITDA margin of roughly 13.6%. The balance sheet reflects a capital-light business with modest long-term debt (~$52M) and goodwill of $18M (flat since FY20, suggesting no M&A activity). Stockholders' equity is attributed to the Beckwith family, indicating a founder/family-owned business. Several addback items (family expenses, legal one-time, pre-opening costs) are consistent with a founder-transition scenario.
- deal_context (confidence=0.78): company=None, sector=None, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - Several income statement subtotals (Gross profit, EBITDA reported, Adj. EBITDA, margins) are blank in the source workbook — values were manually computed from line items present.
  - LTM Adj. EBITDA computed as: Revenue $725M – COGS $501M – S&M $93M – G&A $35M = $96M reported EBITDA + $3M family addback + $1M legal addback + $0M pre-opening – $1.5M trading gains = ~$98.5M; margin ~13.6%. Figures should be validated against a populated version of the model.
  - 3-year revenue CAGR computed as FY22A–FY25 LTM ($540M → $725M, ~3 years): CAGR ≈ 10.3%. Alternatively FY22A→FY24A: ($540M → $686M, 2 years) = ~12.8%. Value reported is approximate; exact period depends on LTM annualization convention.
  - Balance sheet equity line ('Stockholders' equity (Beckwith family)') is blank — no equity value extractable.
  - Sector/geography/deal_type cannot be determined from this financial workbook alone; deal_context fields left null accordingly.
  - Doc type confirmed as financial_model per folder hint (Data Room/financials/) and workbook content.

  </details>

### `Data Room/legal/Aurora_Legal_Diligence_Summary_2026-01.pdf` → `doc_project_aurora_006` (dd_report)
- Title: Project Aurora — Legal Diligence Summary: Helix Specialty Chemicals
- Date: 2026-01-08
- Summary: Kirkland & Ellis preliminary legal diligence summary for Project Aurora (Helix Specialty Chemicals), prepared for IC use. No material adverse findings identified. Key open items include: (i) supplier COC consent letters from Dow, BASF, Croda, and Stepan; (ii) Phase II environmental investigation at Houston DC; (iii) resolution of California wrongful termination matter (Wilson); (iv) confirmation of CleanRivers (PA DEP) remediation timeline; (v) intercompany loan and family entity documentation; and (vi) IP assignment confirmation from founder Beckwith. Pending litigation is low-materiality across four matters. Workforce is largely non-union (1,140 FTEs; 86 unionized at Cleveland DC). Significant deferred tax liability ($14.2M, LIFO-related) noted with transaction structuring implications.
- deal_context (confidence=0.88): company=Helix Specialty Chemicals, sector=specialty_chemicals, subsector=specialty_intermediates
- <details><summary>⚠ extraction warnings</summary>

  - doc_type hint was dd_report; content is an IC Legal Diligence Summary submitted by outside counsel (K&E), which is consistent with dd_report classification — no override needed.
  - No financial metrics (revenue, EBITDA, EV) are present in this legal diligence document; structured financials left null.
  - Subsector 'specialty_intermediates' is an imperfect fit — Helix appears to be primarily a specialty chemical distributor/blender rather than an intermediates manufacturer; taxonomy proposal filed.
  - Deal type classified as 'platform' based on context clues (founder family ownership structure, PE sponsor transaction language) but not explicitly stated in this document.

  </details>

### `Data Room/operations/Aurora_Operations_Overview_2026-01.pdf` → `doc_project_aurora_007` (ic_memo)
- Title: Operations Overview — Helix Specialty Chemicals
- Date: 2026-01-01
- Summary: This Investment Committee Memorandum provides a detailed operational overview of Helix Specialty Chemicals (Project Aurora) as of January 2026. The document covers Helix's 8-DC distribution network spanning the eastern, southern, and western US plus Ontario, Canada, anchored by a 320K sq. ft. Cleveland flagship facility. Key operational KPIs show steady improvement across on-time delivery (88.0%), customer fill rate (96.4%), order accuracy (97.8%), and inventory turns (7.4x), with most metrics at or above industry benchmarks. Supply chain data highlights concentration among top-25 strategic suppliers (64% of COGS) with growing rebate capture. Technology systems include a recently completed NetSuite ERP rollout, partially deployed Manhattan WMS, Salesforce CPQ, and a growing digital ordering channel (Helix Direct at 6% of LTM revenue, +60% YoY). Key initiatives in flight include WMS completion across 3 remaining DCs, Cleveland blending capacity expansion (+$3M EBITDA at full utilization), Houston environmental remediation ($400–800K cost), procurement tier-2 consolidation (+120bps gross margin), and a West Coast/PNW DC strategic review.
- deal_context (confidence=0.88): company=Helix Specialty Chemicals, sector=specialty_chemicals, subsector=specialty_intermediates
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint was dd_report, but document header explicitly states 'Investment Committee Memorandum' — overriding to ic_memo.
  - No revenue or EBITDA figures are present in this operations-focused document; financial metrics left null.
  - Subsector 'specialty_intermediates' used as closest fit under specialty_chemicals, but Helix's model is primarily specialty chemical distribution with blending — a dedicated 'specialty_distribution' subsector under specialty_chemicals would be more precise.
  - Date defaulted to 2026-01-01 (first of month) as only month/year (January 2026) was provided on the cover page.
  - Toronto, ON facility noted — company has minor Canadian operations, but geography tagged as 'national' (US-focused) as the majority of operations are US-based.

  </details>

### `Data Room/org-structure/Aurora_Org_Structure_2025-12.pdf` → `doc_project_aurora_008` (ic_memo)
- Title: Corporate and Organizational Structure — Helix Specialty Chemicals
- Date: 2025-12-01
- Summary: Investment Committee memorandum detailing the corporate legal entity structure, organizational reporting hierarchy, headcount breakdown, distribution center footprint, and equity ownership structure for Helix Specialty Chemicals (Project Aurora). The company is 100% family-owned through Beckwith Family Holdings, LLC, with Tom Beckwith serving as CEO and voting trustee. Total headcount is 1,140 across 8 distribution centers (U.S. and Canada). All family shareholders have authorized a sale process via Lazard Middle Market. Tom Beckwith has indicated willingness to roll 15–20% of proceeds into the post-close capital structure and remain CEO for an 18-month transition.
- deal_context (confidence=0.85): company=Helix Specialty Chemicals, sector=specialty_chemicals, subsector=specialty_intermediates
- <details><summary>⚠ extraction warnings</summary>

  - doc_type overridden from folder hint 'dd_report' to 'ic_memo' based on explicit document header: 'Investment Committee Memorandum' and 'IC Use Only' designation.
  - No financial metrics (revenue, EBITDA, EV) are present in this document; all financial structured fields set to null.
  - Date defaulted to 2025-12-01 from 'December 2025' cover page (no specific day provided).
  - Subsector 'specialty_intermediates' is an imperfect fit — Helix is primarily a specialty chemicals distributor/blender, not a producer of intermediates. Taxonomy proposal filed.

  </details>

### `Financial Model/Aurora_LBO_Model_v1.xlsx` → `doc_project_aurora_009` (financial_model)
- Title: Project Aurora — LBO Model (Base Case)
- Date: 2026-01-01
- Summary: LBO financial model for Project Aurora prepared by Atlas Crossing Partners Fund IV in January 2026, with an anticipated entry date of April 14, 2026. The model reflects a $1.1B enterprise value acquisition of a company (founder Tom Beckwith / Beckwith family) at an implied 11.6x LTM EBITDA multiple ($95M LTM Adj. EBITDA). Debt financing is led by a $580M senior unitranche (Antares + Twin Brook), with $145M Atlas Crossing equity and $123M Beckwith rollover equity. The base case projects revenue growing from $725M LTM to ~$1.19B by FY30, with EBITDA margins expanding from ~13.1% to ~16.3%. The model includes bolt-on M&A assumptions ($25M–$135M annual bolt-on revenue), organic growth decelerating from 8% to 5.5%, and $405M in total debt paydown over the 5-year hold. Returns sensitivity spans a downside exit at $110M EBITDA / 9.5x to an upside of $180M EBITDA / 12.5x.
- deal_context (confidence=0.92): company=Project Aurora (Aurora), sector=None, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - Entry multiple cell was blank in the source sheet; computed as $1,100M EV / $95M LTM EBITDA = 11.58x and populated in ev_ebitda_multiple.
  - Total sources and total uses rows were blank (formula cells); implied totals are $848M sources and $1,199M uses — slight gap may reflect rounding or missing line items in the rendered markdown.
  - Gross profit, EBITDA, EBITDA margin %, MOIC, and Gross IRR cells are blank (formula-driven) in the rendered markdown; values not directly extracted.
  - Revenue CAGR 3yr computed from FY22A ($540M) to FY24A ($686M) actual data: ~12.6% 2-year CAGR; alternatively FY22A–FY25 LTM ~10.3% 3-year CAGR — the latter used.
  - Date extracted as January 2026 from 'Prepared January 2026' banner; no specific day available, defaulted to 2026-01-01.
  - Sector and geography cannot be determined from the financial model alone; left null in deal_context.
  - Founder name (Tom Beckwith) and family trust rollover are identifiable PII — flagged for data handling review.

  </details>

### `Legal/Aurora_Term_Sheet_2026-01.pdf` → `doc_project_aurora_010` (ic_memo)
- Title: Indicative Term Sheet — Acquisition of Helix Specialty Chemicals, Inc. ("Project Aurora")
- Date: 2026-01-16
- Summary: Indicative (non-binding) term sheet issued January 16, 2026 by Atlas Crossing Partners Fund IV, L.P. for the acquisition of 100% of Helix Specialty Chemicals, Inc. via a stock purchase. Proposed enterprise value is $1.1 billion at 11.6x LTM Adjusted EBITDA (~$95M). Deal is structured with $580M senior unitranche debt (Antares + Twin Brook), $145M Atlas Crossing equity, $95M CEO rollover, and $28M Beckwith family trust rollover. Key conditions include HSR clearance, confirmatory diligence completion by March 28, 2026, and anticipated closing April 14, 2026. Notable features include a 10% management incentive pool, founder/CEO rollover (~14.5% pro-forma ownership), a Pennsylvania environmental matter (largely resolved), and R&W insurance with a $50M tower. Exclusivity runs through April 14, 2026.
- deal_context (confidence=0.92): company=Helix Specialty Chemicals, Inc., sector=specialty_chemicals, subsector=specialty_intermediates
- <details><summary>⚠ extraction warnings</summary>

  - doc_type hint was 'dd_report' but document content is clearly an indicative term sheet (legal/transactional document); classified as 'ic_memo' as the closest supported type, with a taxonomy_proposals entry for a dedicated 'term_sheet' type.
  - Revenue LTM not stated in the document; ebitda_margin left null as a result.
  - Geography set to northeast_us based on Pennsylvania environmental matter reference and Delaware incorporation; explicit HQ location not stated.
  - Subsector 'specialty_intermediates' chosen as best fit under specialty_chemicals but the specific sub-segment of Helix's chemicals business is not described in this term sheet.

  </details>

### `Presentations/data-room-cuts/Management_Presentation_Excerpt_2025-12.pdf` → `doc_project_aurora_011` (cim)
- Title: Project Aurora — Management Presentation (Excerpt)
- Date: 2025-12-12
- Summary: Management presentation excerpt for Project Aurora (Helix), the leading independent specialty chemicals distributor in North America. The Beckwith family-led executive team (CEO Tom Beckwith, CFO Sarah Markowicz, CCO Patricia Liang, COO Diego Rivera, VP M&A Mark Allen) outlines strategic priorities for 2026–2028, including category expansion in industrial and specialty water treatment, West Coast/PNW geographic expansion, technical sales force growth, custom-blending capacity investment ($8M capex), and disciplined M&A across adjacent product lines. Recent operational accomplishments include ERP implementation, DC network expansion, procurement consolidation (+220bps gross margin), and technical sales headcount growth. The company is seeking a PE partner to provide capital for M&A, operational expertise, and commercial transformation investment — signaling a classic founder/family transition platform deal. Lazard Middle Market is the sell-side advisor.
- deal_context (confidence=0.88): company=Helix, sector=specialty_chemicals, subsector=specialty_intermediates
- <details><summary>⚠ extraction warnings</summary>

  - Folder-based doc_type hint was 'ic_memo' but document content is clearly a Management Presentation prepared by the target company's executive team for sell-side diligence purposes; overriding to 'cim' as the closest matching doc_type.
  - No financial figures (revenue, EBITDA, margins) were included in this excerpt; structured financials are null.
  - Subsector 'specialty_intermediates' is an imperfect fit — Helix is a distributor, not a manufacturer; taxonomy proposal added.
  - Geography tagged as 'national' based on references to multiple DCs and North American positioning, though the company may skew to certain regions; no single sub-national region dominates the description.

  </details>

### `Presentations/investment-decks/ACP_Preliminary_IC_Review_2025-11.pdf` → `doc_project_aurora_012` (ic_memo)
- Title: Investment Committee Memorandum — Preliminary IC Review — Project Aurora
- Date: 2025-11-11
- Summary: Preliminary IC memorandum submitted by Atlas Crossing Partners (Fund IV) recommending advancement of Project Aurora — a specialty chemicals distributor (codename referencing "Helix") — to IOI submission at an indicative EV of $1.0B (10.5x LTM Adj. EBITDA of $95M). The target is a family-owned B2B specialty chemicals distribution platform being sold via a Lazard Middle Market limited auction. ACP's thesis centers on a fragmented distribution category, founder transition, bolt-on acquisition pipeline (4–6 targets), and $30M+ EBITDA improvement opportunity. Base case projects 2.7x MOIC / 23.5% IRR over a 5-year hold. Key risks include entry valuation discipline, oil & gas end-market cyclicality, supplier concentration (top 25 = 64% of COGS), and CEO succession. Diligence workstreams (QofE via EY, CDD via Bain, legal via K&E, IT via Crowe) are in process or pending.
- deal_context (confidence=0.95): company=Helix, sector=specialty_chemicals, subsector=process_chemicals
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue not disclosed in the document; ebitda_margin cannot be computed.
  - The document references the target by both codename 'Aurora' and apparent operating name 'Helix' (used in comps narrative); company_canonical set to 'Helix' but this should be confirmed against other deal folder documents.
  - ev_proposed_usd set to $1.0B (low end / IOI bid price) per recommendation; indicative range is $1.0B–$1.2B.
  - Subsector 'process_chemicals' used as closest existing value; target is a distributor, not a manufacturer — see taxonomy_proposals for gap.
  - Document mentions 'supplier concentration' risk which maps closest to 'customer_concentration' risk theme in taxonomy; a 'supplier_concentration' risk_theme would be more precise but is not available.

  </details>

## Resolver disagreements

### company_canonical
- Chosen: `Helix Specialty Chemicals, Inc.` (plurality 2/5; tied 2-way, broke tie by confidence sum)
- Voters for chosen: ['Banker Materials/cim/CIM_Helix_Specialty_Chemicals_2025-12.pdf', 'Legal/Aurora_Term_Sheet_2026-01.pdf']
- Dissent `Project Aurora (Beckwith family specialty chemicals distributor)`: ['Banker Materials/teaser/Teaser_Lazard_2025-11.pdf', 'Financial Model/Aurora_LBO_Model_v1.xlsx']
- Dissent `Helix`: ['Presentations/investment-decks/ACP_Preliminary_IC_Review_2025-11.pdf']

### subsector
- Chosen: `specialty_intermediates` (plurality 2/4; tied 2-way, broke tie by confidence sum)
- Voters for chosen: ['Banker Materials/cim/CIM_Helix_Specialty_Chemicals_2025-12.pdf', 'Legal/Aurora_Term_Sheet_2026-01.pdf']
- Dissent `process_chemicals`: ['Banker Materials/teaser/Teaser_Lazard_2025-11.pdf', 'Presentations/investment-decks/ACP_Preliminary_IC_Review_2025-11.pdf']

### geography
- Chosen: `national` (plurality 3/4)
- Voters for chosen: ['Banker Materials/cim/CIM_Helix_Specialty_Chemicals_2025-12.pdf', 'Banker Materials/teaser/Teaser_Lazard_2025-11.pdf', 'Presentations/investment-decks/ACP_Preliminary_IC_Review_2025-11.pdf']
- Dissent `northeast_us`: ['Legal/Aurora_Term_Sheet_2026-01.pdf']

### financials.revenue_cagr_3yr
- Chosen: `0.148` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Banker Materials/cim/CIM_Helix_Specialty_Chemicals_2025-12.pdf']
- Dissent `0.1025`: ['Financial Model/Aurora_LBO_Model_v1.xlsx']

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- doc_type: proposed=`advisor_engagement_summary` (used `ic_memo`, confidence=0.75)
  - rationale: This document is an IC-facing advisor engagement and workstream summary memo — a distinct document type that combines elements of an IC memo and a project management tracker. It is closer to ic_memo than dd_report given its IC addressee and decision-required framing.
- subsector: proposed=`specialty_chemicals_distribution` (used `specialty_intermediates`, confidence=0.82)
  - rationale: Helix is described explicitly as a specialty chemicals distributor, not a manufacturer of specialty intermediates. The taxonomy has no distribution-specific subsector under specialty_chemicals. 'specialty_intermediates' is the closest existing value but imperfectly captures a distribution/go-to-market model. A dedicated 'specialty_chemicals_distribution' subsector would better reflect this business.
- deal_type: proposed=`founder_family_sale` (used `platform`, confidence=0.8)
  - rationale: This is a full sale of a family-owned platform business (3rd generation ownership exit). 'platform' is the closest existing deal_type as it is a standalone scale business being brought to market, but a 'founder_family_sale' or 'family_exit' type would more precisely describe the transaction dynamic.
- risk_theme: proposed=`founder_transition` (used `management_quality`, confidence=0.82)
  - rationale: The document prominently features a 3rd-generation family owner/CEO transition as a central deal thesis driver and risk. The existing taxonomy has 'management_quality' as the closest risk theme, but 'founder_transition' better captures the succession/ownership-change risk dimension. Note: founder_transition also appears as a thesis_theme in the taxonomy.
- doc_type: proposed=`customer_concentration_analysis` (used `dd_report`, confidence=0.65)
  - rationale: This is an xlsx workbook containing a structured customer concentration analysis, a specific due diligence data room artifact. The folder hint suggests dd_report and it is clearly a diligence-related document, but it is more precisely a financial/operational data file than a narrative DD report.
- subsector: proposed=`specialty_distribution_chemicals` (used `specialty_intermediates`, confidence=0.62)
  - rationale: Helix Specialty Chemicals operates as a specialty chemical distributor and blender, which sits closer to specialty distribution than a pure specialty intermediates manufacturer. However, specialty_intermediates under specialty_chemicals is the best available fit in the current taxonomy.
- doc_type: proposed=`operations_overview` (used `ic_memo`, confidence=0.75)
  - rationale: The document is explicitly titled an 'Investment Committee Memorandum — Operations Overview' and is filed in the Data Room. While the folder hint suggests dd_report, the document's header clearly labels it as an IC Memo. ic_memo is more accurate than dd_report, though a distinct 'operations_dd_report' or 'ops_memo' type would better capture this hybrid format.
- subsector: proposed=`specialty_distribution` (used `specialty_intermediates`, confidence=0.62)
  - rationale: Helix operates as a specialty chemicals distributor with custom-blending capabilities. 'specialty_distribution' would be a better fit, but it belongs to industrial_distribution sector in the taxonomy. Under specialty_chemicals, 'specialty_intermediates' is the closest available subsector, though Helix's business model is more distribution-oriented than intermediates manufacturing.
- doc_type: proposed=`org_structure_memo` (used `ic_memo`, confidence=0.88)
  - rationale: This document is labeled 'Investment Committee Memorandum' on its cover, making ic_memo the correct classification. The folder hint suggested dd_report, but the document header and 'IC Use Only' designation override that. No separate org_structure doc_type exists in the taxonomy.
- doc_type: proposed=`term_sheet` (used `ic_memo`, confidence=0.85)
  - rationale: This document is a formal indicative term sheet setting out acquisition terms — a distinct document type not represented in the current taxonomy. ic_memo is the closest existing type as it is a structured deal-decision document, but a dedicated 'term_sheet' type would more accurately classify legal/commercial term sheets in deal folders.
- doc_type: proposed=`management_presentation` (used `cim`, confidence=0.9)
  - rationale: The document is explicitly titled a Management Presentation excerpt prepared by the Helix executive team for the diligence room, coordinated by Lazard Middle Market. It is not an IC memo (the folder hint) nor a traditional CIM, but most closely resembles a CIM in function (company marketing/positioning for prospective buyers). A 'management_presentation' doc_type would more precisely classify this category of document.
