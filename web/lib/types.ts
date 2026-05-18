export type StatusGroup = "Active" | "Portfolio" | "Exited" | "Dead";

export type SectorKey =
  | "healthcare_services"
  | "industrial_distribution"
  | "tech_enabled_services"
  | "business_services"
  | "consumer_products"
  | "manufacturing"
  | "specialty_chemicals"
  | "consumer_apparel"
  | "construction_materials"
  | "consumer_tech"
  | "transportation_logistics";

export type Deal = {
  id: string;
  codename: string;
  company: string;
  sector: SectorKey;
  year: number;
  status: StatusGroup;
  note?: string;
};

export type ScopeContext = {
  dealId?: string;
  codename?: string;
  company?: string;
  status?: StatusGroup;
  statusGroup?: StatusGroup;
};

export type Citation = {
  n: number;
  title: string;
  excerpt?: string;
  /** Specific document type (e.g. "ic_memo", "expert_call", "dd_report"),
   *  or one of the generic buckets: "doc" | "deal" | "macro" | "criteria". */
  type: string;
  ref: string;
  date: string;
  /** When set, the source rail renders the title as an external link. */
  url?: string;
};

export type Provenance = {
  verdict: "pass" | "fail";
  time: string;
  violations: number;
};

export type ActivityItem = {
  id: string;
  name: string;
  input: Record<string, unknown>;
  status: "pending" | "done" | "failed";
  durationMs?: number;
};

export type AssistantMessage = {
  id: string;
  role: "assistant";
  status: "streaming" | "done" | "error";
  text: string;
  activity: ActivityItem[];
  citations: Citation[];
  provenance?: Provenance;
  error?: string;
};

export type ChatMessage =
  | { id: string; role: "user"; content: string }
  | AssistantMessage;

export type Session = {
  id: string;
  title: string;
  scope: ScopeContext | null;
  updatedAt: number;
  turns: number;
  messages: ChatMessage[];
};

export type FrontThread = {
  n: string;
  q: string;
  statusGroup: StatusGroup;
  asks: string;
  scope: ScopeContext;
  canonical: string;
};

/** Inline CSS custom property style helper for TS. */
export type CSSVarStyle = React.CSSProperties & Record<`--${string}`, string>;
