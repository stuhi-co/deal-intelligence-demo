# Ingestion report — Project Everest

Deal ID: `deal_project_everest_2026`
Company canonical: `Ridgeline Pet Co.`
Sector / subsector: `consumer_products` / `pet_supplies`
Geography: `national`
Deal type: `platform`
Voted with 5 qualifying docs at confidence >= 0.9 (out of 12 tagged).

## Triage

### primary (12)
- `Advisors/Everest Advisor Engagement Summary 2026-02.pdf` [hint: dd_report]
- `Banker Materials/CIM/CIM Ridgeline Pet Co 2025-11.pdf` [hint: cim]
- `Banker Materials/Teaser/Teaser Lincoln International 2025-10.pdf` [hint: cim]
- `Data Room/Customers/Everest Top 50 Customer Analysis.xlsx` [hint: dd_report]
- `Data Room/Financials/Everest Historical Financials 2020-2025.xlsx` [hint: financial_model]
- `Data Room/Legal/Everest Legal Diligence Summary 2026-02.pdf` [hint: dd_report]
- `Data Room/Operations/Everest Operations Overview 2025-12.pdf` [hint: dd_report]
- `Data Room/Org Structure/Everest Org Structure 2025-12.pdf`
- `Financial Model/Everest LBO Model_v1.xlsx` [hint: financial_model]
- `Legal/Everest Final Round Process Letter 2026-02.pdf` [hint: dd_report]
- `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-12.pdf`
- `Presentations/Investment Decks/ACP Preliminary IC Review 2026-01.pdf`

### format_duplicate (9)
- `Advisors/Everest Advisor Engagement Summary 2026-02.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Banker Materials/CIM/CIM Ridgeline Pet Co 2025-11.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Banker Materials/Teaser/Teaser Lincoln International 2025-10.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Data Room/Legal/Everest Legal Diligence Summary 2026-02.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Data Room/Operations/Everest Operations Overview 2025-12.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Data Room/Org Structure/Everest Org Structure 2025-12.docx` — PDF preferred over DOCX/PPTX twin
- `Legal/Everest Final Round Process Letter 2026-02.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-12.docx` — PDF preferred over DOCX/PPTX twin
- `Presentations/Investment Decks/ACP Preliminary IC Review 2026-01.docx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Advisors/Everest Advisor Engagement Summary 2026-02.pdf` → `doc_project_everest_001` (dd_report)
- Title: Project Everest — Advisor Engagement Summary
- Date: 2026-03-01
- Summary: Internal advisor engagement summary prepared by Atlas Crossing Partners (ACP) for Project Everest (March 2026). Documents the full diligence workstream team including M&A legal (Kirkland & Ellis), Quality of Earnings (EY Transaction Advisory), tax (KPMG), technology/IT (West Monroe Partners), insurance/R&W (Marsh McLennan), and regulatory (Covington & Burling). Also identifies the sell-side banker (Lincoln International). Tracks key process milestones from teaser receipt (October 2025) through a target signing date of April 18, 2026. As of document date, ACP has advanced to the final round, with QofE and legal/IT diligence in progress, final bid due March 15, 2026.
- deal_context (confidence=0.85): company=None, sector=None, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - Doc classified as dd_report per folder hint; content is an advisor engagement/process tracker rather than a substantive diligence findings report — consider a 'process_summary' doc_type if added to taxonomy.
  - No financial figures present in this document.
  - Date on document is March 2026; using 2026-03-01 as approximation.
  - Regulatory scope mentions 'nutrition labeling' suggesting possible consumer products / food & beverage sector, but insufficient evidence to confirm sector with high confidence — sector and subsector left to resolver.
  - Mention of 'Ridge OS review' under Technology/IT diligence may be a proprietary platform name relevant to tech-enabled services classification.

  </details>

### `Banker Materials/CIM/CIM Ridgeline Pet Co 2025-11.pdf` → `doc_project_everest_002` (cim)
- Title: Project Everest — Confidential Information Memorandum: Ridgeline Pet Co.
- Date: 2025-11-01
- Summary: CIM prepared by Lincoln International for Ridgeline Pet Co. ("Project Everest"), a premium direct-to-consumer and marketplace pet supply platform headquartered in Austin, TX. Founded in 2016 by Amanda Torres (former P&G brand manager), Ridgeline sells proprietary nutrition, wellness, and enrichment products for dogs and cats via a subscription-first DTC model and marketplace/retail channels. LTM revenue of $192M (28% 5-yr CAGR), LTM Adj. EBITDA of $42M (21.9% margin), and 310K+ active subscribers. Private-label accounts for 44% of revenue at 58% gross margin. The transaction is structured as a 100% sale at an indicative EV of $420M (~10x LTM EBITDA). Founder Amanda Torres holds 31% equity and is rolling into the new structure. Key highlights include best-in-class AutoShip churn (4.8%), strong LTV/CAC ratio (11.4x), proprietary Ridge OS subscription platform, and white space in brick-and-mortar and international markets.
- deal_context (confidence=0.95): company=Ridgeline Pet Co., sector=consumer_products, subsector=pet_supplies
- <details><summary>⚠ extraction warnings</summary>

  - revenue_cagr_3yr field populated with the 5-year CAGR of 28% as stated in the CIM ('28% five-year CAGR'); a strict 3-year CAGR is not explicitly broken out but can be approximated from the table (~40% FY21-FY24) — using the stated 5-yr figure as the best available label.
  - ev_ebitda_multiple of 10.0x is derived from indicative EV of $420M / LTM EBITDA of $42M; the CIM does not explicitly state this multiple.
  - Ridgeline's product mix spans both pet_food and pet_supplies subsectors; pet_supplies selected as the broader/closer fit given enrichment accessories and wellness products, but pet_food is a significant revenue component.
  - Bid deadline is March 15, 2026 and anticipated close is Q2 2026 — document date inferred as November 2025 from filename and 'November 2025' on cover page.

  </details>

### `Banker Materials/Teaser/Teaser Lincoln International 2025-10.pdf` → `doc_project_everest_003` (cim)
- Title: Project Everest — Confidential Teaser
- Date: 2025-10-01
- Summary: Lincoln International sell-side teaser for Project Everest, identifying the target as Ridgeline Pet Co., a vertically integrated DTC and marketplace pet supply platform. The company generates $192M in LTM revenue and $42M in LTM Adj. EBITDA (21.9% margin), with a 28% revenue CAGR since FY2021. Key investment highlights include a high-retention AutoShip subscription program (58% of DTC revenue, 94% annual retention), premium pet-owner customer base, strong LTV/CAC of 11.4x, and a 44% private-label revenue mix. Multi-channel distribution spans DTC (62%), Amazon/Chewy marketplaces (24%), and independent specialty retail (14%). The process is banker-run with final bids due March 15, 2026.
- deal_context (confidence=0.95): company=Ridgeline Pet Co., sector=consumer_products, subsector=pet_supplies
- <details><summary>⚠ extraction warnings</summary>

  - Doc type hint was 'cim' but document content is clearly a teaser (short-form, no detailed financials or business section depth); tagged as 'cim' per closest available doc_type — taxonomy does not include 'teaser' as a distinct doc_type.
  - Revenue CAGR stated as FY21–LTM (28%), which spans approximately 3–4 years; treated as revenue_cagr_3yr as the closest mapping.
  - No EV or entry multiple disclosed in teaser; ev_proposed_usd and ev_ebitda_multiple left null.
  - Process timeline references dates in 2026 (bids, management presentations) despite document date of October 2025, consistent with a sell-side process launched in late 2025.

  </details>

### `Data Room/Customers/Everest Top 50 Customer Analysis.xlsx` → `doc_project_everest_004` (dd_report)
- Title: Project Everest — Top 50 Customer Analysis
- Date: 2025-11-30
- Summary: Detailed breakdown of Project Everest's top 50 customers/cohorts by LTM revenue through November 2025, spanning DTC subscription cohorts, marketplace accounts (Amazon, Chewy, Walmart), retail pilots (PetSmart, Target, Costco, Petco), independent specialty retailers, veterinary clinic channels, and corporate/gifting accounts. The top 5 customers/cohorts account for ~$94.8M of the ~$164.2M total revenue represented in this analysis, with DTC AutoShip subscriber cohorts dominating the top rankings. No single customer/cohort exceeds ~17% of LTM revenue, indicating moderate concentration. The business appears to be a premium pet nutrition/wellness brand ("Ridge" brand) with a strong DTC subscription engine and nascent retail expansion.
- deal_context (confidence=0.82): company=Ridge (pet nutrition/wellness), sector=consumer_products, subsector=pet_food
- <details><summary>⚠ extraction warnings</summary>

  - Document is an xlsx workbook rendered as markdown tables; key_quotes left empty per rules.
  - Doc-type hint was dd_report but content is a financial/customer data workbook from the Data Room. Classified as dd_report (closest match) since financial_model is reserved for LBO/financial models; taxonomy proposal added for 'customer_analysis' doc type.
  - LTM revenue total (~$164.2M) was computed by summing all 50 rows from the LTM Revenue ($M) column; this is the top-50 customer subset, not necessarily total company revenue.
  - % LTM Rev column was blank in source data; concentration percentages were not explicitly provided.
  - Date inferred as November 2025 from the banner row 'LTM through November 2025'; exact day set to month-end (2025-11-30).
  - The 'Ridge' brand (Ridge Collection, Ridge Nutrition, Ridge Wellness, Ridge Nutrition Pro, Ridge Nutrition Rx) is referenced throughout — interpreted as the company's primary brand.
  - Subsector set to 'pet_food' (closest available under consumer_products) though the company also sells supplements/wellness products, which could warrant a 'pet_supplements' or 'pet_wellness' subsector proposal.

  </details>

### `Data Room/Financials/Everest Historical Financials 2020-2025.xlsx` → `doc_project_everest_005` (financial_model)
- Title: Project Everest — Historical Financials (FY20–LTM)
- Date: 2025-11-30
- Summary: Historical income statement and revenue channel breakdown for Project Everest covering FY2020 through LTM (November 2025). Revenue grew from $38M in FY20 to $192M LTM, representing strong multi-year growth. The business is heavily DTC-driven, with AutoShip (subscription) revenue the dominant channel at $136M LTM out of $192M total. Key opex lines include Sales & Marketing, G&A, Technology/Platform, and Fulfillment. Reported EBITDA cells are blank in the rendered workbook but can be derived: LTM EBITDA (reported) = Revenue $192M minus COGS $100M minus S&M $52M minus G&A $18M minus Tech $16M minus Fulfillment $24M = –$18M. Adj. EBITDA adds back ~$9M in adjustments (founder comp, one-time, stock/phantom equity, fulfillment ramp) yielding approximately –$9M Adj. EBITDA LTM, implying the business is not yet EBITDA-positive on an LTM basis. A large fulfillment ramp add-back of $5.4M is notable. Revenue CAGR from FY20 to FY24 (4 years) is approximately 46% (38→172). Audited by RSM US LLP for FY20–FY24.
- deal_context (confidence=0.82): company=None, sector=consumer_products, subsector=pet_food
- <details><summary>⚠ extraction warnings</summary>

  - EBITDA (reported) and Adj. EBITDA rows are blank in the rendered workbook; values were derived by calculation from the available line items. Derived LTM reported EBITDA = -$18M; Adj. EBITDA = ~-$9M after $9.0M in add-backs.
  - Gross profit and gross margin % rows are blank; derived LTM gross profit = $92M (~47.9% margin).
  - Revenue CAGR column in the channel sheet is blank; CAGR values were not computed here.
  - YoY growth % row is blank in the income statement.
  - Subsector tagged as 'pet_food' based on channel names (AutoShip, Amazon, Chewy) and gifting language consistent with a DTC pet food/consumables brand; no explicit product category stated in the document.
  - ebitda_margin is negative (-4.7%) based on derived Adj. EBITDA of ~-$9M on $192M revenue — company is pre-profitability on EBITDA basis.
  - revenue_cagr_3yr computed as FY22→FY24/LTM approximate 3-year window (102→192M), yielding ~23.5% CAGR — using 3yr window FY21→FY24 gives ~35.5%; value of 0.257 represents FY22-LTM annualized approximation.
  - LTM period is through November 2025, not a full calendar or fiscal year-end.

  </details>

### `Data Room/Legal/Everest Legal Diligence Summary 2026-02.pdf` → `doc_project_everest_006` (dd_report)
- Title: Project Everest — Legal Diligence Summary
- Date: 2026-02-01
- Summary: Latham & Watkins LLP prepared a preliminary legal diligence summary for Atlas Crossing Partners on Ridgeline Pet Co. (Project Everest). The review covers corporate structure, material contracts, IP, employment, and litigation. Key findings: clean Delaware C-corp structure with no subsidiaries; change-of-control consent required on two fulfillment center leases; Amazon marketplace policy risk flagged for IC; strong IP position with 6 registered trademarks and 2 patents; no CBAs and key executives (CEO/CFO) committed post-close; one pending consumer class action with estimated exposure <$1.5M covered by insurance. Outstanding items include change-of-control consents, CCPA audit, FDA/FTC marketing claim review, and tax diligence not yet initiated.
- deal_context (confidence=0.88): company=Ridgeline Pet Co., sector=consumer_products, subsector=pet_food
- <details><summary>⚠ extraction warnings</summary>

  - Date defaulted to 2026-02-01 (first of month) as only month/year ('February 2026') was specified in the document.
  - No financial metrics (revenue, EBITDA, EV) were present in this legal diligence summary; all financial structured fields set to null.
  - Deal type inferred as 'platform' based on context (Atlas Crossing Partners as PE buyer, full acquisition of Ridgeline Pet Co.); not explicitly stated in document.
  - Subsector set to 'pet_food' based on references to kibble cold-press process and supplement SKUs; document does not explicitly state product category.

  </details>

### `Data Room/Operations/Everest Operations Overview 2025-12.pdf` → `doc_project_everest_007` (dd_report)
- Title: Project Everest — Operations Overview
- Date: 2025-12-01
- Summary: Operations overview for Ridgeline Pet Co. (Project Everest), dated December 2025. Covers the company's two operational fulfillment centers (Austin, TX and Harrisburg, PA) with a third planned in Phoenix, AZ (Q4 2026). Details the private-label supply chain (3 co-manufacturers with multi-year agreements), the proprietary Ridge OS subscription/personalization platform (310K+ active subscriptions, 2.8M+ annual orders), and strong customer experience metrics (NPS 74, 94% AutoShip retention). Key operational risks identified include co-manufacturer concentration (top 2 supply 78% of private-label volume), Austin FC capacity constraints at 91% peak utilization, and Amazon marketplace policy risk around subscription-to-DTC funnel migration.
- deal_context (confidence=0.92): company=Ridgeline Pet Co., sector=consumer_products, subsector=pet_supplies
- <details><summary>⚠ extraction warnings</summary>

  - Doc type hint was dd_report; content is an operations overview data room document, consistent with dd_report classification — no override needed.
  - No financial metrics (revenue, EBITDA, margins) are present in this document; all financial structured fields left null.
  - Deal type inferred as 'platform' from context (primary company overview) but not explicitly stated in this document.
  - Co-manufacturer concentration risk mapped to customer_concentration (closest existing) — see taxonomy_proposals for proposed new risk_theme.
  - Amazon marketplace policy risk mapped to regulatory_exposure (closest existing) — see taxonomy_proposals for proposed new risk_theme.

  </details>

### `Data Room/Org Structure/Everest Org Structure 2025-12.pdf` → `doc_project_everest_008` (dd_report)
- Title: Project Everest — Organizational Structure: Ridgeline Pet Co. — As of December 2025
- Date: 2025-12-01
- Summary: Organizational structure document for Project Everest (Ridgeline Pet Co.) as of December 2025. Details the senior leadership team (7 named executives including founder/CEO Amanda Torres), a headcount summary of 254 FTEs across 8 departments, and pre-transaction equity ownership. Key observations: founder is rolling ~19% post-close; institutional Series A/B investors and angel/seed investors are fully exiting; employee option pool is partially retained. The org reflects a DTC-oriented pet products company with meaningful technology investment (Ridge OS subscription platform, ML personalization) and a two-fulfillment-center operations footprint.
- deal_context (confidence=0.85): company=Ridgeline Pet Co., sector=consumer_products, subsector=pet_supplies
- <details><summary>⚠ extraction warnings</summary>

  - No explicit doc_type hint provided; classified as dd_report (org structure diligence document) rather than cim or ic_memo based on content detail and format.
  - Subsector 'pet_supplies' selected; Ridgeline Pet Co. appears to sell pet products via DTC/subscription — could also involve 'pet_food' depending on product mix, but org structure does not specify. Pet_supplies chosen as the broader fit.
  - Date inferred as 2025-12-01 from 'As of December 2025' in the document header; exact day unknown.
  - No financial metrics present in this document; all numeric structured fields are null.

  </details>

### `Financial Model/Everest LBO Model_v1.xlsx` → `doc_project_everest_009` (financial_model)
- Title: Project Everest — LBO Model (Base Case)
- Date: 2026-02-28
- Summary: LBO financial model for Project Everest, prepared by Atlas Crossing Partners Fund IV in February 2026. The model covers a base-case transaction with a June 2026 entry date, $420M enterprise value, $42M LTM Adj. EBITDA (10.0x entry multiple), and $192M LTM revenue. The capital structure includes $220M senior secured TLB (Owl Rock Capital), $90M ACP equity, ~19% founder rollover from A. Torres (~$80M), and 12% management/employee rollover (~$50M). A subscriber cohort model tracks AutoShip subscribers (310K LTM, ~5% churn), LTV/CAC dynamics, and per-subscriber economics. The P&L projects revenue growing from $192M (LTM) to $420M by FY30B, with EBITDA margins expanding from ~21.9% (LTM implied) to ~26.9% (FY30B). The returns sensitivity table spans three scenarios (Downside: 10x exit / $80M EBITDA; Base: 12.5x / $113M; Upside: 14x / $138M) over a 5-year hold. Key drivers include AutoShip subscriber growth, private label mix expansion, and S&M leverage.
- deal_context (confidence=0.82): company=Project Everest, sector=consumer_products, subsector=pet_food
- <details><summary>⚠ extraction warnings</summary>

  - Entry multiple cell in Summary sheet appears to be a formula placeholder (blank) — calculated as $420M EV / $42M EBITDA = 10.0x by analyst
  - Revenue CAGR 3yr estimated from FY22A ($102M) to FY24A ($172M) implied ~29.8%; using FY23A–LTM as proxy ~18.1%; reported as ~23.4% blended FY22A-FY24A CAGR
  - AutoShip churn rows in Subscriber Model contain raw formula strings (e.g., -=B5*0.055) rather than resolved values — churn rates taken from the 'Annual churn rate' row instead
  - Total sources and total uses cells are blank formula placeholders in the model
  - ACP proceeds, MOIC, and Gross IRR cells in returns sensitivity table are blank formula outputs — not extractable from rendered markdown
  - Date defaulted to 2026-02-28 (end of February 2026) based on 'Prepared February 2026' banner; exact day not stated
  - Subsector tagged as pet_food based on AutoShip subscriber model and consumer product nature; actual product category (pet food vs. pet supplies vs. mixed) not explicitly confirmed in this workbook

  </details>

### `Legal/Everest Final Round Process Letter 2026-02.pdf` → `doc_project_everest_010` (dd_report)
- Title: Final Round Process Letter – Ridgeline Pet Co.
- Date: 2026-02-14
- Summary: Final round process letter issued by Lincoln International on behalf of Ridgeline Pet Co. (seller) to Atlas Crossing Partners (ACP) as a prospective buyer. The letter outlines the sale process timeline (bid deadline March 15, 2026; anticipated close Q2 2026 subject to HSR), bid requirements (fully marked SPA, committed financing, rollover equity summary, and outstanding reps redline), and key negotiating parameters including seller preference for 100% cash at closing, R&W insurance, escrow capped at 5% of EV with a 12-month tail, and no seller financing. The deal is subject to standard HSR review. No financial figures are provided in this document.
- deal_context (confidence=0.82): company=Ridgeline Pet Co., sector=consumer_products, subsector=pet_supplies
- <details><summary>⚠ extraction warnings</summary>

  - doc_type override recommended: folder hint is 'dd_report' but content is clearly a legal/process letter from Lincoln International governing the final round of a sale process — tagged as dd_report per closest available value, with taxonomy proposal filed.
  - No financial figures (revenue, EBITDA, EV) are present in this document.
  - deal_type set to 'platform' by default as no add-on or carve-out signals are present, but the document does not explicitly confirm deal structure.
  - subsector set to 'pet_supplies' as Ridgeline Pet Co. is a pet company; specific sub-category (food vs. supplies) is not confirmed in this document.

  </details>

### `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-12.pdf` → `doc_project_everest_011` (cim)
- Title: Project Everest — Ridgeline Pet Co. Management Presentation Excerpt (December 2025)
- Date: 2025-12-01
- Summary: Internal extract from Ridgeline Pet Co.'s December 2025 management presentation under Project Everest. The document covers the company's founding vision (pet-as-family, individualized pet supply experience), subscriber cohort and retention data (2021–2024 cohorts showing 79–93% 24-month retention and LTVs of $758–$840), a private-label expansion roadmap targeting 55%+ penetration by FY28 via two new product lines and SKU rationalization, fulfillment operations across two centers (Austin, TX and Harrisburg, PA) with a third planned in Phoenix, and a management Q&A addressing Amazon/Chewy marketplace dependency, CAC trends, and founder succession planning (Amanda Torres committed to a 4-year post-close agreement).
- deal_context (confidence=0.9): company=Ridgeline Pet Co., sector=consumer_products, subsector=pet_supplies
- <details><summary>⚠ extraction warnings</summary>

  - No financial metrics (revenue, EBITDA, margins, EV) were included in this excerpt; all financial structured fields left null.
  - doc_type overridden from hint '(none)' to 'cim' as closest match — document is a management presentation excerpt, which has no exact taxonomy equivalent.
  - Date set to 2025-12-01 as only month/year (December 2025) was available in the document header.
  - Subscriber LTV figures ($758–$840) and cohort retention data are available but do not map directly to standard structured financial fields.

  </details>

### `Presentations/Investment Decks/ACP Preliminary IC Review 2026-01.pdf` → `doc_project_everest_012` (ic_memo)
- Title: Project Everest — Preliminary IC Review
- Date: 2026-01-01
- Summary: Preliminary Investment Committee memorandum from Atlas Crossing Partners (ACP Fund IV) for Project Everest — Ridgeline Pet Co., a premium pet supply DTC subscription platform. ACP proposes to acquire 100% of the company at a $420M enterprise value (10.0x LTM Adj. EBITDA), deploying $90M of equity. The investment thesis centers on a durable subscription moat (94% annual AutoShip retention, 310K active subscribers), private-label margin expansion (44% → 55%+ of revenue by FY28), brick-and-mortar channel entry unlocking $40–60M TAM, and platform M&A potential via Ridge OS infrastructure. Key risks include marketplace customer concentration (Amazon/Chewy at 24% of revenue), digital CAC inflation (+18% YoY), founder dependency on Amanda Torres, and competitive intensity in premium pet DTC. Base case projects revenue growing from $232M (FY26) to $420M (FY30) with EBITDA margins expanding from 22.4% to 26.9%. Final-round bid due March 15, 2026; anticipated signing April 2026 and closing Q2 2026.
- deal_context (confidence=0.97): company=Ridgeline Pet Co., sector=consumer_products, subsector=pet_supplies
- <details><summary>⚠ extraction warnings</summary>

  - LTM EBITDA margin computed as $42M / $192M = 21.9%; document does not state LTM margin explicitly.
  - revenue_cagr_3yr not directly stated for historical period; forward CAGR FY26–FY29 implied ~18% but LTM historical CAGR not available in this document.
  - ebitda_margin in structured payload reflects LTM (21.9%); forward base-case margins range from 22.4% (FY26) to 26.9% (FY30).

  </details>

## Resolver disagreements

### financials.ebitda_ltm_usd
- Chosen: `42000000.0` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Banker Materials/CIM/CIM Ridgeline Pet Co 2025-11.pdf']
- Dissent `-9000000.0`: ['Data Room/Financials/Everest Historical Financials 2020-2025.xlsx']

### financials.ebitda_margin
- Chosen: `0.219` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Banker Materials/CIM/CIM Ridgeline Pet Co 2025-11.pdf']
- Dissent `-0.047`: ['Data Room/Financials/Everest Historical Financials 2020-2025.xlsx']

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- doc_type: proposed=`process_summary` (used `dd_report`, confidence=0.75)
  - rationale: This document is an advisor engagement and deal process tracker, not a diligence findings report. A distinct 'process_summary' or 'advisor_engagement' doc_type would better capture this category of deal administration documents.
- subsector: proposed=`pet_supplies` (used `pet_supplies`, confidence=0.75)
  - rationale: Ridgeline Pet Co. sells both pet food (nutrition products) and pet supplies/accessories. The CIM describes revenue across nutrition, treats, supplements, and enrichment accessories. While 'pet_supplies' is listed in the taxonomy under consumer_products, Ridgeline's primary revenue driver appears to be pet food/nutrition — 'pet_food' would be equally or more accurate. The deal spans both subsectors.
- doc_type: proposed=`customer_analysis` (used `dd_report`, confidence=0.72)
  - rationale: This is an Excel workbook containing a structured customer concentration/cohort analysis from the data room, which is a distinct artifact from a narrative DD report. It is more granular than a typical dd_report but has no closer match in the taxonomy.
- subsector: proposed=`dtc_subscription_consumables` (used `pet_food`, confidence=0.65)
  - rationale: Project Everest appears to be a DTC subscription consumables brand (likely pet food/treats given Chewy and AutoShip prominence). The taxonomy has 'pet_food' under consumer_products which is the closest fit, but a broader 'dtc_subscription_consumables' subsector would better capture the channel-driven, subscription-first business model.
- risk_theme: proposed=`platform_channel_risk` (used `customer_concentration`, confidence=0.72)
  - rationale: The Amazon Seller Central policy risk flagged for IC represents a channel/platform dependency risk (reliance on a third-party marketplace) that is distinct from traditional customer concentration. The closest existing taxonomy value is customer_concentration, but a dedicated 'platform_channel_risk' theme would better capture marketplace seller policy exposure.
- risk_theme: proposed=`co_manufacturer_concentration` (used `customer_concentration`, confidence=0.82)
  - rationale: The document identifies co-manufacturer concentration (top 2 suppliers = 78% of private-label volume) as a key operational risk. This is a supply-side concentration risk distinct from customer_concentration, which is demand-side. commodity_exposure is also a partial fit but doesn't capture the supplier dependency angle accurately.
- risk_theme: proposed=`marketplace_platform_dependency` (used `regulatory_exposure`, confidence=0.75)
  - rationale: Amazon TOS policy risk is flagged as a distinct operational/platform dependency risk (not strictly regulatory). The closest existing value is regulatory_exposure, which partially captures the external policy/rule-change nature of the risk.
- subsector: proposed=`direct_to_consumer_pet` (used `pet_food`, confidence=0.65)
  - rationale: The business appears to be a DTC subscription pet product company (AutoShip model, subscriber cohorts, LTV/CAC metrics). While pet_food is the closest existing subsector, the model's emphasis on subscription/AutoShip mechanics and potential pet supplies mix suggests a broader DTC pet category that doesn't map cleanly to pet_food alone.
- doc_type: proposed=`process_letter` (used `dd_report`, confidence=0.9)
  - rationale: This document is a sell-side M&A process letter issued by an investment bank, governing final round bid procedures. It is not a due diligence report; the closest available doc_type is dd_report, but a dedicated 'process_letter' or 'legal' type would be more accurate.
- doc_type: proposed=`management_presentation` (used `cim`, confidence=0.75)
  - rationale: This document is explicitly labeled a 'Management Presentation Excerpt,' which is a distinct document type in PE diligence distinct from a full CIM. The closest existing type is 'cim' as both are company-authored marketing/overview documents, but a dedicated 'management_presentation' type would be more precise.
