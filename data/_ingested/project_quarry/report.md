# Ingestion report — project_quarry

Deal ID: `deal_project_quarry_2019`
Company canonical: `Consolidated Rock Industries`
Sector / subsector: `construction_materials` / `aggregates_quarrying`
Geography: `west_us`
Deal type: `platform`
Voted with 2 qualifying docs at confidence >= 0.9 (out of 2 tagged).

## Triage

### primary (2)
- `Marketing Materials/Project_Quarry_CIM_March2019.pdf`
- `Marketing Materials/Project_Quarry_Teaser_March2019.pdf`

### format_duplicate (2)
- `Marketing Materials/Project_Quarry_CIM_March2019.pptx` — PDF preferred over DOCX/PPTX twin
- `Marketing Materials/Project_Quarry_Teaser_March2019.pptx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Marketing Materials/Project_Quarry_CIM_March2019.pdf` → `doc_project_quarry_001` (cim)
- Title: Project Quarry — Consolidated Rock Industries Confidential Information Memorandum
- Date: 2019-03-01
- Summary: Harris Williams & Co. sell-side CIM for Consolidated Rock Industries ("CRI"), a founder-led regional aggregates producer operating 14 permitted quarry sites across Utah, Nevada, Colorado, and Idaho. CRI produces crushed stone, construction sand & gravel, ready-mix concrete, and industrial minerals. LTM Q1'19 revenue of $245M, Adj. EBITDA of $44M (18.0% margin), with an asking EV of ~$350M (7.9x LTM EBITDA). The investment thesis centers on an irreplaceable permitted reserve base (~580M tons, 30+ years of production), structural supply constraints from permitting barriers, strong pricing power (#1–2 position in 6 MSAs), vertical integration via owned fleet and ready-mix operations, and a proven roll-up strategy with an active bolt-on pipeline. CEO David Mercer, the founder with 62% equity, is leading a transition via a targeted sale process with IOIs due April 5, 2019.
- deal_context (confidence=0.97): company=Consolidated Rock Industries, sector=construction_materials, subsector=aggregates_quarrying
- <details><summary>⚠ extraction warnings</summary>

  - Revenue CAGR 3yr estimated from FY2016 ($165M) to LTM Q1'19 ($245.1M) over ~3 years; not a clean FY2016-to-FY2018 CAGR. FY2016-to-FY2018 CAGR is approximately 15.0%.
  - LTM Q1'19 figures used as the primary LTM basis; these are not a standard fiscal year end.
  - Geography tagged as west_us — CRI operates across UT, NV, CO, and ID (Mountain West). 'national' was considered but rejected as operations are concentrated in the western mountain states.
  - Asking EV of ~$350M is seller guidance, not a binding valuation.

  </details>

### `Marketing Materials/Project_Quarry_Teaser_March2019.pdf` → `doc_project_quarry_002` (teaser)
- Title: Project Quarry — Executive Teaser
- Date: 2019-03-01
- Summary: Harris Williams & Co. sell-side teaser for Project Quarry / Consolidated Rock Industries ("CRI"), a regional aggregates producer operating 14 permitted quarry sites across Utah, Nevada, Colorado, and Idaho. CRI offers ~580M tons of permitted mineral reserves (30+ years of capacity), a 220-vehicle owned fleet, and a vertically integrated ready-mix concrete division. LTM Q1'19 revenue of $245M and Adj. EBITDA of $44M (18.0% margin); asking EV of ~$350M (~7.9x LTM Adj. EBITDA). The investment thesis centers on an irreplaceable permitted reserve base, infrastructure end-market tailwinds (IIJA), strong local market pricing power, and a founder-led roll-up strategy with 6 identified bolt-on targets in adjacent Mountain West markets.
- deal_context (confidence=0.93): company=Consolidated Rock Industries, sector=construction_materials, subsector=aggregates_quarrying
- <details><summary>⚠ extraction warnings</summary>

  - Revenue CAGR (3yr) estimated from FY2016 ($165M) to FY2018 ($218.3M): ~(218.3/165)^(1/2)-1 ≈ 15.0%; document also shows +16.6% and +13.5% YoY growth for FY2017 and FY2018 respectively — using geometric average of stated actuals yields ~14.9%; coded as 0.142 as a rounded estimate.
  - FY2019E and FY2020E projected figures partially cut off in source table — only partial values captured (Rev $268M/$292M; Adj. EBITDA $50M/$57M). Not included in structured payload as they are projections, not actuals.
  - Geography tagged as west_us (Utah, Nevada, Colorado, Idaho headquarters and primary operations); taxonomy does not have a 'mountain_west' region so west_us is the closest existing value.
  - Date defaulted to 2019-03-01 (month-precision) based on document header 'March 2019'.

  </details>
