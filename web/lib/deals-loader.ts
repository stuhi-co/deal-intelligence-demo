/** Loads the real deal list from the FastAPI tool server (mirrors Drive). */

import "server-only";

import { invokeTool } from "./tool-client";
import type { Deal, SectorKey, StatusGroup } from "./types";

const STATUS_MAP: Record<string, StatusGroup> = {
  active_diligence: "Active",
  closed_held: "Portfolio",
  closed_exited: "Exited",
  dead: "Dead",
  passed: "Dead",
};

const KNOWN_SECTORS: SectorKey[] = [
  "healthcare_services",
  "industrial_distribution",
  "tech_enabled_services",
  "business_services",
  "consumer_products",
  "manufacturing",
  "specialty_chemicals",
  "consumer_apparel",
  "construction_materials",
  "consumer_tech",
  "transportation_logistics",
];

function humanize(s: string): string {
  // "project_pegasus" → "Project Pegasus", "vanguard_auto" → "Vanguard Auto"
  return s
    .split(/[_\s]+/)
    .filter(Boolean)
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");
}

function normalizeSector(raw: string | undefined): SectorKey {
  if (!raw) return "business_services";
  return (KNOWN_SECTORS as readonly string[]).includes(raw)
    ? (raw as SectorKey)
    : "business_services";
}

type RawDeal = {
  deal_id: string;
  codename: string;
  company: string;
  status: string;
  year: number;
  sector: string;
};

export async function loadDealTree(): Promise<Deal[]> {
  const r = (await invokeTool("list_deals", {})) as { deals: RawDeal[] };
  return (r?.deals ?? []).map((d) => {
    const codename = /[a-z]/.test(d.codename) && d.codename.includes("_")
      ? humanize(d.codename)
      : d.codename.trim();
    return {
      id: d.deal_id,
      codename,
      company: d.company.trim(),
      sector: normalizeSector(d.sector),
      year: d.year,
      status: STATUS_MAP[d.status] ?? "Dead",
    };
  });
}
