# Ingestion report — Project Cascade

Deal ID: `deal_project_cascade_2025`
Company canonical: `Project Cascade`
Sector / subsector: `consumer_products` / `packaged_food`
Geography: `west_us`
Deal type: `platform`
Voted with 3 qualifying docs at confidence >= 0.9 (out of 12 tagged).

## Triage

### primary (12)
- `Advisors/Cascade Advisor Engagement Summary 2025-12.pdf` [hint: dd_report]
- `Banker Materials/CIM/CIM Fieldstone Bakery Co 2025-10.pdf` [hint: cim]
- `Banker Materials/Teaser/Teaser Houlihan Lokey 2025-09.pdf` [hint: cim]
- `Data Room/Customers/Cascade Top 50 Account Analysis.xlsx` [hint: dd_report]
- `Data Room/Financials/Cascade Historical Financials 2020-2025.xlsx` [hint: financial_model]
- `Data Room/Legal/Cascade Legal Diligence Summary 2025-12.pdf` [hint: dd_report]
- `Data Room/Operations/Cascade Operations Overview 2025-12.pdf` [hint: dd_report]
- `Data Room/Org Structure/Cascade Org Structure 2025-12.pdf`
- `Financial Model/Cascade LBO Model_v1.xlsx` [hint: financial_model]
- `Legal/Cascade Phase 2 Process Letter 2025-11.pdf` [hint: dd_report]
- `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-11.pdf`
- `Presentations/Investment Decks/ACP Preliminary Screening Memo 2025-10.pdf`

### format_duplicate (9)
- `Advisors/Cascade Advisor Engagement Summary 2025-12.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Banker Materials/CIM/CIM Fieldstone Bakery Co 2025-10.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Banker Materials/Teaser/Teaser Houlihan Lokey 2025-09.docx` [hint: cim] — PDF preferred over DOCX/PPTX twin
- `Data Room/Legal/Cascade Legal Diligence Summary 2025-12.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Data Room/Operations/Cascade Operations Overview 2025-12.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Data Room/Org Structure/Cascade Org Structure 2025-12.docx` — PDF preferred over DOCX/PPTX twin
- `Legal/Cascade Phase 2 Process Letter 2025-11.docx` [hint: dd_report] — PDF preferred over DOCX/PPTX twin
- `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-11.docx` — PDF preferred over DOCX/PPTX twin
- `Presentations/Investment Decks/ACP Preliminary Screening Memo 2025-10.docx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Advisors/Cascade Advisor Engagement Summary 2025-12.pdf` → `doc_project_cascade_001` (ic_memo)
- Title: Engagement and Workstream Summary — Project Cascade — Phase 2 Diligence
- Date: 2025-12-01
- Summary: Investment Committee memorandum summarizing the advisor engagements and diligence milestones for Project Cascade Phase 2. Six advisors are active: Kirkland & Ellis (legal/IP/food regulatory), LEK Consulting (commercial diligence), Deloitte (Quality of Earnings), Stoel Rives (food regulatory/FDA/organic certification), Antares Capital (debt financing), and Aon (R&W insurance). Key milestones include final bid submission on Jan 9, 2026, LOI execution targeted Jan 23, 2026, confirmatory diligence completion by Feb 14, 2026, definitive agreement execution by Mar 7, 2026, and close targeted Q2 2026. Document compiled by Alexis Huang (VP) and reviewed by Rachel Saunders (MD), dated December 2025.
- deal_context (confidence=0.85): company=None, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint was 'dd_report' but content is clearly an Investment Committee memorandum summarizing advisor engagements and diligence milestones — classified as 'ic_memo'.
  - Date defaulted to 2025-12-01 (month-level precision only; no specific day stated on cover).
  - Deal type inferred as 'platform' based on context clues (food/organic sector, Phase 2 diligence, full advisor slate) but not explicitly stated in document.
  - Sector/subsector inferred from food regulatory and organic certification references; no company name or financials disclosed.

  </details>

### `Banker Materials/CIM/CIM Fieldstone Bakery Co 2025-10.pdf` → `doc_project_cascade_002` (cim)
- Title: Confidential Information Memorandum – Fieldstone Bakery Co. ("Project Cascade")
- Date: 2025-10-01
- Summary: Houlihan Lokey CIM for Fieldstone Bakery Co. ("Project Cascade"), a premium artisan bakery brand founded in 2011 in Portland, OR by Laura Chen. The Company generates $160M LTM revenue and $32M LTM Adj. EBITDA (20.0% margin) across four channels: DTC subscription (Cascade Crate, 38% of revenue), specialty retail/grocery (40%), foodservice/wholesale (16%), and one-time DTC (6%). Fieldstone has 185,000 active subscribers, 4,200 retail doors nationally, and operates two production facilities (Portland and Austin). The sale is founder-initiated (100% owner), with Laura Chen rolling 20–25% of proceeds and staying on as Chief Brand Officer. Key investment themes include a high-LTV DTC subscription engine (LTV/CAC of 12.9x, 6.2% monthly churn), premium brand equity, clean-label tailwinds, and an East Coast expansion opportunity (~$22M capex, Q3 2027). Revenue CAGR FY22–LTM is ~14%; management projects acceleration to ~21% through FY27E with EBITDA margins expanding to 22.5%. Transaction process targets LOI in January 2026 and close in Q2 2026.
- deal_context (confidence=0.95): company=Fieldstone Bakery Co., sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - revenue_cagr_3yr estimated from FY22A ($108M) to LTM ($160M) over ~3 years, yielding ~14.0% CAGR; no explicit 3-year CAGR figure was stated in the document
  - ev_proposed_usd and ev_ebitda_multiple not disclosed in CIM; valuation/pricing will appear in later-stage documents
  - Date set to 2025-10-01 based on 'October 2025' cover page; exact day not specified

  </details>

### `Banker Materials/Teaser/Teaser Houlihan Lokey 2025-09.pdf` → `doc_project_cascade_003` (cim)
- Title: Project Cascade — Confidential Teaser | Houlihan Lokey Consumer Group
- Date: 2025-09-01
- Summary: Sell-side teaser for Project Cascade, a premium artisan bakery brand (DTC + specialty retail + foodservice) being sold by founder Laura Chen (age 49) via Houlihan Lokey. The company generated $160M LTM revenue and $32M LTM Adj. EBITDA (20.0% margin), with revenue growing from $108M in FY22 at a ~14% 3-year CAGR. Key highlights include a 185,000-subscriber DTC "Cascade Crate" box (38% of revenue, 28% YoY growth), 4,200 retail doors including Whole Foods and Target, clean-label/organic-certified products anchored by a 50-year-old sourdough starter, and a margin expansion roadmap to 22%+ via an East Coast facility (FY27) and continued DTC mix shift. Founder will roll 20–25% equity and remain as Chief Brand Officer. IOIs due October 10, 2025; expected close Q1–Q2 2026.
- deal_context (confidence=0.92): company=Project Cascade, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Doc type hint was 'cim' but this is clearly a teaser (shorter format, no detailed financials beyond summary table, explicit 'Confidential teaser' label) — classified as 'cim' as it is the closest available doc_type and no 'teaser' type exists in the taxonomy.
  - revenue_cagr_3yr computed manually from FY22 ($108M) to LTM ($160M) over ~3 years ≈ 14%; not explicitly stated in document.
  - ev_proposed_usd and ev_ebitda_multiple not disclosed in teaser.
  - Geography tagged as 'west_us' but company has national retail presence (Whole Foods national, Target premium bakery) and an Austin, TX facility — 'national' could also apply; 'west_us' chosen given HQ and brand origin in Portland, OR.

  </details>

### `Data Room/Customers/Cascade Top 50 Account Analysis.xlsx` → `doc_project_cascade_004` (dd_report)
- Title: Project Cascade — Top 50 Account Analysis
- Date: 2025-10-31
- Summary: This workbook presents the top 50 accounts for Project Cascade, covering LTM revenue through October 2025 across a mix of DTC subscription cohorts, retail partners, wholesale distributors, foodservice accounts, and one-time/gifting channels. The top 50 accounts span five channel types: Retail (led by Whole Foods at $18.2M), DTC Subscription cohorts (2020–2024), DTC one-time/gifting, Wholesale distributors (UNFI, KeHE), and Foodservice. The single largest account (Whole Foods, $18.2M) represents a notable concentration relative to total LTM revenue implied across the top 50 (~$136.7M). DTC subscription cohorts show strong and improving retention rates (68–74% 24-month retention). Key growth vectors include Amazon (+42% YoY), seasonal gifting (+35% YoY), and a Costco pilot. The company appears to be a premium packaged/bakery food brand with strong DTC and natural retail presence.
- deal_context (confidence=0.82): company=None, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Doc-type hint was 'dd_report' but content is an xlsx workbook (account-level revenue schedule). Tagged as 'dd_report' per hint since this is a diligence data room file; however content is more characteristic of a financial_model/data-room supporting schedule.
  - LTM revenue total of ~$136.7M is summed from the top 50 accounts listed; actual total company revenue may differ if the top 50 do not represent 100% of revenue.
  - LTM period is 'through October 2025' — interpreted as trailing twelve months ending October 2025; no calendar year-end date available.
  - % LTM rev column is blank in the source data; concentration percentages were not calculable from the raw table.
  - Company identity is de-identified beyond the codename 'Project Cascade'; product category inferred as premium bakery/packaged food (bread, pastry, granola) from account notes.

  </details>

### `Data Room/Financials/Cascade Historical Financials 2020-2025.xlsx` → `doc_project_cascade_005` (financial_model)
- Title: Project Cascade — Historical Financials (FY20–LTM)
- Date: 2025-10-31
- Summary: Historical income statement and DTC subscriber cohort data for Project Cascade, covering FY2020 through LTM October 2025 (audited by Deloitte through FY24). Revenue has grown from $52M in FY20 to $160M LTM, implying a strong multi-year CAGR. The workbook includes Adjusted EBITDA build-up with add-backs for founder compensation excess, one-time items, and stock/phantom equity — though reported and adjusted EBITDA cells are unpopulated (formulas not rendered). A DTC subscriber cohort sheet shows improving retention rates across vintages (52% for 2019 cohort rising to 88% for 2024 cohort), with average monthly spend per subscriber increasing from $34 to $46, indicating premiumization and improving cohort quality over time.
- deal_context (confidence=0.82): company=None, sector=consumer_products, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - EBITDA (reported), Gross profit, Gross margin %, Adj. EBITDA, and Adj. EBITDA margin % cells are all blank — these appear to be formula-driven cells whose computed values were not rendered in the extracted markdown. LTM Adj. EBITDA and margin cannot be confirmed.
  - DTC Cohort Summary: 'Active today', 'LTM cohort rev ($M)', and 'Avg tenure (mo)' columns are blank — only peak subscribers, retention %, and avg $/mo are populated.
  - Revenue CAGR 3yr calculated manually as FY22A–LTM: ($160M / $108M)^(1/3) - 1 ≈ 13.8%. This is an approximation using LTM as year-end proxy; actual 3yr CAGR from FY22A to FY24A would be ($148M / $108M)^(1/2) - 1 ≈ 17.0%. Used the longer window for conservatism.
  - Sector assigned as consumer_products based on DTC subscriber/cohort model and direct-to-consumer revenue structure; specific product category is not identified in the document. Subsector left null as 'pet_food', 'pet_supplies', and 'packaged_food' cannot be confirmed without more detail.
  - founder_transition thesis theme inferred from founder compensation excess add-backs present every year, suggesting a founder-led business.

  </details>

### `Data Room/Legal/Cascade Legal Diligence Summary 2025-12.pdf` → `doc_project_cascade_006` (dd_report)
- Title: Project Cascade — Legal Diligence Summary (Preliminary): Fieldstone Bakery Co.
- Date: 2025-12-12
- Summary: Kirkland & Ellis preliminary legal diligence memo for Project Cascade (Fieldstone Bakery Co.), dated December 12, 2025. No material adverse findings identified. Key confirmatory items include: (1) Target retail MSA change-of-control consent requirement; (2) IP ownership of the proprietary sourdough starter culture and "Edna" trademark; (3) FDA organic labeling compliance for upcoming certification renewals; and (4) co-packer recipe ownership confirmation. Corporate structure is clean — Delaware C-Corp, sole beneficial owner Laura Chen via Cascade Artisan Holdings, LLC, no third-party investors or convertible instruments. Eight registered US trademarks confirmed; sourdough starter protected as trade secret. Both production facilities (Portland and Austin) hold current SQF Level 2 certifications with strong audit scores. Two low-materiality litigation matters (TTAB trademark challenge and a minor WA overtime claim). Five confirmatory items are outstanding with deadlines in January 2026.
- deal_context (confidence=0.82): company=Fieldstone Bakery Co., sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Document is labeled 'Investment Committee Memorandum' in the header but folder hint and content confirm it is a DD report (legal diligence summary) — doc_type retained as dd_report.
  - No financial metrics (revenue, EBITDA) are present in this legal memo; all financial structured fields left null.
  - deal_type inferred as 'platform' based on sole-owner founder structure and PE acquisition context; not explicitly stated in document.
  - Co-packer volume noted as ~8% of LTM revenue but no absolute LTM revenue figure provided.

  </details>

### `Data Room/Operations/Cascade Operations Overview 2025-12.pdf` → `doc_project_cascade_007` (ic_memo)
- Title: Project Cascade — Operations Overview: Fieldstone Bakery Co.
- Date: 2025-12-01
- Summary: Investment Committee memorandum covering Fieldstone Bakery Co.'s operational profile under Project Cascade. The document details two production facilities (Portland, OR at 68,000 sq. ft. / ~95,000 units/day and Austin, TX at 44,000 sq. ft. / ~48,000 units/day), both operating at 71–78% utilization with strong SQF L2 certifications. Fieldstone runs a proprietary cold-chain logistics subsidiary (Fieldstone Distribution, LLC) for DTC shipping, achieving a 94.1% on-time delivery rate and a 0.8% damage/spoilage rate well below the 2–4% industry average. Operational KPIs show consistent improvement across production uptime (96.4%), yield (96.5%), and COGS/unit ($1.68) over FY22–LTM. Key upcoming initiatives include a Portland blending line expansion (+20,000 units/day), Austin packaging line upgrade (–30% manual labor), a potential East Coast greenfield facility ($22M capex), procurement consolidation ($1.2–1.8M savings), and DTC fulfillment automation. The memo was compiled by COO Ben Nakamura and reviewed by Fieldstone's quality and operations team.
- deal_context (confidence=0.88): company=Fieldstone Bakery Co., sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Folder hint suggested doc_type='dd_report', but document header explicitly states 'Investment Committee Memorandum'; overriding to 'ic_memo'.
  - Geography tagged as 'west_us' based on primary facility in Portland, OR, but company has national operations (Austin TX facility, East Coast expansion planned, national retail distribution via UNFI/KeHE). Consider 'national' if deal-level geography is resolved across docs.
  - No revenue, EBITDA, or valuation figures present in this operations-focused memo; financial structured fields left null.
  - Subsector 'packaged_food' is used for Fieldstone Bakery Co., a premium/artisan bakery — a more specific 'artisan_bakery' or 'premium_bakery' subsector could better represent the business, but 'packaged_food' is the closest existing value.

  </details>

### `Data Room/Org Structure/Cascade Org Structure 2025-12.pdf` → `doc_project_cascade_008` (ic_memo)
- Title: Corporate and Organizational Structure — Fieldstone Bakery Co.
- Date: 2025-12-01
- Summary: Investment Committee memorandum documenting the legal entity structure, leadership team, headcount breakdown, and ownership for Project Cascade (Fieldstone Bakery Co.) as of December 2025. The company is 100% founder-owned by Laura Chen through Cascade Artisan Holdings, LLC, with five legal entities spanning Oregon, Delaware, and Texas. Total headcount is 620, predominantly in production (Portland and Austin facilities). Laura Chen plans to roll 20–25% of sale proceeds into the acquisition vehicle and transition to Chief Brand Officer post-close, signaling a classic founder transition deal dynamic.
- deal_context (confidence=0.82): company=Fieldstone Bakery Co., sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - No financial figures present in this document; all financial structured fields set to null.
  - doc_type hint was absent; content is clearly an IC-use organizational memo — classified as ic_memo.
  - Geography set to west_us based on Oregon HQ/headquarters, but company also has material Texas operations; see taxonomy_proposals.
  - customer_concentration risk flag is inferred from the DTC subscription model and single-brand concentration, not explicitly stated in this document.

  </details>

### `Financial Model/Cascade LBO Model_v1.xlsx` → `doc_project_cascade_009` (financial_model)
- Title: Project Cascade — LBO Model (Base Case)
- Date: 2026-01-01
- Summary: LBO financial model for Project Cascade, prepared by Atlas Crossing Partners Fund IV in January 2026 with an assumed entry date of March 31, 2026. The model shows a $320M enterprise value entry at 10.0x LTM Adj. EBITDA ($32M) on $160M LTM revenue (20.0% EBITDA margin). The capital structure includes $175M senior secured debt (Antares), $80M Atlas Crossing equity, $55M founder rollover (~22% from Laura Chen), and $20M management equity pool. P&L projections forecast revenue growing from $160M (LTM) to $365M by FY30B at blended organic growth rates of 13–17.5%, with EBITDA margins expanding from ~21.6% to ~24.7%. A new East Coast facility capex of $22M is modeled in FY27B. Returns sensitivity across a 5-year hold shows exit EBITDA ranging from $42M (downside, 9x) to $82M (upside, 13x), with a base case of $62M at 11x. DTC subscriber dynamics (CAC, churn) and retail door growth are key operating assumptions, suggesting a consumer products / direct-to-consumer business.
- deal_context (confidence=0.82): company=Project Cascade, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - Entry multiple cell was blank in source table; calculated as $320M EV / $32M EBITDA = 10.0x
  - Total sources and total uses cells were blank in source table; implied totals are $330M each (sources: 175+80+55+20=330; uses: 320+12+12+8=352 — slight discrepancy of $22M likely a table rendering gap)
  - Revenue CAGR calculated from FY24A ($148M) to FY27B ($236M) as a 3-year forward proxy (~17%), and FY22A-FY24A historical CAGR ~17%; used blended ~20.8% based on LTM-to-FY27B 2-year CAGR as approximation
  - Subsector 'packaged_food' is the closest taxonomy match but the model's DTC subscriber metrics and churn assumptions suggest a subscription consumer brand (possibly pet food/supplements); subsector may need refinement once CIM is reviewed
  - D&A row shows identical values to Capex row in many periods — likely a table rendering artifact; FY27B shows -30 for both which aligns with the $22M facility capex + $8M maintenance assumption
  - Gross profit, EBITDA, gross margin %, EBITDA margin %, and unlevered FCF rows are formula-driven and blank in the source markdown — values not extractable directly
  - ACP proceeds, MOIC, and Gross IRR columns in returns sensitivity table are blank (formula cells); exit EVs not directly extractable

  </details>

### `Legal/Cascade Phase 2 Process Letter 2025-11.pdf` → `doc_project_cascade_010` (dd_report)
- Title: Phase 2 Process Letter — Project Cascade: Invitation to Management Presentations and Phase 2 Diligence
- Date: 2025-11-03
- Summary: Houlihan Lokey's Consumer, Food & Retail Group issued this Phase 2 Process Letter on November 3, 2025, inviting Atlas Crossing Partners Fund IV, L.P. ("ACP") to participate in the next stage of the sale process for Project Cascade (Fieldstone Bakery Co.). The letter details the management presentation scheduled for November 21, 2025 in Portland, OR, Phase 2 data room access, Q&A protocol, a final bid deadline of January 9, 2026, and the required elements for final bids including proposed enterprise value, transaction structure, financing plan, and key terms. The Seller is Cascade Artisan Holdings, LLC, with Houlihan Lokey acting as advisor.
- deal_context (confidence=0.85): company=Fieldstone Bakery Co., sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - doc_type override: folder hint was 'dd_report' but document is clearly a sell-side Phase 2 Process Letter (procedural/legal). Mapped to 'dd_report' as closest available type; taxonomy proposal submitted for 'process_letter'.
  - No financial figures (revenue, EBITDA, EV) are present in this document — it is a process administration letter only.
  - Geography set to west_us based on management presentation location (Portland, OR); company HQ not explicitly stated.
  - deal_type set to 'platform' as a default assumption for a full company sale; the letter does not specify whether this is a platform or add-on acquisition from ACP's perspective.

  </details>

### `Presentations/Data Room Cuts/Management Presentation Excerpt 2025-11.pdf` → `doc_project_cascade_011` (cim)
- Title: Project Cascade — Management Presentation (Excerpt)
- Date: 2025-11-21
- Summary: Management presentation excerpt for Project Cascade (Fieldstone), a premium packaged food / DTC subscription brand founded by Laura Chen in Portland, OR. The company produces artisan sourdough and ships 140,000+ units/day across two facilities to all 50 states. Key highlights include a DTC subscription model ("Cascade Crate") with 185,000 active subscribers and best-in-class LTV/CAC of 12.9x, retail presence across 4,200 doors including Whole Foods, Sprouts, H-E-B, Wegmans, and Target, and a planned East Coast facility representing $22M capex with an open target of Q4 2027. The presentation is coordinated by Houlihan Lokey (Rachel Kim, MD) and delivered by the Fieldstone executive team.
- deal_context (confidence=0.85): company=Fieldstone, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - No revenue, EBITDA, or financial model data present in this excerpt; structured financials are null.
  - Doc type classified as 'cim' (closest available) but content is explicitly a management presentation — see taxonomy_proposals for recommended addition of 'management_presentation' doc type.
  - Deal type defaulted to 'platform' based on context (founder-led, growth-stage brand seeking PE backing) but no explicit deal structure is stated in this excerpt.
  - East Coast facility location listed as TBD (mid-Atlantic); geography tagged as 'national' given operations across all 50 states.

  </details>

### `Presentations/Investment Decks/ACP Preliminary Screening Memo 2025-10.pdf` → `doc_project_cascade_012` (ic_memo)
- Title: Atlas Crossing Partners — Fund IV: Investment Committee Memorandum — Preliminary Screening Memo, Project Cascade
- Date: 2025-10-17
- Summary: Preliminary IC screening memo from Atlas Crossing Partners (Fund IV) for Project Cascade, a founder-built premium specialty artisan bakery brand with DTC subscription and retail omnichannel distribution. The memo recommends advancing to an IOI at $305M (9.5x LTM EBITDA) in a Houlihan Lokey-run limited auction. Key investment thesis rests on exceptional DTC subscription metrics (LTV/CAC of 12.9x, 185K subscribers), rapid retail door expansion (4,200 doors, +18% YoY), a proprietary 50-year sourdough starter moat, and founder Laura Chen transitioning to Chief Brand Officer post-close. Primary risks include single-founder brand dependency, production capacity constraints (Portland at 78% utilization, $22M+ East Coast capex in Year 2), CAC inflation, and retail category competition. Base case model projects a 2.9x MOIC / 24.0% IRR over a 5-year hold at exit EV of $682M.
- deal_context (confidence=0.92): company=Project Cascade, sector=consumer_products, subsector=packaged_food
- <details><summary>⚠ extraction warnings</summary>

  - LTM revenue not explicitly stated in the document; ebitda_margin could not be calculated.
  - Indicative EV range is $290M–$360M; ev_proposed_usd set to $305M reflecting the specific IOI bid recommendation rather than the midpoint of the range.
  - Geography assigned as west_us based on Portland, OR production facility; the company may have national DTC distribution which could alternatively warrant a 'national' geography tag.
  - Subsector 'packaged_food' used for specialty artisan bakery DTC+retail brand — a taxonomy proposal for 'specialty_food' or 'artisan_food' would be more precise but packaged_food is the closest existing value under consumer_products.

  </details>

## Resolver disagreements

### company_canonical
- Chosen: `Project Cascade` (plurality 2/3)
- Voters for chosen: ['Banker Materials/Teaser/Teaser Houlihan Lokey 2025-09.pdf', 'Presentations/Investment Decks/ACP Preliminary Screening Memo 2025-10.pdf']
- Dissent `Fieldstone Bakery Co.`: ['Banker Materials/CIM/CIM Fieldstone Bakery Co 2025-10.pdf']

### geography
- Chosen: `west_us` (plurality 2/3)
- Voters for chosen: ['Banker Materials/Teaser/Teaser Houlihan Lokey 2025-09.pdf', 'Presentations/Investment Decks/ACP Preliminary Screening Memo 2025-10.pdf']
- Dissent `national`: ['Banker Materials/CIM/CIM Fieldstone Bakery Co 2025-10.pdf']

### financials.revenue_cagr_3yr
- Chosen: `0.14` (other docs reported values differing by >20%; chosen value not overridden)
- Voters for chosen: ['Banker Materials/CIM/CIM Fieldstone Bakery Co 2025-10.pdf']
- Dissent `0.208`: ['Financial Model/Cascade LBO Model_v1.xlsx']

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- geography: proposed=`pacific_northwest_us` (used `west_us`, confidence=0.75)
  - rationale: The company's production facility is based in Portland, OR, which is Pacific Northwest — mapped to west_us as the closest available geography enum value.
- subsector: proposed=`dtc_subscription` (used `packaged_food`, confidence=0.65)
  - rationale: The business appears to be a DTC subscription company with cohort-based subscriber economics. None of the existing consumer_products subsectors (pet_food, pet_supplies, packaged_food) cleanly describe a subscription-oriented DTC model. 'packaged_food' is the least-wrong existing option if the product is consumable, but a 'dtc_subscription' subsector would better capture this business model.
- doc_type: proposed=`legal_dd_report` (used `dd_report`, confidence=0.72)
  - rationale: This document is specifically a legal diligence summary prepared by outside counsel (Kirkland & Ellis), distinct from commercial or financial DD reports. A dedicated 'legal_dd_report' sub-type would improve retrieval and routing precision.
- subsector: proposed=`artisan_bakery` (used `packaged_food`, confidence=0.82)
  - rationale: Fieldstone Bakery Co. is a premium artisan bakery producing fresh/frozen baked goods sold via DTC and retail channels. The existing 'packaged_food' subsector is the closest fit but does not capture the artisan/perishable bakery nature of the business, which has distinct operational characteristics (cold-chain, short shelf life, SQF certifications).
- geography: proposed=`multi_region_us` (used `west_us`, confidence=0.65)
  - rationale: Fieldstone Bakery operates in Oregon (HQ, Portland production) and Texas (Austin facility), spanning two distinct US regions. 'west_us' is the closest single-region fit given the Oregon headquarters, but a multi-region designation would be more accurate.
- subsector: proposed=`dtc_subscription_consumer` (used `packaged_food`, confidence=0.55)
  - rationale: The model's key assumptions include DTC subscriber growth rates, monthly churn (6.2%), and CAC per subscriber — strongly suggesting a direct-to-consumer subscription-based consumer brand. None of the existing consumer_products subsectors (pet_food, pet_supplies, packaged_food) fully capture this subscription/DTC dynamic. packaged_food is the closest available.
- doc_type: proposed=`process_letter` (used `dd_report`, confidence=0.9)
  - rationale: This document is a sell-side M&A process letter issued by an investment bank, governing Phase 2 bidding procedures. It is neither a diligence report nor a CIM — it is a procedural/legal process document. The closest existing type is dd_report, but a dedicated 'process_letter' or 'legal' doc type would be more precise.
- doc_type: proposed=`management_presentation` (used `cim`, confidence=0.72)
  - rationale: This document is a management presentation excerpt, which is a distinct doc type from a CIM. While both are marketing-oriented sell-side documents, a management presentation is typically a live/diligence-room deck delivered by the company's executive team, whereas a CIM is a written descriptive memorandum. The closest existing doc_type is 'cim'.
