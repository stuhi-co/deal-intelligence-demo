// =============================================================================
// Deal Intelligence — Knowledge Graph Load Script
// =============================================================================
// Paste into Neo4j Browser. Idempotent: re-running wipes and reloads.
// Enums are sourced from ../enums.yaml — keep values in sync.
//
// Mirrors data/deals.json:
//   - 8 Deals, 4 People, 8 Companies, 4 PortfolioCompanies (one per closed deal),
//     3 Sectors, 6 Subsectors, 5 Themes, 6 RiskThemes.
//   - Every SIMILAR_TO edge mirrors a deal's `similar_deals_computed` entry.
//   - Every PASSED_DUE_TO edge mirrors a passed deal's `outcome.primary_reason`
//     (weight 0.7) and `outcome.secondary_reasons` (weight 0.4 each).
//
// Three demo queries are appended at the bottom (search for "// DEMO QUERY").
// =============================================================================


// -----------------------------------------------------------------------------
// 0. Reset
// -----------------------------------------------------------------------------
MATCH (n) DETACH DELETE n;


// -----------------------------------------------------------------------------
// 1. People (4)
// -----------------------------------------------------------------------------
CREATE (:Person {id: "person_jsmith", name: "John Smith",    role: "partner"});
CREATE (:Person {id: "person_mchen",  name: "Michael Chen",  role: "partner"});
CREATE (:Person {id: "person_klee",   name: "Karen Lee",     role: "principal"});
CREATE (:Person {id: "person_rpatel", name: "Raj Patel",     role: "vp"});


// -----------------------------------------------------------------------------
// 2. Sectors (3) + Subsectors (6)
// -----------------------------------------------------------------------------
CREATE (:Sector {id: "sector_hcsvc",    key: "healthcare_services",     name: "Healthcare Services"});
CREATE (:Sector {id: "sector_inddist",  key: "industrial_distribution", name: "Industrial Distribution"});
CREATE (:Sector {id: "sector_techsvc",  key: "tech_enabled_services",   name: "Tech-Enabled Services"});
CREATE (:Sector {id: "sector_chem",     key: "specialty_chemicals",     name: "Specialty Chemicals"});

CREATE (:Subsector {id: "sub_outclin",   key: "outsourced_clinical_services", name: "Outsourced Clinical Services"});
CREATE (:Subsector {id: "sub_payer",     key: "payer_services",               name: "Payer Services"});
CREATE (:Subsector {id: "sub_specdist",  key: "specialty_distribution",       name: "Specialty Distribution"});
CREATE (:Subsector {id: "sub_mrodist",   key: "mro_distribution",             name: "MRO Distribution"});
CREATE (:Subsector {id: "sub_vsaas",     key: "vertical_saas",                name: "Vertical SaaS"});
CREATE (:Subsector {id: "sub_managed",   key: "managed_services",             name: "Managed Services"});
CREATE (:Subsector {id: "sub_procchem",  key: "process_chemicals",            name: "Process Chemicals"});
CREATE (:Subsector {id: "sub_specint",   key: "specialty_intermediates",      name: "Specialty Intermediates"});


// -----------------------------------------------------------------------------
// 3. Themes (thesis) + RiskThemes
// -----------------------------------------------------------------------------
CREATE (:Theme {id: "theme_rollup",        key: "roll_up",              name: "Roll-up Strategy"});
CREATE (:Theme {id: "theme_consol",        key: "market_consolidation", name: "Market Consolidation"});
CREATE (:Theme {id: "theme_founder",       key: "founder_transition",   name: "Founder Transition"});
CREATE (:Theme {id: "theme_marginexp",     key: "margin_expansion",     name: "Margin Expansion"});
CREATE (:Theme {id: "theme_recurring",     key: "recurring_revenue",    name: "Recurring Revenue"});

CREATE (:RiskTheme {id: "risk_mgmt",       key: "management_quality",     name: "Management Quality"});
CREATE (:RiskTheme {id: "risk_payer",      key: "payer_concentration",    name: "Payer Concentration"});
CREATE (:RiskTheme {id: "risk_customer",   key: "customer_concentration", name: "Customer Concentration"});
CREATE (:RiskTheme {id: "risk_regulatory", key: "regulatory_exposure",    name: "Regulatory Exposure"});
CREATE (:RiskTheme {id: "risk_cycle",      key: "cyclicality",            name: "Cyclicality"});
CREATE (:RiskTheme {id: "risk_integration",key: "integration_risk",       name: "Integration Risk"});


// -----------------------------------------------------------------------------
// 4. Companies (8, canonical names) + PortfolioCompanies (4, one per closed deal)
// -----------------------------------------------------------------------------
CREATE (:Company {id: "co_medtech",     name: "MedTech Services Inc."});
CREATE (:Company {id: "co_orion",       name: "Orion Industrial Supply Co."});
CREATE (:Company {id: "co_acme",        name: "Acme MedSupply Inc."});
CREATE (:Company {id: "co_techflow",    name: "TechFlow Distribution Inc."});
CREATE (:Company {id: "co_atlas",       name: "Atlas Health Group LLC"});
CREATE (:Company {id: "co_cascade",     name: "Cascade Software Holdings Inc."});
CREATE (:Company {id: "co_healthroll",  name: "HealthRoll Partners LLC"});
CREATE (:Company {id: "co_midstates",   name: "MidStates Components Co."});

CREATE (:PortfolioCompany {id: "portco_acme",       name: "Acme MedSupply (PortCo, exited 2025)"});
CREATE (:PortfolioCompany {id: "portco_techflow",   name: "TechFlow Distribution (PortCo, exited 2024)"});
CREATE (:PortfolioCompany {id: "portco_healthroll", name: "HealthRoll Partners (PortCo, currently held)"});
CREATE (:PortfolioCompany {id: "portco_midstates",  name: "MidStates Components (PortCo, currently held)"});


// -----------------------------------------------------------------------------
// 5. Deals (8)
// -----------------------------------------------------------------------------
CREATE (:Deal {
  id: "deal_falcon_2025", codename: "Project Falcon",
  status: "active_diligence", year: 2025,
  revenue_ltm_usd: 142000000, ebitda_ltm_usd: 28000000, ebitda_margin: 0.197,
  ev_proposed_usd: 285000000, deal_type: "platform", geography: "southeast_us"
});
CREATE (:Deal {
  id: "deal_orion_2026", codename: "Project Orion",
  status: "active_diligence", year: 2026,
  revenue_ltm_usd: 198000000, ebitda_ltm_usd: 22000000, ebitda_margin: 0.111,
  ev_proposed_usd: 230000000, deal_type: "platform", geography: "midwest_us"
});
CREATE (:Deal {
  id: "deal_acme_2021", codename: "Acme Acquisition",
  status: "closed_exited", year: 2021,
  revenue_ltm_usd: 118000000, ebitda_ltm_usd: 21000000, ebitda_margin: 0.178,
  ev_proposed_usd: 220000000, deal_type: "platform", geography: "southeast_us"
});
CREATE (:Deal {
  id: "deal_techflow_2019", codename: "TechFlow Acquisition",
  status: "closed_exited", year: 2019,
  revenue_ltm_usd: 165000000, ebitda_ltm_usd: 19000000, ebitda_margin: 0.115,
  ev_proposed_usd: 175000000, deal_type: "platform", geography: "midwest_us"
});
CREATE (:Deal {
  id: "deal_atlas_2022", codename: "Project Atlas",
  status: "passed", year: 2022,
  revenue_ltm_usd: 175000000, ebitda_ltm_usd: 28000000, ebitda_margin: 0.160,
  ev_proposed_usd: 310000000, deal_type: "platform", geography: "northeast_us"
});
CREATE (:Deal {
  id: "deal_cascade_2024", codename: "Project Cascade",
  status: "dead", year: 2024,
  revenue_ltm_usd: 64000000, ebitda_ltm_usd: 9000000, ebitda_margin: 0.141,
  ev_proposed_usd: null, deal_type: "platform", geography: "west_us"
});
CREATE (:Deal {
  id: "deal_healthroll_2020", codename: "Project HealthRoll",
  status: "closed_held", year: 2020,
  revenue_ltm_usd: 95000000, ebitda_ltm_usd: 20000000, ebitda_margin: 0.211,
  ev_proposed_usd: 180000000, deal_type: "platform", geography: "southeast_us"
});
CREATE (:Deal {
  id: "deal_midstates_2022", codename: "MidStates Acquisition",
  status: "closed_held", year: 2022,
  revenue_ltm_usd: 145000000, ebitda_ltm_usd: 18000000, ebitda_margin: 0.124,
  ev_proposed_usd: 195000000, deal_type: "platform", geography: "midwest_us"
});


// =============================================================================
// EDGES
// =============================================================================

// -----------------------------------------------------------------------------
// 6. WORKED_ON  (Person -> Deal, role: lead | team)
// -----------------------------------------------------------------------------
// Falcon: jsmith lead, klee + rpatel team
MATCH (p:Person {id: "person_jsmith"}), (d:Deal {id: "deal_falcon_2025"})    CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_klee"}),   (d:Deal {id: "deal_falcon_2025"})    CREATE (p)-[:WORKED_ON {role: "team"}]->(d);
MATCH (p:Person {id: "person_rpatel"}), (d:Deal {id: "deal_falcon_2025"})    CREATE (p)-[:WORKED_ON {role: "team"}]->(d);

// Orion: mchen lead, klee team
MATCH (p:Person {id: "person_mchen"}),  (d:Deal {id: "deal_orion_2026"})     CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_klee"}),   (d:Deal {id: "deal_orion_2026"})     CREATE (p)-[:WORKED_ON {role: "team"}]->(d);

// Acme: jsmith lead, klee team
MATCH (p:Person {id: "person_jsmith"}), (d:Deal {id: "deal_acme_2021"})      CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_klee"}),   (d:Deal {id: "deal_acme_2021"})      CREATE (p)-[:WORKED_ON {role: "team"}]->(d);

// TechFlow: mchen lead, rpatel team
MATCH (p:Person {id: "person_mchen"}),  (d:Deal {id: "deal_techflow_2019"})  CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_rpatel"}), (d:Deal {id: "deal_techflow_2019"})  CREATE (p)-[:WORKED_ON {role: "team"}]->(d);

// Atlas: mchen lead, klee + rpatel team
MATCH (p:Person {id: "person_mchen"}),  (d:Deal {id: "deal_atlas_2022"})     CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_klee"}),   (d:Deal {id: "deal_atlas_2022"})     CREATE (p)-[:WORKED_ON {role: "team"}]->(d);
MATCH (p:Person {id: "person_rpatel"}), (d:Deal {id: "deal_atlas_2022"})     CREATE (p)-[:WORKED_ON {role: "team"}]->(d);

// Cascade: mchen lead, rpatel team
MATCH (p:Person {id: "person_mchen"}),  (d:Deal {id: "deal_cascade_2024"})   CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_rpatel"}), (d:Deal {id: "deal_cascade_2024"})   CREATE (p)-[:WORKED_ON {role: "team"}]->(d);

// HealthRoll: jsmith lead, klee team
MATCH (p:Person {id: "person_jsmith"}), (d:Deal {id: "deal_healthroll_2020"}) CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_klee"}),   (d:Deal {id: "deal_healthroll_2020"}) CREATE (p)-[:WORKED_ON {role: "team"}]->(d);

// MidStates: mchen lead, rpatel team
MATCH (p:Person {id: "person_mchen"}),  (d:Deal {id: "deal_midstates_2022"}) CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_rpatel"}), (d:Deal {id: "deal_midstates_2022"}) CREATE (p)-[:WORKED_ON {role: "team"}]->(d);


// -----------------------------------------------------------------------------
// 7. SUBJECT_OF  (Deal -> Company)
// -----------------------------------------------------------------------------
MATCH (d:Deal {id: "deal_falcon_2025"}),     (c:Company {id: "co_medtech"})    CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_orion_2026"}),      (c:Company {id: "co_orion"})      CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_acme_2021"}),       (c:Company {id: "co_acme"})       CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_techflow_2019"}),   (c:Company {id: "co_techflow"})   CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_atlas_2022"}),      (c:Company {id: "co_atlas"})      CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_cascade_2024"}),    (c:Company {id: "co_cascade"})    CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_healthroll_2020"}), (c:Company {id: "co_healthroll"}) CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_midstates_2022"}),  (c:Company {id: "co_midstates"})  CREATE (d)-[:SUBJECT_OF]->(c);


// -----------------------------------------------------------------------------
// 8. IN_SECTOR  (Deal -> Sector)
// -----------------------------------------------------------------------------
MATCH (d:Deal {id: "deal_falcon_2025"}),     (s:Sector {id: "sector_hcsvc"})   CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_orion_2026"}),      (s:Sector {id: "sector_inddist"}) CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_acme_2021"}),       (s:Sector {id: "sector_hcsvc"})   CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_techflow_2019"}),   (s:Sector {id: "sector_inddist"}) CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_atlas_2022"}),      (s:Sector {id: "sector_hcsvc"})   CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_cascade_2024"}),    (s:Sector {id: "sector_techsvc"}) CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_healthroll_2020"}), (s:Sector {id: "sector_hcsvc"})   CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_midstates_2022"}),  (s:Sector {id: "sector_inddist"}) CREATE (d)-[:IN_SECTOR]->(s);


// -----------------------------------------------------------------------------
// 9. IN_SUBSECTOR  (Deal -> Subsector)
// -----------------------------------------------------------------------------
MATCH (d:Deal {id: "deal_falcon_2025"}),     (s:Subsector {id: "sub_outclin"})  CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_orion_2026"}),      (s:Subsector {id: "sub_specdist"}) CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_acme_2021"}),       (s:Subsector {id: "sub_outclin"})  CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_techflow_2019"}),   (s:Subsector {id: "sub_specdist"}) CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_atlas_2022"}),      (s:Subsector {id: "sub_outclin"})  CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_cascade_2024"}),    (s:Subsector {id: "sub_vsaas"})    CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_healthroll_2020"}), (s:Subsector {id: "sub_outclin"})  CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_midstates_2022"}),  (s:Subsector {id: "sub_mrodist"})  CREATE (d)-[:IN_SUBSECTOR]->(s);


// -----------------------------------------------------------------------------
// 10. HAS_THESIS_THEME  (Deal -> Theme)
// -----------------------------------------------------------------------------
// Falcon: roll_up, founder_transition
MATCH (d:Deal {id: "deal_falcon_2025"}), (t:Theme {id: "theme_rollup"})    CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_falcon_2025"}), (t:Theme {id: "theme_founder"})   CREATE (d)-[:HAS_THESIS_THEME]->(t);

// Orion: market_consolidation, margin_expansion
MATCH (d:Deal {id: "deal_orion_2026"}), (t:Theme {id: "theme_consol"})     CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_orion_2026"}), (t:Theme {id: "theme_marginexp"})  CREATE (d)-[:HAS_THESIS_THEME]->(t);

// Acme: roll_up, founder_transition
MATCH (d:Deal {id: "deal_acme_2021"}), (t:Theme {id: "theme_rollup"})      CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_acme_2021"}), (t:Theme {id: "theme_founder"})     CREATE (d)-[:HAS_THESIS_THEME]->(t);

// TechFlow: market_consolidation, margin_expansion
MATCH (d:Deal {id: "deal_techflow_2019"}), (t:Theme {id: "theme_consol"})    CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_techflow_2019"}), (t:Theme {id: "theme_marginexp"}) CREATE (d)-[:HAS_THESIS_THEME]->(t);

// Atlas: roll_up
MATCH (d:Deal {id: "deal_atlas_2022"}), (t:Theme {id: "theme_rollup"})     CREATE (d)-[:HAS_THESIS_THEME]->(t);

// Cascade: recurring_revenue, margin_expansion
MATCH (d:Deal {id: "deal_cascade_2024"}), (t:Theme {id: "theme_recurring"})  CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_cascade_2024"}), (t:Theme {id: "theme_marginexp"}) CREATE (d)-[:HAS_THESIS_THEME]->(t);

// HealthRoll: roll_up, founder_transition
MATCH (d:Deal {id: "deal_healthroll_2020"}), (t:Theme {id: "theme_rollup"})  CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_healthroll_2020"}), (t:Theme {id: "theme_founder"}) CREATE (d)-[:HAS_THESIS_THEME]->(t);

// MidStates: market_consolidation
MATCH (d:Deal {id: "deal_midstates_2022"}), (t:Theme {id: "theme_consol"})  CREATE (d)-[:HAS_THESIS_THEME]->(t);


// -----------------------------------------------------------------------------
// 11. FLAGGED_RISK  (Deal -> RiskTheme)
// Risks identified but NOT the cause of a pass decision.
// (Passed deals' kill reasons live on PASSED_DUE_TO edges instead.)
// -----------------------------------------------------------------------------
MATCH (d:Deal {id: "deal_falcon_2025"}),     (r:RiskTheme {id: "risk_payer"})       CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_orion_2026"}),      (r:RiskTheme {id: "risk_customer"})    CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_orion_2026"}),      (r:RiskTheme {id: "risk_cycle"})       CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_acme_2021"}),       (r:RiskTheme {id: "risk_payer"})       CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_techflow_2019"}),   (r:RiskTheme {id: "risk_cycle"})       CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_cascade_2024"}),    (r:RiskTheme {id: "risk_integration"}) CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_cascade_2024"}),    (r:RiskTheme {id: "risk_customer"})    CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_healthroll_2020"}), (r:RiskTheme {id: "risk_regulatory"})  CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_midstates_2022"}),  (r:RiskTheme {id: "risk_cycle"})       CREATE (d)-[:FLAGGED_RISK]->(r);


// -----------------------------------------------------------------------------
// 12. PASSED_DUE_TO  (Deal -> RiskTheme, weight)
// Mirrors outcome.primary_reason (weight 0.7) + secondary_reasons (weight 0.4).
// Only emitted for status = "passed".
// -----------------------------------------------------------------------------
// Atlas: primary management_quality, secondary customer_concentration
MATCH (d:Deal {id: "deal_atlas_2022"}), (r:RiskTheme {id: "risk_mgmt"})     CREATE (d)-[:PASSED_DUE_TO {weight: 0.7}]->(r);
MATCH (d:Deal {id: "deal_atlas_2022"}), (r:RiskTheme {id: "risk_customer"}) CREATE (d)-[:PASSED_DUE_TO {weight: 0.4}]->(r);


// -----------------------------------------------------------------------------
// 13. BECAME  (Deal -> PortfolioCompany)
// All closed deals (held + exited) get a PortCo node.
// -----------------------------------------------------------------------------
MATCH (d:Deal {id: "deal_acme_2021"}),       (p:PortfolioCompany {id: "portco_acme"})       CREATE (d)-[:BECAME]->(p);
MATCH (d:Deal {id: "deal_techflow_2019"}),   (p:PortfolioCompany {id: "portco_techflow"})   CREATE (d)-[:BECAME]->(p);
MATCH (d:Deal {id: "deal_healthroll_2020"}), (p:PortfolioCompany {id: "portco_healthroll"}) CREATE (d)-[:BECAME]->(p);
MATCH (d:Deal {id: "deal_midstates_2022"}),  (p:PortfolioCompany {id: "portco_midstates"})  CREATE (d)-[:BECAME]->(p);


// -----------------------------------------------------------------------------
// 14. SIMILAR_TO  (Deal -> Deal, score, drivers)  — the HERO edge
// Mirrors each deal's `similar_deals_computed` array in deals.json.
// -----------------------------------------------------------------------------
// Falcon's precedents (the hero query)
MATCH (a:Deal {id: "deal_falcon_2025"}), (b:Deal {id: "deal_acme_2021"})
  CREATE (a)-[:SIMILAR_TO {score: 0.87, drivers: "subsector,size,deal_type"}]->(b);
MATCH (a:Deal {id: "deal_falcon_2025"}), (b:Deal {id: "deal_healthroll_2020"})
  CREATE (a)-[:SIMILAR_TO {score: 0.81, drivers: "subsector,thesis"}]->(b);
MATCH (a:Deal {id: "deal_falcon_2025"}), (b:Deal {id: "deal_atlas_2022"})
  CREATE (a)-[:SIMILAR_TO {score: 0.74, drivers: "sector,size"}]->(b);

// Orion's precedents
MATCH (a:Deal {id: "deal_orion_2026"}), (b:Deal {id: "deal_techflow_2019"})
  CREATE (a)-[:SIMILAR_TO {score: 0.83, drivers: "subsector,deal_type,size"}]->(b);
MATCH (a:Deal {id: "deal_orion_2026"}), (b:Deal {id: "deal_midstates_2022"})
  CREATE (a)-[:SIMILAR_TO {score: 0.71, drivers: "sector,geography"}]->(b);

// Backfill — between historical deals (gives KG visual richness)
MATCH (a:Deal {id: "deal_acme_2021"}), (b:Deal {id: "deal_healthroll_2020"})
  CREATE (a)-[:SIMILAR_TO {score: 0.79, drivers: "subsector,thesis"}]->(b);
MATCH (a:Deal {id: "deal_techflow_2019"}), (b:Deal {id: "deal_midstates_2022"})
  CREATE (a)-[:SIMILAR_TO {score: 0.76, drivers: "sector,geography"}]->(b);
MATCH (a:Deal {id: "deal_atlas_2022"}), (b:Deal {id: "deal_acme_2021"})
  CREATE (a)-[:SIMILAR_TO {score: 0.72, drivers: "subsector,size"}]->(b);
MATCH (a:Deal {id: "deal_healthroll_2020"}), (b:Deal {id: "deal_acme_2021"})
  CREATE (a)-[:SIMILAR_TO {score: 0.78, drivers: "subsector,thesis"}]->(b);
MATCH (a:Deal {id: "deal_midstates_2022"}), (b:Deal {id: "deal_techflow_2019"})
  CREATE (a)-[:SIMILAR_TO {score: 0.74, drivers: "sector,geography"}]->(b);


// =============================================================================
// 15. EXTENSIONS — Pet Food + Manufacturing deals, Documents, Experts, Macro,
//     Market Companies. Mirrors the additions in data/deals.json and the new
//     data/{documents,experts,macro,investment_criteria,market_companies}.json files.
// =============================================================================

// -- New sectors + subsectors -------------------------------------------------
CREATE (:Sector {id: "sector_consumer", key: "consumer_products", name: "Consumer Products"});
CREATE (:Sector {id: "sector_mfg",      key: "manufacturing",     name: "Manufacturing"});

CREATE (:Subsector {id: "sub_petfood",     key: "pet_food",              name: "Pet Food"});
CREATE (:Subsector {id: "sub_petsupplies", key: "pet_supplies",          name: "Pet Supplies"});
CREATE (:Subsector {id: "sub_packagedfood",key: "packaged_food",         name: "Packaged Food"});
CREATE (:Subsector {id: "sub_indcomp",     key: "industrial_components", name: "Industrial Components"});
CREATE (:Subsector {id: "sub_procmfg",     key: "process_manufacturing", name: "Process Manufacturing"});
CREATE (:Subsector {id: "sub_packaging",   key: "packaging",             name: "Packaging"});

// -- New themes + risks -------------------------------------------------------
CREATE (:Theme {id: "theme_premium",   key: "premiumization",         name: "Premiumization"});
CREATE (:Theme {id: "theme_opex",      key: "operational_excellence", name: "Operational Excellence"});
CREATE (:RiskTheme {id: "risk_commodity", key: "commodity_exposure",     name: "Commodity Exposure"});
CREATE (:RiskTheme {id: "risk_privlabel", key: "private_label_pressure", name: "Private Label Pressure"});

// -- New companies + portcos --------------------------------------------------
CREATE (:Company {id: "co_kibble",   name: "Pawsome Premium Foods Inc."});
CREATE (:Company {id: "co_whisker",  name: "Whisker Naturals LLC"});
CREATE (:Company {id: "co_paws",     name: "BarkBites Inc."});
CREATE (:Company {id: "co_crunch",   name: "Crunch Pet Co."});
CREATE (:Company {id: "co_forge",    name: "Forge Precision Components Inc."});
CREATE (:Company {id: "co_polymer",  name: "Polymer Process Industries LLC"});
CREATE (:Company {id: "co_packtech", name: "PackTech Solutions Co."});

CREATE (:PortfolioCompany {id: "portco_kibble",   name: "Pawsome Premium (PortCo, held)"});
CREATE (:PortfolioCompany {id: "portco_forge",    name: "Forge Precision (PortCo, exited 2023)"});
CREATE (:PortfolioCompany {id: "portco_polymer",  name: "Polymer Process (PortCo, exited 2024)"});
CREATE (:PortfolioCompany {id: "portco_packtech", name: "PackTech Solutions (PortCo, held)"});

// -- New deals ----------------------------------------------------------------
CREATE (:Deal {id: "deal_kibble_2024",  codename: "Project Kibble",  status: "closed_held",       year: 2024, revenue_ltm_usd: 168000000, ebitda_ltm_usd: 27000000, ebitda_margin: 0.161, ev_proposed_usd: 360000000, deal_type: "platform",  geography: "southeast_us"});
CREATE (:Deal {id: "deal_whisker_2025", codename: "Project Whisker", status: "active_diligence",  year: 2025, revenue_ltm_usd:  92000000, ebitda_ltm_usd: 14500000, ebitda_margin: 0.158, ev_proposed_usd: 210000000, deal_type: "platform",  geography: "west_us"});
CREATE (:Deal {id: "deal_paws_2023",    codename: "Project Paws",    status: "passed",            year: 2023, revenue_ltm_usd:  78000000, ebitda_ltm_usd:  8500000, ebitda_margin: 0.109, ev_proposed_usd: 145000000, deal_type: "platform",  geography: "midwest_us"});
CREATE (:Deal {id: "deal_crunch_2026",  codename: "Project Crunch",  status: "active_diligence",  year: 2026, revenue_ltm_usd: 215000000, ebitda_ltm_usd: 31000000, ebitda_margin: 0.144, ev_proposed_usd: 380000000, deal_type: "carve_out", geography: "national"});
CREATE (:Deal {id: "deal_forge_2018",   codename: "Project Forge",   status: "closed_exited",     year: 2018, revenue_ltm_usd: 140000000, ebitda_ltm_usd: 22000000, ebitda_margin: 0.157, ev_proposed_usd: 215000000, deal_type: "platform",  geography: "midwest_us"});
CREATE (:Deal {id: "deal_polymer_2019", codename: "Project Polymer", status: "closed_exited",     year: 2019, revenue_ltm_usd: 195000000, ebitda_ltm_usd: 29000000, ebitda_margin: 0.149, ev_proposed_usd: 280000000, deal_type: "platform",  geography: "southeast_us"});
CREATE (:Deal {id: "deal_packtech_2022",codename: "Project PackTech",status: "closed_held",       year: 2022, revenue_ltm_usd: 165000000, ebitda_ltm_usd: 24000000, ebitda_margin: 0.145, ev_proposed_usd: 245000000, deal_type: "platform",  geography: "northeast_us"});

// -- Edges: SUBJECT_OF / IN_SECTOR / IN_SUBSECTOR ----------------------------
MATCH (d:Deal {id: "deal_kibble_2024"}),   (c:Company {id: "co_kibble"})   CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_whisker_2025"}),  (c:Company {id: "co_whisker"})  CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_paws_2023"}),     (c:Company {id: "co_paws"})     CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_crunch_2026"}),   (c:Company {id: "co_crunch"})   CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_forge_2018"}),    (c:Company {id: "co_forge"})    CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_polymer_2019"}),  (c:Company {id: "co_polymer"})  CREATE (d)-[:SUBJECT_OF]->(c);
MATCH (d:Deal {id: "deal_packtech_2022"}), (c:Company {id: "co_packtech"}) CREATE (d)-[:SUBJECT_OF]->(c);

MATCH (d:Deal {id: "deal_kibble_2024"}),   (s:Sector {id: "sector_consumer"}) CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_whisker_2025"}),  (s:Sector {id: "sector_consumer"}) CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_paws_2023"}),     (s:Sector {id: "sector_consumer"}) CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_crunch_2026"}),   (s:Sector {id: "sector_consumer"}) CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_forge_2018"}),    (s:Sector {id: "sector_mfg"})      CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_polymer_2019"}),  (s:Sector {id: "sector_mfg"})      CREATE (d)-[:IN_SECTOR]->(s);
MATCH (d:Deal {id: "deal_packtech_2022"}), (s:Sector {id: "sector_mfg"})      CREATE (d)-[:IN_SECTOR]->(s);

MATCH (d:Deal {id: "deal_kibble_2024"}),   (s:Subsector {id: "sub_petfood"})    CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_whisker_2025"}),  (s:Subsector {id: "sub_petfood"})    CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_paws_2023"}),     (s:Subsector {id: "sub_petfood"})    CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_crunch_2026"}),   (s:Subsector {id: "sub_petfood"})    CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_forge_2018"}),    (s:Subsector {id: "sub_indcomp"})    CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_polymer_2019"}),  (s:Subsector {id: "sub_procmfg"})    CREATE (d)-[:IN_SUBSECTOR]->(s);
MATCH (d:Deal {id: "deal_packtech_2022"}), (s:Subsector {id: "sub_packaging"})  CREATE (d)-[:IN_SUBSECTOR]->(s);

// -- Edges: WORKED_ON ---------------------------------------------------------
MATCH (p:Person {id: "person_jsmith"}), (d:Deal {id: "deal_kibble_2024"})   CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_rpatel"}), (d:Deal {id: "deal_kibble_2024"})   CREATE (p)-[:WORKED_ON {role: "team"}]->(d);
MATCH (p:Person {id: "person_jsmith"}), (d:Deal {id: "deal_whisker_2025"})  CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_klee"}),   (d:Deal {id: "deal_whisker_2025"})  CREATE (p)-[:WORKED_ON {role: "team"}]->(d);
MATCH (p:Person {id: "person_mchen"}),  (d:Deal {id: "deal_paws_2023"})     CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_rpatel"}), (d:Deal {id: "deal_paws_2023"})     CREATE (p)-[:WORKED_ON {role: "team"}]->(d);
MATCH (p:Person {id: "person_mchen"}),  (d:Deal {id: "deal_crunch_2026"})   CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_klee"}),   (d:Deal {id: "deal_crunch_2026"})   CREATE (p)-[:WORKED_ON {role: "team"}]->(d);
MATCH (p:Person {id: "person_rpatel"}), (d:Deal {id: "deal_crunch_2026"})   CREATE (p)-[:WORKED_ON {role: "team"}]->(d);
MATCH (p:Person {id: "person_mchen"}),  (d:Deal {id: "deal_forge_2018"})    CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_klee"}),   (d:Deal {id: "deal_forge_2018"})    CREATE (p)-[:WORKED_ON {role: "team"}]->(d);
MATCH (p:Person {id: "person_jsmith"}), (d:Deal {id: "deal_polymer_2019"})  CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_rpatel"}), (d:Deal {id: "deal_polymer_2019"})  CREATE (p)-[:WORKED_ON {role: "team"}]->(d);
MATCH (p:Person {id: "person_mchen"}),  (d:Deal {id: "deal_packtech_2022"}) CREATE (p)-[:WORKED_ON {role: "lead"}]->(d);
MATCH (p:Person {id: "person_klee"}),   (d:Deal {id: "deal_packtech_2022"}) CREATE (p)-[:WORKED_ON {role: "team"}]->(d);

// -- Edges: HAS_THESIS_THEME (new deals) -------------------------------------
MATCH (d:Deal {id: "deal_kibble_2024"}),   (t:Theme {id: "theme_premium"})    CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_kibble_2024"}),   (t:Theme {id: "theme_recurring"})  CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_whisker_2025"}),  (t:Theme {id: "theme_premium"})    CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_whisker_2025"}),  (t:Theme {id: "theme_recurring"})  CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_whisker_2025"}),  (t:Theme {id: "theme_founder"})    CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_paws_2023"}),     (t:Theme {id: "theme_premium"})    CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_crunch_2026"}),   (t:Theme {id: "theme_marginexp"})  CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_crunch_2026"}),   (t:Theme {id: "theme_opex"})       CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_forge_2018"}),    (t:Theme {id: "theme_opex"})       CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_forge_2018"}),    (t:Theme {id: "theme_marginexp"})  CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_polymer_2019"}),  (t:Theme {id: "theme_opex"})       CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_polymer_2019"}),  (t:Theme {id: "theme_consol"})     CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_packtech_2022"}), (t:Theme {id: "theme_opex"})       CREATE (d)-[:HAS_THESIS_THEME]->(t);
MATCH (d:Deal {id: "deal_packtech_2022"}), (t:Theme {id: "theme_marginexp"})  CREATE (d)-[:HAS_THESIS_THEME]->(t);

// -- Edges: FLAGGED_RISK / PASSED_DUE_TO (new deals) -------------------------
MATCH (d:Deal {id: "deal_kibble_2024"}),   (r:RiskTheme {id: "risk_commodity"})  CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_kibble_2024"}),   (r:RiskTheme {id: "risk_privlabel"})  CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_whisker_2025"}),  (r:RiskTheme {id: "risk_commodity"})  CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_whisker_2025"}),  (r:RiskTheme {id: "risk_customer"})   CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_crunch_2026"}),   (r:RiskTheme {id: "risk_commodity"})  CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_crunch_2026"}),   (r:RiskTheme {id: "risk_integration"}) CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_forge_2018"}),    (r:RiskTheme {id: "risk_cycle"})       CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_polymer_2019"}),  (r:RiskTheme {id: "risk_cycle"})       CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_polymer_2019"}),  (r:RiskTheme {id: "risk_commodity"})   CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_packtech_2022"}), (r:RiskTheme {id: "risk_commodity"})   CREATE (d)-[:FLAGGED_RISK]->(r);
MATCH (d:Deal {id: "deal_packtech_2022"}), (r:RiskTheme {id: "risk_customer"})    CREATE (d)-[:FLAGGED_RISK]->(r);

MATCH (d:Deal {id: "deal_paws_2023"}), (r:RiskTheme {id: "risk_privlabel"})  CREATE (d)-[:PASSED_DUE_TO {weight: 0.7}]->(r);
MATCH (d:Deal {id: "deal_paws_2023"}), (r:RiskTheme {id: "risk_commodity"})  CREATE (d)-[:PASSED_DUE_TO {weight: 0.4}]->(r);

// -- Edges: BECAME (new closed deals) ----------------------------------------
MATCH (d:Deal {id: "deal_kibble_2024"}),   (p:PortfolioCompany {id: "portco_kibble"})   CREATE (d)-[:BECAME]->(p);
MATCH (d:Deal {id: "deal_forge_2018"}),    (p:PortfolioCompany {id: "portco_forge"})    CREATE (d)-[:BECAME]->(p);
MATCH (d:Deal {id: "deal_polymer_2019"}),  (p:PortfolioCompany {id: "portco_polymer"})  CREATE (d)-[:BECAME]->(p);
MATCH (d:Deal {id: "deal_packtech_2022"}), (p:PortfolioCompany {id: "portco_packtech"}) CREATE (d)-[:BECAME]->(p);

// -- Edges: SIMILAR_TO (new deals) -------------------------------------------
MATCH (a:Deal {id: "deal_kibble_2024"}),  (b:Deal {id: "deal_whisker_2025"}) CREATE (a)-[:SIMILAR_TO {score: 0.84, drivers: "subsector,thesis"}]->(b);
MATCH (a:Deal {id: "deal_kibble_2024"}),  (b:Deal {id: "deal_paws_2023"})    CREATE (a)-[:SIMILAR_TO {score: 0.77, drivers: "subsector,size"}]->(b);
MATCH (a:Deal {id: "deal_whisker_2025"}), (b:Deal {id: "deal_kibble_2024"})  CREATE (a)-[:SIMILAR_TO {score: 0.84, drivers: "subsector,thesis"}]->(b);
MATCH (a:Deal {id: "deal_whisker_2025"}), (b:Deal {id: "deal_paws_2023"})    CREATE (a)-[:SIMILAR_TO {score: 0.69, drivers: "subsector"}]->(b);
MATCH (a:Deal {id: "deal_crunch_2026"}),  (b:Deal {id: "deal_kibble_2024"})  CREATE (a)-[:SIMILAR_TO {score: 0.72, drivers: "subsector,size"}]->(b);
MATCH (a:Deal {id: "deal_forge_2018"}),   (b:Deal {id: "deal_polymer_2019"}) CREATE (a)-[:SIMILAR_TO {score: 0.78, drivers: "sector,thesis"}]->(b);
MATCH (a:Deal {id: "deal_forge_2018"}),   (b:Deal {id: "deal_packtech_2022"}) CREATE (a)-[:SIMILAR_TO {score: 0.66, drivers: "sector"}]->(b);

// -- Experts ------------------------------------------------------------------
CREATE (:Expert {id: "expert_jdoe",    name: "Jane Doe",        firm: "Channel Insights LLC"});
CREATE (:Expert {id: "expert_mfeld",   name: "Marcus Feldman",  firm: "Feldman Advisory"});
CREATE (:Expert {id: "expert_bstone",  name: "Barbara Stone",   firm: "Stone Healthcare Partners"});
CREATE (:Expert {id: "expert_lwong",   name: "Linda Wong",      firm: "Wong Regulatory Consulting"});
CREATE (:Expert {id: "expert_rgarza",  name: "Ricardo Garza",   firm: "Pet Industry Insights"});
CREATE (:Expert {id: "expert_tpark",   name: "Tom Park",        firm: "GTN Capital Network"});
CREATE (:Expert {id: "expert_sokafor", name: "Samuel Okafor",   firm: "Okafor Operations Partners"});

// -- Documents (key ones — full list in data/documents.json) -----------------
CREATE (:Document {id: "doc_8430",            doc_type: "expert_call", title: "Expert Call — Channel Pricing Dynamics in Outsourced Clinical Services"});
CREATE (:Document {id: "doc_kibble_cim",      doc_type: "cim",         title: "Project Kibble — CIM"});
CREATE (:Document {id: "doc_kibble_expert_1", doc_type: "expert_call", title: "Expert Call — Premium Pet Food Channel Pricing"});
CREATE (:Document {id: "doc_whisker_cim",     doc_type: "cim",         title: "Project Whisker — CIM"});
CREATE (:Document {id: "doc_paws_expert_1",   doc_type: "expert_call", title: "Expert Call — Private Label in Pet Food"});
CREATE (:Document {id: "doc_forge_expert_1",  doc_type: "expert_call", title: "Expert Call — Lean Ops in Precision Manufacturing"});

MATCH (d:Deal {id: "deal_falcon_2025"}),   (doc:Document {id: "doc_8430"})            CREATE (d)-[:HAS_DOCUMENT]->(doc);
MATCH (d:Deal {id: "deal_kibble_2024"}),   (doc:Document {id: "doc_kibble_cim"})      CREATE (d)-[:HAS_DOCUMENT]->(doc);
MATCH (d:Deal {id: "deal_kibble_2024"}),   (doc:Document {id: "doc_kibble_expert_1"}) CREATE (d)-[:HAS_DOCUMENT]->(doc);
MATCH (d:Deal {id: "deal_whisker_2025"}),  (doc:Document {id: "doc_whisker_cim"})     CREATE (d)-[:HAS_DOCUMENT]->(doc);
MATCH (d:Deal {id: "deal_paws_2023"}),     (doc:Document {id: "doc_paws_expert_1"})   CREATE (d)-[:HAS_DOCUMENT]->(doc);
MATCH (d:Deal {id: "deal_forge_2018"}),    (doc:Document {id: "doc_forge_expert_1"})  CREATE (d)-[:HAS_DOCUMENT]->(doc);

MATCH (doc:Document {id: "doc_8430"}),            (e:Expert {id: "expert_jdoe"})    CREATE (doc)-[:AUTHORED_BY]->(e);
MATCH (doc:Document {id: "doc_kibble_expert_1"}), (e:Expert {id: "expert_rgarza"})  CREATE (doc)-[:AUTHORED_BY]->(e);
MATCH (doc:Document {id: "doc_paws_expert_1"}),   (e:Expert {id: "expert_rgarza"})  CREATE (doc)-[:AUTHORED_BY]->(e);
MATCH (doc:Document {id: "doc_forge_expert_1"}),  (e:Expert {id: "expert_sokafor"}) CREATE (doc)-[:AUTHORED_BY]->(e);

// =============================================================================
// DEMO QUERIES — paste these one at a time into Neo4j Browser
// =============================================================================
//
// // DEMO QUERY Q1 — "All deals John Smith has led" (shows partner ownership)
// MATCH (p:Person {name: "John Smith"})-[w:WORKED_ON {role: "lead"}]->(d:Deal)-[:SUBJECT_OF]->(c:Company)
// RETURN p, w, d, c;
//
//
// // DEMO QUERY Q2 — HERO: "Project Falcon precedents and how they played out"
// MATCH (falcon:Deal {codename: "Project Falcon"})-[s:SIMILAR_TO]->(precedent:Deal)
// OPTIONAL MATCH (precedent)-[b:BECAME]->(portco:PortfolioCompany)
// RETURN falcon, s, precedent, b, portco;
//
//
// // DEMO QUERY Q3 — "What risks have we flagged across our healthcare passes?"
// MATCH (d:Deal)-[:IN_SECTOR]->(:Sector {name: "Healthcare Services"})
// WHERE d.status IN ["passed", "dead"]
// MATCH (d)-[r:PASSED_DUE_TO]->(risk:RiskTheme)
// RETURN d, r, risk;
//
//
// // BONUS — Falcon's full 2-hop neighborhood (the "wow" visual)
// MATCH path = (falcon:Deal {codename: "Project Falcon"})-[*1..2]-(n)
// RETURN path;
//
// =============================================================================
