"use client";

import { useMemo, useState } from "react";
import { renderBlocks, renderInline } from "@/lib/markdown";
import type { ActivityItem, ChatMessage, Citation } from "@/lib/types";

function typeLabel(t: string): string {
  const upperAcronyms = new Set(["ic", "dd", "cim", "kpi", "qofe", "loi", "ioi"]);
  return t
    .split(/[_\s]+/)
    .filter(Boolean)
    .map((w, i) =>
      upperAcronyms.has(w.toLowerCase())
        ? w.toUpperCase()
        : i === 0
        ? w.charAt(0).toUpperCase() + w.slice(1)
        : w,
    )
    .join(" ");
}

function humanizeToolName(name: string): string {
  return name
    .split(/[_\s]+/)
    .filter(Boolean)
    .map((w, i) =>
      i === 0 ? w.charAt(0).toUpperCase() + w.slice(1) : w,
    )
    .join(" ");
}

function inputSummary(input: Record<string, unknown>): string {
  const entries = Object.entries(input ?? {}).filter(
    ([, v]) => v != null && v !== "",
  );
  if (entries.length === 0) return "";
  return entries
    .slice(0, 2)
    .map(([k, v]) => {
      const sv = typeof v === "string" ? v : JSON.stringify(v);
      const truncated = sv.length > 40 ? sv.slice(0, 40) + "…" : sv;
      return `${k}: ${truncated}`;
    })
    .join(" · ");
}

function Footnotes({
  citations,
  highlight,
}: {
  citations: Citation[];
  highlight: number | null;
}) {
  return (
    <ol className="fns" style={{ listStyle: "none", margin: 0, padding: 0 }}>
      {citations.map((c) => (
        <li
          key={c.n}
          data-fn={c.n}
          className="fn"
          style={
            highlight === c.n
              ? { background: "color-mix(in oklch, var(--mint) 30%, transparent)" }
              : undefined
          }
        >
          <span className="n">[{c.n}]</span>
          <span className="src">
            {c.url ? (
              <a
                className="title src-link"
                href={c.url}
                target="_blank"
                rel="noopener noreferrer"
                title="Open in Google Drive"
              >
                {c.title}
                <span className="src-ext" aria-hidden>
                  {" "}
                  ↗
                </span>
              </a>
            ) : (
              <span className="title">{c.title}</span>
            )}
            {c.excerpt && <span className="ex">{c.excerpt}</span>}
          </span>
          <span className="meta">
            {typeLabel(c.type)} · {c.ref}
            <br />
            {c.date}
          </span>
        </li>
      ))}
    </ol>
  );
}

function ActivityPanel({
  activity,
  isStreaming,
}: {
  activity: ActivityItem[];
  isStreaming: boolean;
}) {
  const [open, setOpen] = useState(true);
  // Auto-collapse once streaming finishes, but only on first transition.
  const [autoCollapsed, setAutoCollapsed] = useState(false);
  if (!isStreaming && !autoCollapsed) {
    setAutoCollapsed(true);
    setOpen(false);
  }

  if (activity.length === 0 && !isStreaming) return null;

  const totalMs = activity.reduce((a, it) => a + (it.durationMs ?? 0), 0);
  const done = activity.filter((a) => a.status !== "pending").length;
  const summary = isStreaming
    ? `Working${activity.length ? ` · ${done}/${activity.length} steps` : "…"}`
    : `${activity.length} step${activity.length === 1 ? "" : "s"} · ${(totalMs / 1000).toFixed(1)}s`;

  return (
    <div className={`activity ${open ? "open" : "closed"}`}>
      <button
        className="activity-head"
        onClick={() => setOpen((v) => !v)}
        aria-expanded={open}
      >
        <span className="activity-caret">{open ? "▾" : "▸"}</span>
        <span className="activity-label">Activity</span>
        <span className="activity-sub">{summary}</span>
        {isStreaming && (
          <span className="loading-dots">
            <span />
            <span />
            <span />
          </span>
        )}
      </button>
      {open && (
        <ol className="activity-list">
          {activity.map((it) => (
            <li key={it.id} className={`activity-item activity-${it.status}`}>
              <span className="activity-status" aria-hidden>
                {it.status === "done" ? "✓" : it.status === "failed" ? "✕" : "○"}
              </span>
              <span className="activity-name">{humanizeToolName(it.name)}</span>
              <span className="activity-args">{inputSummary(it.input)}</span>
              {typeof it.durationMs === "number" && (
                <span className="activity-time">
                  {(it.durationMs / 1000).toFixed(1)}s
                </span>
              )}
            </li>
          ))}
        </ol>
      )}
    </div>
  );
}

export function MessageBubble({ message }: { message: ChatMessage }) {
  const [hover, setHover] = useState<number | null>(null);
  const [reviewOpen, setReviewOpen] = useState(false);

  const contentText =
    message.role === "assistant" && message.text ? message.text : "";
  const blocks = useMemo(
    () => (contentText ? renderBlocks(contentText, setHover) : null),
    [contentText],
  );

  if (message.role === "user") {
    return (
      <div className="msg-user fade-in" data-role="user">
        <div className="bubble">{renderInline(message.content)}</div>
      </div>
    );
  }

  // Assistant
  const isStreaming = message.status === "streaming";
  const isError = message.status === "error";
  const nCites = message.citations.length;
  const verdict = message.provenance?.verdict ?? "pass";
  const violations = message.provenance?.violations ?? 0;
  const time = message.provenance?.time;

  return (
    <div className="msg-asst fade-in">
      <div className="body">
        {(message.activity.length > 0 || isStreaming) && (
          <ActivityPanel activity={message.activity} isStreaming={isStreaming} />
        )}

        {!message.text && isStreaming && message.activity.length === 0 && (
          <p className="loading-line">
            Working
            <span className="loading-dots">
              <span />
              <span />
              <span />
            </span>
          </p>
        )}

        {blocks}

        {isError && message.error && !message.text && (
          <p style={{ color: "var(--judge-fail)" }}>{message.error}</p>
        )}

        {message.citations.length > 0 && (
          <Footnotes citations={message.citations} highlight={hover} />
        )}

        {(verdict !== "pass" || nCites > 0 || time) && (
          <div className="prov">
            {verdict === "pass" ? (
              <span className="check">
                {`Verified against ${nCites} ${nCites === 1 ? "source" : "sources"}`}
              </span>
            ) : (
              <span className="review" onClick={() => setReviewOpen((v) => !v)}>
                {`${violations} ${violations === 1 ? "claim needs" : "claims need"} review`}
              </span>
            )}
            {time && <span className="tnum">{time}</span>}
          </div>
        )}

        {verdict === "fail" && reviewOpen && (
          <div className="review-panel">
            <h5>Claims to verify</h5>
            <p style={{ margin: 0 }}>
              The judge model flagged {violations} claim
              {violations === 1 ? "" : "s"} where the draft text and the source
              excerpt diverge. Click each marker to inspect.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
