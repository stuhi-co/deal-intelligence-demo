# Ingestion report — project_sundial

Deal ID: `deal_project_sundial_2022`
Company canonical: `Slumber Smart, Inc.`
Sector / subsector: `consumer_tech` / `connected_devices`
Geography: `national`
Deal type: `platform`
Voted with 2 qualifying docs at confidence >= 0.9 (out of 2 tagged).

## Triage

### primary (2)
- `Marketing Materials/Project_Sundial_CIM_April2022.pdf`
- `Marketing Materials/Project_Sundial_Teaser_April2022.pdf`

### format_duplicate (2)
- `Marketing Materials/Project_Sundial_CIM_April2022.pptx` — PDF preferred over DOCX/PPTX twin
- `Marketing Materials/Project_Sundial_Teaser_April2022.pptx` — PDF preferred over DOCX/PPTX twin

## Tagged documents

### `Marketing Materials/Project_Sundial_CIM_April2022.pdf` → `doc_project_sundial_001` (cim)
- Title: Project Sundial — Confidential Information Memorandum: Slumber Smart, Inc.
- Date: 2022-04-01
- Summary: Goldman Sachs-prepared CIM for Slumber Smart, Inc. ("Project Sundial"), a Boulder, CO-based premium sleep-tech hardware and software platform. The Company designs and sells an integrated ecosystem of smart mattress pads (SlumberPod™), biometric monitoring hardware, and AI-powered sleep coaching software (SlumberOS™). LTM revenue of $145M growing at 28% YoY, with $18M Adj. EBITDA (12.4% margin) and $29M subscription ARR at 115% NRR. Goldman Sachs is running a limited sell-side auction with a guided enterprise value of ~$200M (11.1x LTM EBITDA). Management projects revenue growing to $340M by FY2026 with EBITDA margins expanding to 21.8%. Key investment themes include a proprietary hardware-software flywheel, premium DTC economics (LTV/CAC of 10.6x), and a structurally growing sleep-wellness TAM.
- deal_context (confidence=0.95): company=Slumber Smart, Inc., sector=consumer_tech, subsector=connected_devices
- <details><summary>⚠ extraction warnings</summary>

  - Revenue CAGR of 26% is explicitly stated for FY2019–FY2021; set revenue_cagr_3yr to 0.26 accordingly.
  - LTM figures reflect the 12 months ending Q1 2022 (March 31, 2022), not a standard FY period.
  - Guided EV of ~$200M is a process guidance figure from the sell-side banker, not a signed transaction value.
  - Management projections (FY2022E–FY2026E) are unaudited and not independently verified by Goldman Sachs per the CIM disclaimer.
  - Geography tagged as 'national' (US-primary); international revenues (UK, AU) are ~6% LTM — not sufficient to override to 'international'.

  </details>

### `Marketing Materials/Project_Sundial_Teaser_April2022.pdf` → `doc_project_sundial_002` (teaser)
- Title: Project Sundial — Executive Teaser
- Date: 2022-04-01
- Summary: Goldman Sachs-run limited auction teaser for Project Sundial / Slumber Smart, Inc., a Boulder, CO-based premium sleep-tech hardware and software company founded in 2014. LTM revenue of $145M (+28% YoY), LTM Adj. EBITDA of $18M (12.4% margin), and subscription ARR of $29M (~185K subscribers, 115% NRR). Asking EV of ~$200M (11.1x LTM EBITDA). Process timeline runs April–June 2022. Investment highlights emphasize category leadership in sleep-tech, a hardware+software flywheel (SlumberOS), high-growth SaaS subscription layer, strong DTC unit economics, and international expansion whitespace. Founder-led by CEO Maya Chen (ex-Fitbit).
- deal_context (confidence=0.92): company=Slumber Smart, Inc., sector=consumer_tech, subsector=connected_devices
- <details><summary>⚠ extraction warnings</summary>

  - Date inferred as 2022-04-01 from 'April 2022' cover page; exact day not specified.
  - Revenue CAGR 3yr not explicitly stated; implied ~26% from FY2019–FY2021 history but not labeled as such in the document — left null.
  - Asking EV of ~$200M described as approximate ('~'); ev_proposed_usd recorded as 200000000.
  - FY2022E and FY2023E figures are Goldman Sachs estimates based on management projections — not audited actuals; not emitted as period_actuals.
  - risk_flags includes founder_dependency given CEO Maya Chen is the founder; customer_concentration flagged due to reliance on DTC channel and limited retail partners, though not explicitly called out as a risk in the document.

  </details>

## Taxonomy proposals

These values were not in `enums.yaml`. The tagger persisted `closest_existing`
but flagged the proposed addition. `--commit` will refuse until these are resolved.

- subsector: proposed=`sleep_tech_hardware_software` (used `connected_devices`, confidence=0.78)
  - rationale: Slumber Smart is specifically a sleep-tech hardware + software subscription company. The taxonomy's 'connected_devices' under consumer_tech is the closest available subsector, but a dedicated 'sleep_tech_hardware_software' or 'smart_home_devices' subsector would better capture this emerging category.
