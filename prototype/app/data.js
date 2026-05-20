/* ─────────────────────────────────────────────────────────────────────
 *  Fixture data
 * ───────────────────────────────────────────────────────────────────── */

window.DEALS = [
  // Active
  { id: "D-Pinetree", codename: "Pinetree",  company: "Greenpine Logistics",      sector: "transportation_logistics", year: 2026, status: "Active",    note: "QofE in flight" },
  { id: "D-Bramble",  codename: "Bramble",   company: "Bramble Medical Group",     sector: "healthcare_services",       year: 2026, status: "Active",    note: "LOI signed" },
  { id: "D-Caldera",  codename: "Caldera",   company: "Caldera Industrial Coatings", sector: "specialty_chemicals",     year: 2026, status: "Active",    note: "IC prep" },
  { id: "D-Larkspur", codename: "Larkspur",  company: "Larkspur Surgical Centers",   sector: "healthcare_services",     year: 2026, status: "Active",    note: "Mgmt mtg next wk" },

  // Portfolio
  { id: "D-Pinecrest",codename: "Pinecrest", company: "Pinecrest Foods Inc.",     sector: "consumer_products",          year: 2023, status: "Portfolio", note: "Held 2.4y" },
  { id: "D-Anvil",    codename: "Anvil",     company: "Anvil Distribution",       sector: "industrial_distribution",    year: 2022, status: "Portfolio", note: "Held 3.1y" },
  { id: "D-Marble",   codename: "Marble",    company: "Marblefield Software",     sector: "tech_enabled_services",      year: 2024, status: "Portfolio", note: "Held 1.6y" },

  // Exited
  { id: "D-Northwind",codename: "Northwind", company: "Northwind Apparel",        sector: "consumer_apparel",           year: 2019, status: "Exited",    note: "Exited Q2 '24 · 3.4×" },
  { id: "D-Atlas",    codename: "Atlas",     company: "Atlas Bus Services",       sector: "business_services",          year: 2018, status: "Exited",    note: "Exited Q4 '23 · 2.8×" },

  // Dead
  { id: "D-Conepine", codename: "Conepine",  company: "Conepine Health Network",  sector: "healthcare_services",        year: 2024, status: "Dead",      note: "Passed Q2 '24" },
  { id: "D-Slate",    codename: "Slate",     company: "Slate Roofing Supply",      sector: "construction_materials",     year: 2025, status: "Dead",      note: "Lost auction" },
];

window.SECTOR_SHORT = {
  healthcare_services:      "Healthcare",
  industrial_distribution:  "Industrial",
  tech_enabled_services:    "Tech-svcs",
  business_services:        "B2B svcs",
  consumer_products:        "Consumer",
  manufacturing:            "Mfg",
  specialty_chemicals:      "Chemicals",
  consumer_apparel:         "Apparel",
  construction_materials:   "Construction",
  consumer_tech:            "Con. tech",
  transportation_logistics: "Transport",
};

window.STATUS_COLOR = {
  Active:    "var(--st-active)",
  Portfolio: "var(--st-portfolio)",
  Exited:    "var(--st-exited)",
  Dead:      "var(--st-dead)",
};

// ─────────────────────────────────────────────────────────────────────
// Demo chat sessions — recent threads, with realistic titles
// ─────────────────────────────────────────────────────────────────────

window.SESSIONS = [
  {
    id: "s1",
    title: "Pinecrest — Q1 variance vs underwriting",
    scope: { dealId: "D-Pinecrest", codename: "Pinecrest", company: "Pinecrest Foods Inc.", status: "Portfolio" },
    updatedAt: Date.now() - 1000 * 60 * 90,         // 1.5h ago
    turns: 6,
    messages: [],   // demo seeds populated by main
  },
  {
    id: "s2",
    title: "Pinecrest — Customer concentration risk",
    scope: { dealId: "D-Pinecrest", codename: "Pinecrest", company: "Pinecrest Foods Inc.", status: "Portfolio" },
    updatedAt: Date.now() - 1000 * 60 * 60 * 22,
    turns: 4,
    messages: [],
  },
  {
    id: "s3",
    title: "Bramble — renewal exposure, top 5 customers",
    scope: { dealId: "D-Bramble", codename: "Bramble", company: "Bramble Medical Group", status: "Active" },
    updatedAt: Date.now() - 1000 * 60 * 60 * 30,
    turns: 7,
    messages: [],
  },
  {
    id: "s4",
    title: "Healthcare-services comps — Q1 multiples",
    scope: { statusGroup: "Active" },
    updatedAt: Date.now() - 1000 * 60 * 60 * 48,
    turns: 3,
    messages: [],
  },
  {
    id: "s5",
    title: "Why we passed on Conepine — reconstruct",
    scope: { dealId: "D-Conepine", codename: "Conepine", company: "Conepine Health Network", status: "Dead" },
    updatedAt: Date.now() - 1000 * 60 * 60 * 72,
    turns: 5,
    messages: [],
  },
  {
    id: "s6",
    title: "Northwind — what drove the 3.4× outcome",
    scope: { dealId: "D-Northwind", codename: "Northwind", company: "Northwind Apparel", status: "Exited" },
    updatedAt: Date.now() - 1000 * 60 * 60 * 24 * 6,
    turns: 8,
    messages: [],
  },
];

// ─────────────────────────────────────────────────────────────────────
// Front-page threads — shown on empty state
// ─────────────────────────────────────────────────────────────────────

window.FRONT_THREADS = [
  {
    n: "01",
    q: "Where is *Pinecrest Foods* drifting from the underwriting case?",
    statusGroup: "Portfolio",
    asks: "asked 3× this week",
    scope: { dealId: "D-Pinecrest", codename: "Pinecrest", company: "Pinecrest Foods Inc.", status: "Portfolio" },
    canonical: "Where is Pinecrest Foods drifting from the underwriting case?",
  },
  {
    n: "02",
    q: "Which exited deals cleared *3.0×* MOIC, and what did they share?",
    statusGroup: "Exited",
    asks: "asked 2× this week",
    scope: { statusGroup: "Exited" },
    canonical: "Which exited deals cleared 3.0× MOIC, and what did they share in common?",
  },
  {
    n: "03",
    q: "Summarise the reasons we *passed* on healthcare-services deals in 2025.",
    statusGroup: "Dead",
    asks: "VPs · IC prep",
    scope: { statusGroup: "Dead" },
    canonical: "Summarise the reasons we passed on healthcare-services deals in 2025.",
  },
  {
    n: "04",
    q: "*Active diligence pipeline* — leverage, sector, and quality-of-earnings status.",
    statusGroup: "Active",
    asks: "weekly",
    scope: { statusGroup: "Active" },
    canonical: "Give me the active diligence pipeline — leverage, sector, and quality-of-earnings status.",
  },
];

// ─────────────────────────────────────────────────────────────────────
// Demo Q&A — pre-canned answers with inline [1]…[n] markers + footnotes
// Picked by closest substring match.
// ─────────────────────────────────────────────────────────────────────

window.ANSWER_BANK = [
  {
    matchOn: ["pinecrest", "drift", "underwriting"],
    text:
`Three things are pulling Pinecrest off the underwriting case, in order of severity.

**1. Foodservice channel softness.** Q1 revenue grew 11% against an underwriting plan of 14%, with the entirety of the gap concentrated in foodservice<sup data-cite="1"></sup>. Retail and DTC are running ahead of plan; foodservice is running 600 bps behind.

**2. Margin pressure on private-label SKUs.** Gross margin compressed 140 bps YoY, driven by sustained input-cost inflation on dairy and packaging<sup data-cite="2"></sup>. Management's pass-through pricing took effect in late February — too late to recover Q1.

**3. CapEx pull-forward.** The Lebanon, TN plant retooling was originally a Y3 item; mgmt accelerated it to Y2 to capture a co-pack contract with a national QSR<sup data-cite="3"></sup>. The capex is incremental to underwriting but the contract is high-confidence and accretive on a 4-year view.

| Driver                | UW plan | Actual Q1 | Δ           |
| --------------------- | :-----: | :-------: | :---------: |
| Revenue growth        | +14.0%  | +11.0%    | (300 bps)   |
| Gross margin          | 28.6%   | 27.2%     | (140 bps)   |
| Adj. EBITDA           | $14.8M  | $13.1M    | ($1.7M)     |
| Leverage (net)        |  4.6×   |  5.0×     | +0.4×       |

The drift is real but not yet a thesis-level concern — pricing is now in market, and the foodservice softness tracks the wider QSR slowdown rather than a Pinecrest-specific share-loss story<sup data-cite="4"></sup>.`,
    citations: [
      { n: 1, title: "Pinecrest Q1 management report",   excerpt: "Foodservice revenue (38% of total) grew 4% vs +18% plan; retail +16% vs +12% plan.", type: "doc",      ref: "P-1042", date: "2026-04-22" },
      { n: 2, title: "EY QofE addendum — Q1 margin walk",excerpt: "Adj. GM compressed 140 bps; dairy input +9.4% YoY, paperboard +6.1% YoY.",         type: "doc",      ref: "P-1051", date: "2026-04-30" },
      { n: 3, title: "Deal memo — Pinecrest Y2 capex revision", excerpt: "Lebanon TN line retool pulled forward to support QSR co-pack agreement (4-yr).", type: "deal",   ref: "D-1108", date: "2026-03-11" },
      { n: 4, title: "Consumer foodservice multiples & volume", excerpt: "QSR same-store volumes -3.1% YoY in Q1; recovery expected H2 on lapping.",     type: "macro",   ref: "HC-Q1",  date: "2026-04-12" },
    ],
    provenance: { time: "2.1s", violations: 0 },
  },
  {
    matchOn: ["exited", "moic", "3", "share"],
    text:
`Four exited deals cleared 3.0× MOIC in the period. They share three traits more than the broader exited cohort.

| Deal       | MOIC | IRR  | Hold (yrs) | Sector             |
| ---------- | :--: | :--: | :--------: | ------------------ |
| Northwind  | 3.4× | 28%  |    4.6     | Consumer Apparel   |
| Atlas      | 3.1× | 24%  |    5.2     | Business Services  |
| Halifax    | 3.0× | 22%  |    5.0     | Industrial Dist.   |
| Vermillion | 3.2× | 31%  |    3.8     | Tech-enabled Svcs  |

**Common traits.** First, all four were acquired at or below the firm's cohort-median entry multiple — a 7.8× average vs. an 8.6× cohort median<sup data-cite="1"></sup>. Second, each was sold to a strategic rather than a sponsor, with a documented synergy story attached to the bid<sup data-cite="2"></sup>. Third, organic growth (not bolt-ons) drove the bulk of value creation: cohort-average organic revenue CAGR was 14.2% vs. 7.4% for the rest of the exited book<sup data-cite="3"></sup>.

The clearest single predictor in the dataset was the gap between entry multiple and cohort median<sup data-cite="4"></sup>. Hold period and sector were less informative.`,
    citations: [
      { n: 1, title: "Exited-deal book — entry/exit multiples (2018–2024)", excerpt: "Cohort median entry 8.6× EV/EBITDA; 3×+ MOIC subset 7.8× avg.", type: "doc",   ref: "EX-2024-04", date: "2025-01-10" },
      { n: 2, title: "Exit memos — bidder type & rationale",                excerpt: "All four ≥3× MOIC sold to strategic acquirers with named synergy targets.", type: "doc",   ref: "EX-MEMO",    date: "2024-09-30" },
      { n: 3, title: "Value-creation attribution — Atlas Crossing fund I/II", excerpt: "Organic revenue CAGR 14.2% for ≥3× cohort vs 7.4% remainder.",        type: "deal",  ref: "VC-ATTR",    date: "2025-02-12" },
      { n: 4, title: "Internal study — drivers of MOIC dispersion",          excerpt: "Entry multiple gap vs cohort median highest single correlation to MOIC (r=-0.62).", type: "criteria", ref: "IC-31",   date: "2025-03-05" },
    ],
    provenance: { time: "2.6s", violations: 0 },
  },
  {
    matchOn: ["passed", "healthcare", "2025"],
    text:
`We passed on eleven healthcare-services opportunities in 2025. The reasons cluster into four themes.

**1. Reimbursement risk** — five deals. CMS rate uncertainty (or a specific exposure to a code under review) was the single most-cited diligence finding<sup data-cite="1"></sup>. Conepine, Foxglove, and Birchwood all fell into this bucket; in each case the underwriting required a stable-or-better rate environment that we could not get comfortable with.

**2. Customer / payor concentration** — three deals. Top-3 payor share above 60% appeared in each, with no credible diversification path inside our hold<sup data-cite="2"></sup>.

**3. Multiple-discipline** — two deals. The price required to win exceeded the cohort underwriting band by more than 1.0×<sup data-cite="3"></sup>.

**4. Management depth** — one deal (Slatehill). Single-physician dependency without succession.

Across the eleven, only Conepine reached IC. We passed at IC on a unanimous vote, citing reimbursement risk as primary<sup data-cite="4"></sup>.`,
    citations: [
      { n: 1, title: "Diligence findings log — Healthcare 2025",       excerpt: "Reimbursement-risk language appears in 5/11 pass memos as primary.",   type: "doc",      ref: "DL-HC-25", date: "2025-12-15" },
      { n: 2, title: "Payor concentration — passed cohort",            excerpt: "Birchwood top-3 payor 71% of net revenue; Foxglove 64%.",             type: "doc",      ref: "P-PASS-HC", date: "2025-11-02" },
      { n: 3, title: "IC underwriting bands vs auction clears",        excerpt: "Two HC-svcs auctions cleared >1.0× above the firm's underwriting band.", type: "criteria", ref: "IC-22",     date: "2025-09-01" },
      { n: 4, title: "Conepine IC pass memo",                          excerpt: "Unanimous pass; primary reason: CMS rate uncertainty on code 99214.",   type: "deal",     ref: "D-Conepine", date: "2025-06-18" },
    ],
    provenance: { time: "1.9s", violations: 0 },
  },
  {
    matchOn: ["active", "pipeline", "leverage"],
    text:
`Four deals currently in active diligence.

| Codename   | Sector              | Entry leverage | QofE         | Stage           |
| ---------- | ------------------- | :------------: | :----------: | --------------- |
| Pinetree   | Transport / Logistics |     5.6×     | EY draft v2  | LOI signed      |
| Bramble    | Healthcare Services |     5.8×       | KPMG kickoff | Mgmt mtg done   |
| Caldera    | Specialty Chemicals |     5.4×       | Final        | IC next Tue     |
| Larkspur   | Healthcare Services |     6.2×       | Not started  | IOI submitted   |

Average target leverage across the four is 5.75× — comfortably within the IC cap of 6.0×, with Larkspur on the edge<sup data-cite="1"></sup>. Three of the four are within or below the cohort-median entry multiple for their sector in Q1<sup data-cite="2"></sup>; Bramble is the exception, currently 0.6× above the median.

**Concentration note.** Two of four are healthcare-services. Worth flagging to IC given the 2025 pass rate on the sector (see prior threads on healthcare-services passes)<sup data-cite="3"></sup>.`,
    citations: [
      { n: 1, title: "IC underwriting thresholds",                excerpt: "Leverage cap 6.0× at close; ratchet at 5.5× post-Y2.",                type: "criteria", ref: "IC-22", date: "2025-09-01" },
      { n: 2, title: "Cohort-median multiples by sector — Q1 2026", excerpt: "HC-svcs median 9.4× EV/EBITDA; Bramble target clears 10.0×.",          type: "macro",    ref: "HC-Q1", date: "2026-04-12" },
      { n: 3, title: "Healthcare-services pass log 2025",         excerpt: "11 passes; 5 cited reimbursement risk as primary.",                    type: "doc",      ref: "DL-HC-25", date: "2025-12-15" },
    ],
    provenance: { time: "2.4s", violations: 0 },
  },
];

window.findAnswer = function(text) {
  const t = text.toLowerCase();
  let best = null, bestScore = 0;
  for (const a of window.ANSWER_BANK) {
    const score = a.matchOn.reduce((acc, k) => acc + (t.includes(k) ? 1 : 0), 0);
    if (score > bestScore) { best = a; bestScore = score; }
  }
  return bestScore >= 1 ? best : window.ANSWER_BANK[0];
};

window.relativeTime = function(ts) {
  const diff = (Date.now() - ts) / 1000;
  if (diff < 60)             return "just now";
  if (diff < 60 * 60)        return Math.floor(diff / 60) + "m ago";
  if (diff < 60 * 60 * 24)   return Math.floor(diff / 3600) + "h ago";
  if (diff < 60 * 60 * 24 * 7) {
    const d = Math.floor(diff / 86400);
    return d === 1 ? "yesterday" : d + "d ago";
  }
  return new Date(ts).toLocaleDateString(undefined, { month: "short", day: "numeric" });
};

window.formatScope = function(scope) {
  if (!scope) return null;
  if (scope.codename)    return { kind: "deal",   primary: "Project " + scope.codename, status: scope.status };
  if (scope.statusGroup) return { kind: "group",  primary: scope.statusGroup, status: scope.statusGroup };
  return null;
};
