# Ingestion report — project_tideway

Deal ID: `deal_project_tideway_2023`
Company canonical: `Meridian Marine Services`
Sector / subsector: `business_services` / `outsourced_business_services`
Geography: `southeast_us`
Deal type: `platform`
Voted with 2 qualifying docs at confidence >= 0.7 (out of 2 tagged).

## Triage

### primary (2)
- `Marketing Materials/Project_Tideway_CIM_June2023.pdf`
- `Marketing Materials/Project_Tideway_Teaser_June2023.pdf`

### format_duplicate (2)
- `Marketing Materials/Project_Tideway_CIM_June2023.pptx` — PDF preferred over DOCX/PPTX twin
- `Marketing Materials/Project_Tideway_Teaser_June2023.pptx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Marketing Materials/Project_Tideway_CIM_June2023.pdf` → `doc_project_tideway_001` (cim)
- Title: Project Tideway — Confidential Information Memorandum: Meridian Marine Services
- Date: 2023-06-01
- Summary: Jefferies LLC-prepared CIM for Project Tideway, the sale process for Meridian Marine Services, a Houston-based provider of integrated offshore logistics, vessel chartering, and port services to the Gulf of Mexico energy sector. Meridian operates a fleet of 38 vessels (PSVs, fast crew boats, anchor handling tugs) with owned shore bases at Port Fourchon, LA and Ingleside, TX. LTM Q1'23 revenue of $185M and Adj. EBITDA of $32M (17.3% margin). Asking EV of ~$280M (8.75x LTM EBITDA). The company was founded in 2008 by Kirk Dolan (ex-Tidewater COO) and has completed 3 fleet acquisitions since 2018. Shell and BP collectively represent 41% of LTM revenue. The process is structured as a limited auction with IOIs due July 14, 2023, run exclusively by Jefferies.
- deal_context (confidence=0.88): company=Meridian Marine Services, sector=business_services, subsector=None
- <details><summary>⚠ extraction warnings</summary>

  - Sector classification is imprecise: Meridian Marine Services operates in offshore marine/energy services, which has no direct taxonomy match. 'business_services' selected as closest; taxonomy proposal filed.
  - Subsector left null per rules (no valid subsector under 'business_services' fits offshore marine logistics); taxonomy proposal filed for 'offshore_logistics_and_marine_services'.
  - Geography classified as 'southeast_us' (Port Fourchon, LA) but HQ is Houston, TX (southeast_us border); 'gulf_coast_us' would be ideal — taxonomy proposal filed.
  - Revenue CAGR 3yr not explicitly stated; implied from FY2020–FY2022 data (~16% CAGR) but not labeled as such in the document, so left null in structured payload.
  - LTM Q1'23 revenue of $185.4M and EBITDA of $32.1M used (precise figures from financial table); headline callouts round to $185M/$32M.
  - Management projections (FY2023E–FY2027E) are present but labeled 'not independently verified'; not populated into returns_extract or underwriting_case_extract as this is a CIM, not an IC memo.
  - doc_type override: filename and content both confirm this is a CIM; folder-based hint was absent.

  </details>

### `Marketing Materials/Project_Tideway_Teaser_June2023.pdf` → `doc_project_tideway_002` (teaser)
- Title: Project Tideway — Executive Teaser
- Date: 2023-06-01
- Summary: Jefferies-run sell-side teaser for Project Tideway, the marketed sale of Meridian Marine Services — a Houston-based provider of offshore logistics, vessel chartering, and port services to the Gulf of Mexico energy sector. Meridian operates a 38-vessel fleet (PSVs, crew boats, anchor handling tugs), owns shore bases in Fourchon, LA and Ingleside, TX, and counts Shell, BP, Chevron, and Murphy Oil as key clients. LTM (Q1'23) revenue is $185M with Adj. EBITDA of $32M (17.3% margin). Asking EV is ~$280M (~8.75x LTM Adj. EBITDA). The investment thesis centers on a contracted revenue backlog ($285M), fleet value at a 54% discount to replacement cost, energy sector tailwinds, and a management team with a demonstrated M&A track record. The process was at teaser-distribution stage as of June 2023.
- deal_context (confidence=0.92): company=Meridian Marine Services, sector=business_services, subsector=outsourced_business_services
- <details><summary>⚠ extraction warnings</summary>

  - Revenue CAGR (3yr) not explicitly stated; implied ~10.9% CAGR from FY2020 ($128M) to FY2022 ($172M), but LTM growth of 21% YoY is highlighted instead — not populated to avoid ambiguity.
  - FY2023E–FY2027E figures are management projections not independently verified by Jefferies LLC; these were NOT loaded into structured financials (LTM actuals used instead).
  - Geography mapped to 'southeast_us' as best available proxy for Gulf Coast / Gulf of Mexico operations; see taxonomy_proposals for proposed addition.
  - Sector mapped to 'business_services' as closest fit; offshore marine logistics / energy services is not a current taxonomy value — see taxonomy_proposals.
  - Deal type mapped to 'platform' as this appears to be a full-company sale of an established platform with identified add-on targets; no explicit PE buyer structure confirmed at teaser stage.

  </details>

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- sector: proposed=`offshore_marine_services` (used `business_services`, confidence=0.62)
  - rationale: Meridian Marine Services operates offshore logistics vessels, vessel chartering, and port services for E&P operators — a capital-intensive, asset-heavy marine sector that does not fit cleanly into any existing taxonomy value. 'business_services' is the closest available option (B2B services orientation), but an 'offshore_marine_services' or 'energy_services' sector designation would be more accurate.
- subsector: proposed=`offshore_logistics_and_marine_services` (used `outsourced_business_services`, confidence=0.55)
  - rationale: Meridian provides integrated offshore logistics, vessel chartering, and port services — a distinct subsector not represented in the taxonomy. Under 'business_services', the closest available subsector is 'outsourced_business_services', though this is a poor fit. A dedicated 'offshore_marine_services' or 'energy_field_services' subsector would be more appropriate.
- geography: proposed=`gulf_coast_us` (used `southeast_us`, confidence=0.75)
  - rationale: Meridian's operations are concentrated in the Gulf of Mexico, with facilities in Louisiana (Port Fourchon) and Texas (Ingleside, Houston HQ). A 'gulf_coast_us' geography designation would be more precise than 'southeast_us', which is the closest existing value.
- sector: proposed=`marine_logistics_services` (used `business_services`, confidence=0.62)
  - rationale: Meridian Marine Services operates in offshore marine logistics and vessel chartering — a capital-intensive, asset-heavy B2B services niche tied to the energy sector. None of the existing sector values precisely capture this; 'business_services' is the closest available match, though 'industrial_distribution' or a future 'energy_services' sector would also be candidates.
- subsector: proposed=`offshore_marine_logistics` (used `outsourced_business_services`, confidence=0.55)
  - rationale: Meridian provides offshore vessel chartering, logistics, and port services — a specialized subsector not represented in the taxonomy. 'outsourced_business_services' is the closest existing value under 'business_services', but it does not adequately capture the marine/energy services nature of this business.
- geography: proposed=`gulf_of_mexico` (used `southeast_us`, confidence=0.65)
  - rationale: Meridian's primary operating geography is the Gulf of Mexico (with shore bases in Louisiana and Texas). The existing taxonomy lacks a Gulf of Mexico or south-central US designation; 'southeast_us' is the closest match given the Louisiana base, though Texas would point to 'south_central'. A 'gulf_coast_us' or 'south_us' geography option would be more precise.
