/** Per-tool citation extractors.
 *
 * The model's <sup data-cite="N"></sup> markers reference the 1-indexed tool
 * call. Each extractor returns a `Citation` for the rail (or `null` to skip,
 * e.g. for directory/index calls that aren't sources). The orchestrator
 * renumbers the rendered citations and rewrites the markers so the
 * displayed indexes are gap-free.
 */

import { driveUrlForDeal } from "./drive-index";
import type { Citation } from "./types";

type Rec = Record<string, unknown>;
type Extractor = (input: Rec, result: unknown) => Omit<Citation, "n"> | null;

function snip(s: string, max = 200): string {
  s = s.replace(/\s+/g, " ").trim();
  return s.length > max ? s.slice(0, max - 1) + "…" : s;
}

function titleCase(s: string): string {
  return s
    .split(/[_\s-]+/)
    .filter(Boolean)
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");
}

function displayCodename(d: Rec): string {
  const raw = (d.codename as string) ?? "";
  if (raw && /[a-z]/.test(raw) && raw.includes("_")) return titleCase(raw);
  return raw.trim();
}

/** Turn `deal_cardinal_filtration_co_2014` into `Cardinal Filtration Co. · 2014`. */
function humanizeDealRef(dealId: string): string {
  const stripped = dealId.replace(/^deal_/, "");
  const m = stripped.match(/^(.*)_(\d{4})$/);
  if (m) return `${titleCase(m[1])} · ${m[2]}`;
  return titleCase(stripped);
}

/** Compact document ref: `doc_halcyon_pet_foods_004` → `Halcyon Pet Foods · 004`. */
function humanizeDocRef(docId: string): string {
  const stripped = docId.replace(/^doc_/, "");
  const m = stripped.match(/^(.*)_(\d+)$/);
  if (m) return `${titleCase(m[1])} · ${m[2]}`;
  return titleCase(stripped);
}

function today(): string {
  return new Date().toISOString().slice(0, 10);
}

function dealSummary(d: Rec): string | undefined {
  const bits: string[] = [];
  if (typeof d.revenue_ltm_usd === "number")
    bits.push(`LTM rev $${(d.revenue_ltm_usd / 1e6).toFixed(0)}M`);
  if (typeof d.ebitda_ltm_usd === "number")
    bits.push(`EBITDA $${(d.ebitda_ltm_usd / 1e6).toFixed(0)}M`);
  if (typeof d.ev_ebitda_multiple === "number")
    bits.push(`${(d.ev_ebitda_multiple as number).toFixed(1)}× EV/EBITDA`);
  if (typeof d.moic === "number") bits.push(`MOIC ${(d.moic as number).toFixed(1)}×`);
  if (typeof d.irr === "number") bits.push(`IRR ${((d.irr as number) * 100).toFixed(1)}%`);
  return bits.length ? bits.join(" · ") : undefined;
}

// ── per-tool extractors ────────────────────────────────────────────────────

function dealRecord(label: string): Extractor {
  return (_input, result) => {
    const r = result as Rec;
    if (!r || typeof r !== "object") return null;
    const code = displayCodename(r);
    const company = ((r.company as string) ?? "").trim();
    const dealId = (r.deal_id as string) ?? "";
    return {
      title: company && company !== code ? `${code} — ${label}` : `${code} ${label}`.trim(),
      excerpt: dealSummary(r),
      type: "deal record",
      ref: dealId ? humanizeDealRef(dealId) : code,
      date: (r.year as number | undefined)?.toString() ?? today(),
      url: driveUrlForDeal(dealId),
    };
  };
}

const outcomeMemo: Extractor = (_input, result) => {
  const r = result as Rec;
  if (!r || typeof r !== "object") return null;
  const code = displayCodename(r);
  const dealId = (r.deal_id as string) ?? "";
  const tracking = r.post_decision_tracking;
  const excerpt =
    typeof tracking === "string" && tracking ? snip(tracking, 220) : dealSummary(r);
  return {
    title: `${code} — outcome IC memo`,
    excerpt,
    type: "ic_memo",
    ref: dealId ? humanizeDealRef(dealId) : code,
    date:
      (r.exit_year as number | undefined)?.toString() ??
      (r.decision_date as string) ??
      today(),
    url: driveUrlForDeal(dealId),
  };
};

const portcoPerf: Extractor = (_input, result) => {
  const r = result as Rec;
  if (!r) return null;
  const code = displayCodename(r);
  const dealId = (r.deal_id as string) ?? "";
  const actuals = (r.actuals as Rec[] | undefined) ?? [];
  const years = actuals
    .map((a) => a.year as number | undefined)
    .filter((y): y is number => typeof y === "number");
  const span =
    years.length > 0 ? `${Math.min(...years)}–${Math.max(...years)}` : "";
  const latest = actuals[actuals.length - 1];
  const revBit =
    latest && typeof latest.revenue_usd === "number"
      ? `Latest: $${((latest.revenue_usd as number) / 1e6).toFixed(0)}M revenue${
          typeof latest.ebitda_margin === "number"
            ? ` · ${((latest.ebitda_margin as number) * 100).toFixed(1)}% EBITDA margin`
            : ""
        }`
      : undefined;
  return {
    title: `${code} — quarterly actuals${span ? ` (${span})` : ""}`,
    excerpt: revBit,
    type: "performance data",
    ref: dealId ? humanizeDealRef(dealId) : code,
    date: years.length ? String(Math.max(...years)) : today(),
    url: driveUrlForDeal(dealId),
  };
};

const variance =
  (label: string): Extractor =>
  (_input, result) => {
    const r = result as Rec;
    if (!r) return null;
    const code = displayCodename(r);
    const dealId = (r.deal_id as string) ?? "";
    return {
      title: `${code} — ${label}`,
      excerpt: undefined,
      type: "variance report",
      ref: dealId ? humanizeDealRef(dealId) : code,
      date: today(),
      url: driveUrlForDeal(dealId),
    };
  };

const exitAnalysis: Extractor = (input, result) => {
  const r = result as Rec;
  const sector = ((input.sector as string) ?? (r?.sector as string) ?? "").trim();
  const status = ((input.status as string) ?? (r?.status as string) ?? "closed_exited")
    .trim()
    .replace(/_/g, " ");
  const count = (r?.count as number) ?? 0;
  const themes = (r?.top_thesis_themes as [string, number][] | undefined)?.slice(0, 3) ?? [];
  const themeStr = themes.map(([t]) => titleCase(t)).join(", ");
  return {
    title: `Exit-driver analysis — ${titleCase(sector)}`,
    excerpt: count
      ? `Aggregated across ${count} ${status} deal(s)${themeStr ? `; common themes: ${themeStr}` : ""}.`
      : undefined,
    type: "analysis",
    ref: `${titleCase(sector)} · ${status}`,
    date: today(),
  };
};

const precedentSearch: Extractor = (input, result) => {
  const r = result as Rec;
  const anchorRaw =
    ((input.deal as string) ?? ((input.profile as Rec)?.codename as string) ?? "").trim();
  const anchor = anchorRaw ? displayCodename({ codename: anchorRaw }) : "";
  const deals = (r?.deals as Rec[] | undefined) ?? (r?.results as Rec[] | undefined) ?? [];
  return {
    title: `Precedent search${anchor ? ` — anchored on ${anchor}` : ""}`,
    excerpt: deals.length ? `${deals.length} similar deal(s) returned` : undefined,
    type: "analysis",
    ref: anchor ? `Precedents · ${anchor}` : "Precedent search",
    date: today(),
  };
};

const sideBySide: Extractor = (input, _result) => {
  const ids = (input.deal_ids as string[] | undefined) ?? [];
  const labels = ids.map(humanizeDealRef);
  return {
    title: `Side-by-side — ${labels.map((l) => l.split(" · ")[0]).join(" vs ") || "deals"}`,
    excerpt: undefined,
    type: "comparison",
    ref: labels.join(" / ") || "Comparison",
    date: today(),
  };
};

const docHit: Extractor = (_input, result) => {
  const r = result as Rec;
  if (!r) return null;
  const hits = r.hits as Rec[] | undefined;
  if (!Array.isArray(hits) || hits.length === 0) return null;
  const h = hits[0];
  const docType = ((h.doc_type as string) ?? "doc").trim();
  const docId = (h.doc_id as string) ?? "";
  const dealId = (h.deal_id as string) ?? "";
  const topic = h.topic ? ` — ${h.topic}` : "";
  return {
    title: `${(h.title as string) ?? "Document"}${topic}`,
    excerpt: h.match_text ? `“${snip(h.match_text as string)}”` : undefined,
    type: docType,
    ref: docId ? humanizeDocRef(docId) : "doc",
    date: (h.date as string) ?? today(),
    url: driveUrlForDeal(dealId),
  };
};

const fullDoc: Extractor = (_input, result) => {
  const r = result as Rec;
  if (!r || typeof r !== "object" || r.error) return null;
  const docId = (r.doc_id as string) ?? "";
  const docType = ((r.doc_type as string) ?? "doc").trim();
  const dealId = (r.deal_id as string) ?? "";
  return {
    title: (r.title as string) ?? "Document",
    excerpt:
      typeof r.summary === "string"
        ? snip(r.summary as string)
        : typeof r.full_text_excerpt === "string"
        ? snip(r.full_text_excerpt as string)
        : undefined,
    type: docType,
    ref: docId ? humanizeDocRef(docId) : "doc",
    date: (r.date as string) ?? today(),
    url: driveUrlForDeal(dealId),
  };
};

const cimEval: Extractor = (input, result) => {
  const r = result as Rec;
  const docId = (input.cim_doc_id as string) ?? "";
  return {
    title: `CIM evaluation — ${docId ? humanizeDocRef(docId) : "doc"}`,
    excerpt:
      typeof r?.summary === "string" ? snip(r.summary as string) : undefined,
    type: "criteria check",
    ref: docId ? humanizeDocRef(docId) : "CIM eval",
    date: today(),
  };
};

const macroSnap: Extractor = (input, result) => {
  const r = result as Rec;
  const sector = ((input.sector as string) ?? (r?.sector as string) ?? "").trim();
  const asOf = ((input.as_of as string) ?? (r?.as_of as string) ?? "").trim();
  return {
    title: `Macro snapshot — ${titleCase(sector)}${asOf ? ` (${asOf})` : ""}`,
    excerpt: undefined,
    type: "macro",
    ref: `${titleCase(sector)}${asOf ? ` · ${asOf}` : ""}`,
    date: asOf || today(),
  };
};

const macroCompareEx: Extractor = (input, _result) => {
  const sector = ((input.sector as string) ?? "").trim();
  const a = ((input.date_a as string) ?? "").trim();
  const b = ((input.date_b as string) ?? "").trim();
  return {
    title: `Macro comparison — ${titleCase(sector)}`,
    excerpt: a && b ? `${a} → ${b}` : undefined,
    type: "macro",
    ref: `${titleCase(sector)} · ${a} → ${b}`,
    date: b || today(),
  };
};

const companyProfile: Extractor = (_input, result) => {
  const r = result as Rec;
  if (!r || typeof r !== "object") return null;
  const code = displayCodename(r);
  const company = ((r.company as string) ?? "").trim();
  const dealId = (r.deal_id as string) ?? "";
  return {
    title: company && company !== code ? `${code} — company profile` : `${code} profile`,
    excerpt: undefined,
    type: "company profile",
    ref: dealId ? humanizeDealRef(dealId) : company || code,
    date: today(),
    url: driveUrlForDeal(dealId),
  };
};

const criteriaDoc: Extractor = (_input, _result) => ({
  title: "Investment criteria — Atlas Crossing Partners",
  excerpt: "Size band, sector preferences, thesis preferences, leverage caps.",
  type: "criteria",
  ref: "Atlas Crossing IC",
  date: today(),
});

// Sources rail = real documents only. Everything else (deal records,
// variance reports, analyses, comparisons, macro snapshots, the criteria
// table) is structured data, not a source — those tools are still useful
// to the model for reasoning but they don't earn a row in the rail. The
// system prompt forces the model to back every factual claim with a
// `search_documents` or `get_document` call so the user can verify in Drive.
const EXTRACTORS: Record<string, Extractor | "skip"> = {
  // Documents only — these surface in the rail.
  search_documents: docHit,
  get_document: fullDoc,
  parse_cim: fullDoc,

  // Everything else is reasoning fuel, not a source.
  list_deals: "skip",
  source_similar_companies: "skip",
  get_deal: "skip",
  get_deal_financials: "skip",
  get_deal_outcome: "skip",
  get_portco_performance: "skip",
  get_underwriting_case: "skip",
  compare_portco_vs_underwriting: "skip",
  compare_exit_vs_underwriting: "skip",
  find_precedent_deals: "skip",
  compare_deals: "skip",
  analyze_exit_drivers: "skip",
  evaluate_cim_against_criteria: "skip",
  get_macro_snapshot: "skip",
  compare_macro: "skip",
  get_company_profile: "skip",
  get_investment_criteria: "skip",
};

/** Returns a citation for the given tool call, or null if the tool is a
 * directory/index that shouldn't appear in the source rail. The caller is
 * responsible for assigning the displayed `n` after filtering. */
export function buildCitation(
  toolName: string,
  toolInput: Rec,
  result: unknown,
): Omit<Citation, "n"> | null {
  const ex = EXTRACTORS[toolName];
  if (ex === "skip") return null;
  if (!ex) {
    return {
      title: toolName.replace(/_/g, " "),
      excerpt: undefined,
      type: "tool",
      ref: toolName,
      date: today(),
    };
  }
  return ex(toolInput, result);
}
