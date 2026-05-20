"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { STATUS_COLOR, STATUS_GROUPS } from "@/lib/fixtures";
import { relativeTime } from "@/lib/utils";
import type { Deal, Session, StatusGroup } from "@/lib/types";

type Item =
  | {
      kind: "deal";
      id: string;
      primary: React.ReactNode;
      meta: string;
      dotColor: string;
      payload: Deal;
    }
  | {
      kind: "chat";
      id: string;
      primary: React.ReactNode;
      meta: string;
      dotColor: string;
      payload: Session;
    }
  | {
      kind: "group";
      id: string;
      primary: React.ReactNode;
      meta: string;
      dotColor: string;
      payload: StatusGroup;
    }
  | {
      kind: "new";
      id: string;
      primary: React.ReactNode;
      meta: string;
      dotColor: string;
      payload: string;
    };

type Section = { section: string; items: Item[] };

type Props = {
  open: boolean;
  onClose: () => void;
  deals: Deal[];
  sessions: Session[];
  onScopeDeal: (d: Deal) => void;
  onScopeStatus: (g: StatusGroup) => void;
  onPickSession: (id: string) => void;
  onNewChat: (prefill?: string) => void;
};

export function CommandPalette({
  open,
  onClose,
  deals,
  sessions,
  onScopeDeal,
  onScopeStatus,
  onPickSession,
  onNewChat,
}: Props) {
  const [q, setQ] = useState("");
  const [sel, setSel] = useState(0);
  const inputRef = useRef<HTMLInputElement | null>(null);

  useEffect(() => {
    if (open) {
      setQ("");
      setSel(0);
      setTimeout(() => inputRef.current?.focus(), 30);
    }
  }, [open]);

  const items: Section[] = useMemo(() => {
    const Q = q.toLowerCase().trim();
    const matches = (s: string) => !Q || s.toLowerCase().includes(Q);

    const dealItems: Item[] = deals
      .filter(
        (d) =>
          matches(d.codename) ||
          matches(d.company) ||
          matches(d.sector) ||
          matches(String(d.year)) ||
          matches(d.status),
      )
      .slice(0, 7)
      .map((d) => ({
        kind: "deal",
        id: d.id,
        primary: (
          <>
            <em>{d.codename}</em>{" "}
            <span className="mute">— {d.company}</span>
          </>
        ),
        meta: `${d.status.toLowerCase()} · ${d.year}`,
        dotColor: STATUS_COLOR[d.status],
        payload: d,
      }));

    const chats: Item[] = sessions
      .filter((s) => matches(s.title))
      .slice(0, 5)
      .map((s) => ({
        kind: "chat",
        id: s.id,
        primary: <span>{s.title}</span>,
        meta: relativeTime(s.updatedAt),
        dotColor:
          (s.scope?.status && STATUS_COLOR[s.scope.status]) ?? "var(--fg-faint)",
        payload: s,
      }));

    const groups: Item[] = STATUS_GROUPS.filter((g) => matches(g)).map((g) => ({
      kind: "group",
      id: "g-" + g,
      primary: (
        <span>
          Browse <em>{g}</em>
        </span>
      ),
      meta: `${deals.filter((d) => d.status === g).length} deals`,
      dotColor: STATUS_COLOR[g],
      payload: g,
    }));

    const list: Section[] = [];
    if (dealItems.length) list.push({ section: "Deals", items: dealItems });
    if (chats.length) list.push({ section: "Recent chats", items: chats });
    if (groups.length && !Q) list.push({ section: "Status groups", items: groups });

    if (!list.length) {
      list.push({
        section: "Actions",
        items: [
          {
            kind: "new",
            id: "new-from-q",
            primary: (
              <span>
                Ask a new question <span className="mute">— &quot;{q}&quot;</span>
              </span>
            ),
            meta: "⌘↵",
            dotColor: "var(--accent)",
            payload: q,
          },
        ],
      });
    }
    return list;
  }, [q, sessions, deals]);

  const flat: Item[] = useMemo(() => items.flatMap((s) => s.items), [items]);
  useEffect(() => {
    if (sel >= flat.length) setSel(0);
  }, [flat.length, sel]);

  function commit(item: Item | undefined) {
    if (!item) return;
    if (item.kind === "deal") onScopeDeal(item.payload);
    else if (item.kind === "chat") onPickSession(item.payload.id);
    else if (item.kind === "group") onScopeStatus(item.payload);
    else if (item.kind === "new") onNewChat(item.payload);
    onClose();
  }

  function onKey(e: React.KeyboardEvent<HTMLDivElement>) {
    if (e.key === "Escape") {
      e.preventDefault();
      onClose();
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      setSel((s) => Math.min(flat.length - 1, s + 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setSel((s) => Math.max(0, s - 1));
    } else if (e.key === "Enter") {
      e.preventDefault();
      commit(flat[sel]);
    }
  }

  if (!open) return null;

  let runningIndex = -1;

  return (
    <div
      className="scrim"
      onMouseDown={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
    >
      <div className="cmd" onKeyDown={onKey}>
        <div className="cmd-input">
          <span className="pfx">⌘ K</span>
          <input
            ref={inputRef}
            value={q}
            onChange={(e) => {
              setQ(e.target.value);
              setSel(0);
            }}
            placeholder="Search a deal, codename, or chat…"
          />
        </div>
        <div className="cmd-list">
          {items.map((sec) => (
            <div key={sec.section}>
              <div className="cmd-sec">
                <span>{sec.section}</span>
                <span className="tnum">{sec.items.length}</span>
              </div>
              {sec.items.map((it) => {
                runningIndex += 1;
                const isSel = runningIndex === sel;
                const myIdx = runningIndex;
                return (
                  <div
                    key={it.id}
                    className={`cmd-item ${isSel ? "sel" : ""}`}
                    onMouseMove={() => setSel(myIdx)}
                    onMouseDown={(e) => {
                      e.preventDefault();
                      commit(it);
                    }}
                  >
                    <span
                      className="dot"
                      style={{ background: it.dotColor }}
                    />
                    <span className="label">{it.primary}</span>
                    <span className="meta">{it.meta}</span>
                  </div>
                );
              })}
            </div>
          ))}
        </div>
        <div className="cmd-foot">
          <span>
            <kbd>↵</kbd>scope
          </span>
          <span>
            <kbd>⌘</kbd>
            <kbd>↵</kbd>new chat scoped
          </span>
          <span>
            <kbd>esc</kbd>close
          </span>
        </div>
      </div>
    </div>
  );
}
