# Ingestion report — project_vellum

Deal ID: `deal_project_vellum_2024`
Company canonical: `Ascot Paper Products`
Sector / subsector: `manufacturing` / `process_manufacturing`
Geography: `west_us`
Deal type: `platform`
Voted with 2 qualifying docs at confidence >= 0.9 (out of 2 tagged).

## Triage

### primary (2)
- `Marketing Materials/Project_Vellum_CIM_Feb2024.pdf`
- `Marketing Materials/Project_Vellum_Teaser_Feb2024.pdf`

### format_duplicate (2)
- `Marketing Materials/Project_Vellum_CIM_Feb2024.pptx` — PDF preferred over DOCX/PPTX twin
- `Marketing Materials/Project_Vellum_Teaser_Feb2024.pptx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Marketing Materials/Project_Vellum_CIM_Feb2024.pdf` → `doc_project_vellum_001` (cim)
- Title: Project Vellum — Confidential Information Memorandum: Ascot Paper Products
- Date: 2024-02-01
- Summary: Lincoln International has prepared this CIM on behalf of Ascot Paper Products ("Ascot"), a Portland, OR-based manufacturer and distributor of premium specialty paper products — including fine writing papers, art & illustration papers, archival document papers, and premium packaging substrates. Founded in 2001 by Richard Hartley (68% family-owned), Ascot operates two facilities (Portland manufacturing; Memphis distribution) with ~290 employees. LTM Q4'23 revenue of $95M and Adj. EBITDA of $14M (14.7% margin). The Company is being marketed at a ~$140M EV (10.0x LTM Adj. EBITDA) in a targeted sell-side process led by Lincoln International with IOIs due March 15, 2024. Key investment themes include defensible niche positioning via ISO 9706 archival certification and proprietary coating formulas, premium pricing power (30–45x premium over commodity paper), durable institutional customer base (Library of Congress, Smithsonian) on 5-year supply agreements, and a high-growth DTC/e-commerce channel (65% CAGR FY2021–FY2023). The balance sheet is debt-free with $11M cash. This is a first-generation family liquidity event with Margaret Hartley designated as CEO successor.
- deal_context (confidence=0.95): company=Ascot Paper Products, sector=manufacturing, subsector=process_manufacturing
- <details><summary>⚠ extraction warnings</summary>

  - Revenue CAGR approximated as ~5.0% using FY2021 ($82M) to LTM Q4'23 ($95M) over ~2 years; a strict 3-year CAGR from FY2021 to FY2023 ($82M to $91.4M) yields ~5.6% — slightly different from headline +7% YoY LTM figure which reflects recent acceleration.
  - Geography tagged as 'west_us' (Portland, OR HQ and manufacturing), though the Company has national distribution across 4,800+ retail doors and a Memphis, TN distribution center — 'national' could also apply. West_us chosen as primary operating footprint.
  - Management projections (FY2024E–FY2028E) are explicitly noted as not independently verified; not extracted into underwriting_case_extract as this is a CIM (not an IC memo).
  - Deal type tagged as 'platform' — this is a first-generation family liquidity event with no stated add-on strategy, but the CIM references 'immediate bolt-on capacity' suggesting a platform thesis. Could also be categorized as 'carve_out' is inapplicable; 'platform' is the best fit.

  </details>

### `Marketing Materials/Project_Vellum_Teaser_Feb2024.pdf` → `doc_project_vellum_002` (teaser)
- Title: Project Vellum — Executive Teaser
- Date: 2024-02-01
- Summary: Executive teaser prepared by Lincoln International (exclusive advisor) for Project Vellum, the sale process for Ascot Paper Products — a Portland, OR-based manufacturer and distributor of premium specialty paper products (fine writing, art, archival, and packaging substrates). The company was founded in 2001 and is majority family-owned (Hartley family, 68%), representing a first-generation founder transition. LTM revenue is $95M with LTM Adj. EBITDA of $14M (14.7% margin); asking EV is ~$140M (~10.0x LTM Adj. EBITDA). Key investment highlights include defensible niche positioning via patents and certifications, premium pricing power, a durable institutional customer base with long tenure, a fast-growing DTC/e-commerce channel, FSC-certified sustainability credentials, and a clean balance sheet with zero debt. Management projects revenue growing from $102M (FY2024E) to $137M (FY2028E) with margin expansion to ~17%+.
- deal_context (confidence=0.92): company=Ascot Paper Products, sector=manufacturing, subsector=process_manufacturing
- <details><summary>⚠ extraction warnings</summary>

  - Revenue CAGR estimated from FY2021 ($82M) to LTM Q4'23 ($95.1M) over ~2 years, yielding ~7.7% CAGR; 3-year CAGR from FY2021 to FY2024E ($102M) is approximately 7.5% — reported as ~0.05 (conservative 3yr estimate using actuals only through FY2023).
  - FY2024E and FY2025E revenue ($102M, $110M) and EBITDA/margin (15.7%, 17.3%) are management projections not independently verified by Lincoln International.
  - Geography tagged as 'west_us' based on Portland, OR HQ; company also has Memphis, TN operations suggesting partial southeast_us footprint — 'national' could also apply.
  - Asking EV of ~$140M is approximate (denoted with tilde in source); EV/EBITDA multiple of 10.0x is as stated in the teaser.

  </details>

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- sector: proposed=`specialty_paper_manufacturing` (used `manufacturing`, confidence=0.72)
  - rationale: Ascot Paper Products is a specialty paper manufacturer — a distinct niche that combines elements of manufacturing and specialty chemicals but is best captured under 'manufacturing'. The taxonomy lacks a 'specialty_paper' or 'light_industrial' sector, so 'manufacturing' is the closest fit.
- subsector: proposed=`specialty_paper` (used `process_manufacturing`, confidence=0.65)
  - rationale: Ascot manufactures premium specialty papers using proprietary coating chemistry and surface sizing — a process-intensive manufacturing operation. 'process_manufacturing' is the closest subsector under 'manufacturing', though 'specialty_paper_manufacturing' would be more precise.
- subsector: proposed=`specialty_paper_manufacturing` (used `process_manufacturing`, confidence=0.72)
  - rationale: Ascot Paper Products is a specialty paper manufacturer — a niche within manufacturing that combines process manufacturing characteristics with premium/specialty product positioning. 'process_manufacturing' is the closest existing subsector under 'manufacturing', but a dedicated 'specialty_paper_manufacturing' or 'specialty_manufacturing' subsector would better capture this segment.
- sector: proposed=`specialty_paper_and_packaging` (used `manufacturing`, confidence=0.65)
  - rationale: Ascot operates in light industrial specialty paper manufacturing — a sector that also has characteristics of consumer products (premium writing papers) and specialty chemicals (proprietary coatings). 'manufacturing' is the best existing fit, but a dedicated 'specialty_paper_and_packaging' sector would be more precise.
