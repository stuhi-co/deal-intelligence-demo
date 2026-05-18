import type { FrontThread, SectorKey, Session, StatusGroup } from "./types";

// Deals come from the FastAPI tool server (api/) → mcp_server data, which
// mirrors the Atlas Crossing Partners Drive folder. See web/lib/deals-loader.ts.

export const SECTOR_SHORT: Record<SectorKey, string> = {
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

export const STATUS_COLOR: Record<StatusGroup, string> = {
  Active:    "var(--st-active)",
  Portfolio: "var(--st-portfolio)",
  Exited:    "var(--st-exited)",
  Dead:      "var(--st-dead)",
};

export const STATUS_GROUPS: StatusGroup[] = ["Active", "Portfolio", "Exited", "Dead"];

// Chat sessions accumulate as the user converses; no seed history.
export const SESSIONS: Session[] = [];

export const FRONT_THREADS: FrontThread[] = [
  {
    n: "01",
    q: "What is our fund's investment criteria? List out all of our investments and fund performance.",
    statusGroup: "Active",
    asks: "",
    scope: {},
    canonical: "What is our fund's investment criteria? List out all of our investments and fund performance.",
  },
  {
    n: "02",
    q: "How are our active portcos performing vs. underwriting case?",
    statusGroup: "Portfolio",
    asks: "",
    scope: { statusGroup: "Portfolio" },
    canonical: "How are our active portcos performing vs. the underwriting case?",
  },
  {
    n: "03",
    q: "Across our exits, how well-calibrated has our underwriting been? Do we systematically over- or under-project IRR, and by how much?",
    statusGroup: "Exited",
    asks: "",
    scope: { statusGroup: "Exited" },
    canonical:
      "Across our exits, how well-calibrated has our underwriting been? Do we systematically over- or under-project IRR, and by how much?",
  },
  {
    n: "04",
    q: "Have we ever passed on a deal that resembled one we later closed and made money on? What was the reason we passed?",
    statusGroup: "Dead",
    asks: "",
    scope: {},
    canonical:
      "Have we ever passed on a deal that resembled one we later closed and made money on? What was the reason we passed?",
  },
  {
    n: "05",
    q: "For our exited companies, what do the winners have in common?",
    statusGroup: "Exited",
    asks: "",
    scope: { statusGroup: "Exited" },
    canonical: "For our exited companies, what do the winners have in common?",
  },
  {
    n: "06",
    q: "Run Aurora's CIM against our fund's investment criteria.",
    statusGroup: "Active",
    asks: "",
    scope: {
      dealId: "deal_project_aurora_2026",
      codename: "Project Aurora",
      company: "Helix Specialty Chemicals, Inc.",
      status: "Active",
    },
    canonical: "Run Project Aurora's CIM against our fund's investment criteria.",
  },
  {
    n: "07",
    q: "Give me a list of all consumer companies we've looked at in the past three years.",
    statusGroup: "Active",
    asks: "",
    scope: {},
    canonical:
      "Give me a list of all consumer companies we've looked at in the past three years.",
  },
  {
    n: "08",
    q: "Wholesum is tracking below our underwriting case. Where exactly is the gap — revenue, margin, or growth pace — and when did it first show up?",
    statusGroup: "Portfolio",
    asks: "",
    scope: {
      dealId: "deal_wholesum_foods_distribution_2022",
      codename: "Wholesum Foods Distribution",
      company: "Wholesum Foods Distribution, Inc.",
      status: "Portfolio",
    },
    canonical:
      "Wholesum is tracking below our underwriting case. Where exactly is the gap — revenue, margin, or growth pace — and when did it first show up?",
  },
  {
    n: "09",
    q: "On our exits that underperformed the base case, what DD risks did we flag pre-close that we ended up underweighting?",
    statusGroup: "Exited",
    asks: "",
    scope: { statusGroup: "Exited" },
    canonical:
      "On our exits that underperformed the base case, what DD risks did we flag pre-close that we ended up underweighting?",
  },
  {
    n: "10",
    q: "Of our 5 active deals, which best matches the economic profile of our top-performing exits?",
    statusGroup: "Active",
    asks: "",
    scope: { statusGroup: "Active" },
    canonical:
      "Of our 5 active deals, which best matches the economic profile of our top-performing exits?",
  },
];

