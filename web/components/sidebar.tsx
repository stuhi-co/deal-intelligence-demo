"use client";

import { useEffect, useMemo, useState } from "react";
import { useTheme } from "next-themes";
import { Icons } from "./icons";
import { SECTOR_SHORT, STATUS_COLOR, STATUS_GROUPS } from "@/lib/fixtures";
import { relativeTime } from "@/lib/utils";
import type {
  CSSVarStyle,
  Deal,
  ScopeContext,
  Session,
  StatusGroup,
} from "@/lib/types";

type Props = {
  deals: Deal[];
  sessions: Session[];
  currentSessionId: string | null;
  scope: ScopeContext | null;
  onNewChat: () => void;
  onPickSession: (id: string) => void;
  onScopeDeal: (deal: Deal) => void;
  onOpenPalette: () => void;
};

export function Sidebar({
  deals,
  sessions,
  currentSessionId,
  scope,
  onNewChat,
  onPickSession,
  onScopeDeal,
  onOpenPalette,
}: Props) {
  const [tab, setTab] = useState<"deals" | "chats">("deals");
  const [query, setQuery] = useState("");
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  useEffect(() => setMounted(true), []);

  const sorted = useMemo(
    () => [...sessions].sort((a, b) => b.updatedAt - a.updatedAt),
    [sessions],
  );

  const dealsByGroup = useMemo(() => {
    const q = query.trim().toLowerCase();
    const out: Record<StatusGroup, Deal[]> = {
      Active: [],
      Portfolio: [],
      Exited: [],
      Dead: [],
    };
    for (const d of deals) {
      if (q) {
        const hay = [d.codename, d.company, SECTOR_SHORT[d.sector] ?? d.sector]
          .join(" ")
          .toLowerCase();
        if (!hay.includes(q)) continue;
      }
      out[d.status].push(d);
    }
    return out;
  }, [deals, query]);

  const grouped = useMemo(() => {
    const q = query.trim().toLowerCase();
    const out: Record<StatusGroup | "Other", Session[]> = {
      Active: [],
      Portfolio: [],
      Exited: [],
      Dead: [],
      Other: [],
    };
    for (const s of sorted) {
      if (q && !s.title.toLowerCase().includes(q)) continue;
      const k = (s.scope?.status ?? s.scope?.statusGroup ?? "Other") as keyof typeof out;
      (out[k] ?? out.Other).push(s);
    }
    return out;
  }, [sorted, query]);

  const totalDeals = deals.length;
  const totalChats = sessions.length;

  return (
    <aside className="side">
      {/* Icon rail */}
      <div className="rail">
        <div className="brand" title="Atlas Crossing">A</div>
        <button className="rail-btn" onClick={onNewChat} aria-label="New chat">
          <Icons.Plus size={17} />
          <span className="tip">New chat &nbsp;·&nbsp; ⌘N</span>
        </button>
        <button
          className="rail-btn"
          onClick={onOpenPalette}
          aria-label="Search"
        >
          <Icons.Search size={16} />
          <span className="tip">Scope a deal &nbsp;·&nbsp; ⌘K</span>
        </button>

        <div className="grow" />

        <button
          className="rail-btn"
          onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
          aria-label="Toggle theme"
        >
          {mounted && (theme === "dark" ? <Icons.Sun size={16} /> : <Icons.Moon size={16} />)}
          {mounted && (
            <span className="tip">{theme === "dark" ? "Light mode" : "Dark mode"}</span>
          )}
        </button>
      </div>

      {/* Chats column */}
      <div className="col">
        <div className="col-head">
          <h2>
            Atlas <em>Crossing</em>
          </h2>
          <div className="sub">Deal Intelligence</div>
        </div>

        <button className="new-chat" onClick={onNewChat}>
          <span style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <Icons.Plus size={14} />
            New chat
          </span>
          <span className="kbd">⌘N</span>
        </button>

        {/* Tabs */}
        <div className="col-tabs" role="tablist">
          <button
            role="tab"
            aria-selected={tab === "chats"}
            className={tab === "chats" ? "active" : ""}
            onClick={() => setTab("chats")}
          >
            Chats <span className="tnum count">{totalChats}</span>
          </button>
          <button
            role="tab"
            aria-selected={tab === "deals"}
            className={tab === "deals" ? "active" : ""}
            onClick={() => setTab("deals")}
          >
            Deals <span className="tnum count">{totalDeals}</span>
          </button>
        </div>

        {/* Search */}
        <div className="col-search">
          <Icons.Search size={13} />
          <input
            type="text"
            placeholder={tab === "deals" ? "Search deals…" : "Search chats…"}
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            aria-label="Search"
          />
          {query && (
            <button
              className="clear"
              onClick={() => setQuery("")}
              aria-label="Clear search"
            >
              <Icons.Close size={11} />
            </button>
          )}
        </div>

        <div className="chats">
          {tab === "deals" ? (
            STATUS_GROUPS.map((g) =>
              dealsByGroup[g].length ? (
                <DealGroup
                  key={g}
                  label={g}
                  color={STATUS_COLOR[g]}
                  deals={dealsByGroup[g]}
                  activeDealId={scope?.dealId}
                  onPick={onScopeDeal}
                />
              ) : null,
            )
          ) : (
            <>
              {STATUS_GROUPS.map((g) =>
                grouped[g].length ? (
                  <SessionGroup
                    key={g}
                    label={g}
                    color={STATUS_COLOR[g]}
                    sessions={grouped[g]}
                    currentId={currentSessionId}
                    onPick={onPickSession}
                  />
                ) : null,
              )}
              {grouped.Other.length ? (
                <SessionGroup
                  key="other"
                  label="Other"
                  color="var(--fg-faint)"
                  sessions={grouped.Other}
                  currentId={currentSessionId}
                  onPick={onPickSession}
                />
              ) : null}
            </>
          )}

          {tab === "deals" &&
            query &&
            Object.values(dealsByGroup).every((a) => !a.length) && (
              <div className="empty-result">No deals match “{query}”.</div>
            )}
          {tab === "chats" &&
            query &&
            Object.values(grouped).every((a) => !a.length) && (
              <div className="empty-result">No chats match “{query}”.</div>
            )}
          {tab === "chats" && !query && sessions.length === 0 && (
            <div className="empty-result">No chats yet. Ask something to start one.</div>
          )}
        </div>

        <div className="col-foot">
          <span className="powered-by">
            Powered by
            <img
              src="/stuhi-logo.png"
              alt="Stuhi"
              className="stuhi-logo"
            />
          </span>
        </div>
      </div>
    </aside>
  );
}

function DealGroup({
  label,
  color,
  deals,
  activeDealId,
  onPick,
}: {
  label: string;
  color: string;
  deals: Deal[];
  activeDealId?: string;
  onPick: (d: Deal) => void;
}) {
  const [open, setOpen] = useState(true);
  return (
    <div>
      <button
        type="button"
        className="chats-h"
        onClick={() => setOpen((v) => !v)}
        aria-expanded={open}
      >
        <span className="chats-h-label">
          <span className="caret">{open ? "▼" : "▶"}</span>
          <span className="cat" style={{ "--cat-color": color } as CSSVarStyle}>
            {label}
          </span>
        </span>
        <span className="tnum">{deals.length}</span>
      </button>
      {open &&
        deals.map((d) => (
          <DealItem
            key={d.id}
            d={d}
            active={d.id === activeDealId}
            onClick={() => onPick(d)}
          />
        ))}
    </div>
  );
}

const CORP_SUFFIX = new Set([
  "inc",
  "co",
  "llc",
  "ltd",
  "corp",
  "corporation",
  "company",
  "holdings",
  "group",
]);

function nameTokens(s: string): string[] {
  return s
    .toLowerCase()
    .replace(/[.,]/g, "")
    .split(/\s+/)
    .filter((t) => t && !CORP_SUFFIX.has(t));
}

/** True when the company line is just a longer/decorated version of the
 *  codename (e.g. "Vanguard Auto" vs "Vanguard Auto Parts") — in which case
 *  the second line adds no information and we suppress it. */
function isNameDuplicate(codename: string, company: string): boolean {
  const a = nameTokens(codename);
  const b = nameTokens(company);
  if (a.length === 0 || b.length === 0) return false;
  const [small, big] = a.length <= b.length ? [a, b] : [b, a];
  return small.every((t) => big.includes(t));
}

function DealItem({
  d,
  active,
  onClick,
}: {
  d: Deal;
  active: boolean;
  onClick: () => void;
}) {
  return (
    <button
      className={`deal-item ${active ? "active" : ""}`}
      onClick={onClick}
      title={d.company}
    >
      <div className="t">{d.codename}</div>
      {d.company && !isNameDuplicate(d.codename, d.company) && (
        <div className="m">
          <span className="co">{d.company}</span>
        </div>
      )}
    </button>
  );
}

function SessionGroup({
  label,
  color,
  sessions,
  currentId,
  onPick,
}: {
  label: string;
  color: string;
  sessions: Session[];
  currentId: string | null;
  onPick: (id: string) => void;
}) {
  const [open, setOpen] = useState(true);
  return (
    <div>
      <button
        type="button"
        className="chats-h"
        onClick={() => setOpen((v) => !v)}
        aria-expanded={open}
      >
        <span className="chats-h-label">
          <span className="caret">{open ? "▼" : "▶"}</span>
          <span className="cat" style={{ "--cat-color": color } as CSSVarStyle}>
            {label}
          </span>
        </span>
        <span className="tnum">{sessions.length}</span>
      </button>
      {open &&
        sessions.map((s) => (
          <ChatItem
            key={s.id}
            s={s}
            active={s.id === currentId}
            onClick={() => onPick(s.id)}
          />
        ))}
    </div>
  );
}

function ChatItem({
  s,
  active,
  onClick,
}: {
  s: Session;
  active: boolean;
  onClick: () => void;
}) {
  const title = useMemo(() => {
    if (!s.scope?.codename) return s.title;
    const re = new RegExp(`(${s.scope.codename})`, "i");
    const parts = s.title.split(re);
    return parts.map((p, i) =>
      re.test(p) ? <em key={i}>{p}</em> : <span key={i}>{p}</span>,
    );
  }, [s.title, s.scope?.codename]);

  return (
    <button
      className={`chat-item ${active ? "active" : ""}`}
      onClick={onClick}
    >
      <div className="t">{title}</div>
      <div className="m">
        <span className="tnum">{relativeTime(s.updatedAt)}</span>
        <span>·</span>
        <span className="tnum">{s.turns} turns</span>
      </div>
    </button>
  );
}
