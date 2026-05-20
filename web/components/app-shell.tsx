"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { Sidebar } from "./sidebar";
import { ChatPanel } from "./chat-panel";
import { CommandPalette } from "./palette";
import { SESSIONS as SEED_SESSIONS } from "@/lib/fixtures";
import type {
  AssistantMessage,
  ChatMessage,
  Citation,
  Deal,
  FrontThread,
  Provenance,
  ScopeContext,
  Session,
  StatusGroup,
} from "@/lib/types";

const SESSIONS_KEY = "ac-sessions-v1";

function uid(prefix: string): string {
  return `${prefix}_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 8)}`;
}

type StreamEvent =
  | { type: "tool_use_start"; id: string; name: string; input: Record<string, unknown> }
  | { type: "tool_use_end"; id: string; ok: boolean; durationMs: number }
  | { type: "text"; text: string }
  | {
      type: "done";
      citations: Citation[];
      provenance: Provenance;
      elapsedSeconds: number;
      iterations: number;
    }
  | { type: "error"; message: string };

export function AppShell() {
  const [sessions, setSessions] = useState<Session[]>(SEED_SESSIONS);
  const [currentId, setCurrentId] = useState<string | null>(null);
  const [scope, setScope] = useState<ScopeContext | null>(null);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [deals, setDeals] = useState<Deal[]>([]);
  const [hydrated, setHydrated] = useState(false);

  // Hydrate sessions from localStorage on mount (client only — server has no
  // storage, so we render SEED_SESSIONS first then swap in the saved list).
  useEffect(() => {
    try {
      const raw = window.localStorage.getItem(SESSIONS_KEY);
      if (raw) {
        const parsed = JSON.parse(raw) as Session[];
        if (Array.isArray(parsed)) {
          // Dedupe by id in case older storage contains duplicates.
          const seen = new Set<string>();
          const unique = parsed.filter((s) => {
            if (!s?.id || seen.has(s.id)) return false;
            seen.add(s.id);
            return true;
          });
          setSessions(unique);
        }
      }
    } catch {
      /* ignore corrupt storage */
    }
    setHydrated(true);
  }, []);

  // Sync mirror of `messages` so async tasks (finally blocks, stream readers)
  // can read the latest list without nesting setState updaters.
  const messagesRef = useRef<ChatMessage[]>([]);

  // Persist sessions on every change once we've hydrated (avoid overwriting
  // the saved list with the seed before we've read it).
  useEffect(() => {
    if (!hydrated) return;
    try {
      window.localStorage.setItem(SESSIONS_KEY, JSON.stringify(sessions));
    } catch {
      /* quota exceeded or storage unavailable — silently drop */
    }
  }, [sessions, hydrated]);

  useEffect(() => {
    let cancelled = false;
    fetch("/api/deals")
      .then((r) => r.json())
      .then((j: { deals?: Deal[] }) => {
        if (!cancelled && Array.isArray(j.deals)) setDeals(j.deals);
      })
      .catch((e) => console.error("[deals] load failed", e));
    return () => {
      cancelled = true;
    };
  }, []);

  const sendMessage = useCallback(
    async (text: string, scopeOverride?: ScopeContext | null) => {
      const useScope = scopeOverride !== undefined ? scopeOverride : scope;
      const userMsg: ChatMessage = {
        id: uid("u"),
        role: "user",
        content: text,
      };
      const assistantId = uid("a");
      const seedAsst: AssistantMessage = {
        id: assistantId,
        role: "assistant",
        status: "streaming",
        text: "",
        activity: [],
        citations: [],
      };

      // Snapshot or create the session id eagerly so the finally-block save
      // is pure (no race between updater runs in StrictMode).
      const sessionId = currentId ?? uid("s");
      if (!currentId) {
        setCurrentId(sessionId);
      }

      // Snapshot prior history before appending the new turn — orchestrator
      // expects the conversation *up to but not including* this user message.
      const priorHistory = messagesRef.current;

      // Local accumulator updated SYNCHRONOUSLY on every patch — React's
      // setMessages updater is async, so reading messagesRef in the finally
      // block could otherwise see a state from before the final "done" patch
      // has flushed (chat would persist with status="streaming").
      let buf: ChatMessage[] = [...priorHistory, userMsg, seedAsst];
      messagesRef.current = buf;
      setMessages(buf);
      setIsLoading(true);

      const patchAsst = (patch: (a: AssistantMessage) => AssistantMessage) => {
        buf = buf.map((msg) =>
          msg.id === assistantId && msg.role === "assistant"
            ? patch(msg as AssistantMessage)
            : msg,
        );
        messagesRef.current = buf;
        setMessages(buf);
      };

      const t0 = Date.now();
      try {
        const r = await fetch("/api/chat", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({
            message: text,
            scope: useScope,
            history: priorHistory,
          }),
        });
        if (!r.ok || !r.body) {
          const err = await r.json().catch(() => ({ error: r.statusText }));
          throw new Error(err.error || `chat failed (${r.status})`);
        }

        const reader = r.body.getReader();
        const decoder = new TextDecoder();
        let buf = "";
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          buf += decoder.decode(value, { stream: true });
          let nl: number;
          while ((nl = buf.indexOf("\n")) >= 0) {
            const line = buf.slice(0, nl).trim();
            buf = buf.slice(nl + 1);
            if (!line) continue;
            let ev: StreamEvent;
            try {
              ev = JSON.parse(line) as StreamEvent;
            } catch {
              continue;
            }
            applyEvent(patchAsst, ev);
          }
        }
        // mark done if no explicit done event arrived
        patchAsst((a) =>
          a.status === "streaming" ? { ...a, status: "done" } : a,
        );
      } catch (e) {
        const elapsed = ((Date.now() - t0) / 1000).toFixed(1) + "s";
        patchAsst((a) => ({
          ...a,
          status: "error",
          error: (e as Error).message,
          text:
            a.text ||
            `**Error.** ${(e as Error).message}\n\nIs the FastAPI tool server running on :8000?`,
          provenance: { verdict: "fail", time: elapsed, violations: 1 },
        }));
      } finally {
        setIsLoading(false);
        // Defensive: any assistant message still marked streaming becomes
        // done so a refresh later doesn't render the bubble as interrupted.
        buf = buf.map((m) =>
          m.role === "assistant" && m.status === "streaming"
            ? { ...m, status: "done" as const }
            : m,
        );
        messagesRef.current = buf;
        setMessages(buf);

        const finalMessages = buf;
        // Pure updater: find-or-create by sessionId. Idempotent under React
        // StrictMode double-invoke — the second run finds the row we just
        // inserted and updates it in place.
        setSessions((all) => {
          const existing = all.find((s) => s.id === sessionId);
          if (existing) {
            return all.map((s) =>
              s.id === sessionId
                ? {
                    ...s,
                    updatedAt: Date.now(),
                    turns: (s.turns ?? 0) + 1,
                    messages: finalMessages,
                  }
                : s,
            );
          }
          const title = text.length > 70 ? text.slice(0, 70) + "…" : text;
          const newSession: Session = {
            id: sessionId,
            title,
            scope: useScope ?? null,
            updatedAt: Date.now(),
            turns: 1,
            messages: finalMessages,
          };
          return [newSession, ...all];
        });
      }
    },
    [scope, currentId],
  );

  const newChat = useCallback(
    (prefill?: string) => {
      setCurrentId(null);
      setMessages([]);
      messagesRef.current = [];
      setIsLoading(false);
      if (typeof prefill === "string" && prefill.trim()) {
        setTimeout(() => sendMessage(prefill), 30);
      }
    },
    [sendMessage],
  );

  const switchSession = useCallback(
    (id: string) => {
      const s = sessions.find((x) => x.id === id);
      if (!s) return;
      // If a stale assistant message was persisted while it was still
      // streaming (e.g. user reloaded mid-answer), reset it so the bubble
      // doesn't render as if it's still working.
      const cleaned = (s.messages ?? []).map((m) =>
        m.role === "assistant" && m.status === "streaming"
          ? { ...m, status: "error" as const, error: "Interrupted." }
          : m,
      );
      setCurrentId(id);
      setScope(s.scope ?? null);
      setMessages(cleaned);
      messagesRef.current = cleaned;
      setIsLoading(false);
    },
    [sessions],
  );

  const scopeDeal = useCallback((deal: Deal) => {
    setScope({
      dealId: deal.id,
      codename: deal.codename,
      company: deal.company,
      status: deal.status,
    });
    setCurrentId(null);
    setMessages([]);
  }, []);

  const scopeStatus = useCallback((g: StatusGroup) => {
    setScope({ statusGroup: g });
    setCurrentId(null);
    setMessages([]);
  }, []);

  const clearScope = useCallback(() => setScope(null), []);

  const onPickThread = useCallback(
    (thread: FrontThread) => {
      const next = thread.scope ?? null;
      setScope(next);
      setCurrentId(null);
      setMessages([]);
      setTimeout(() => sendMessage(thread.canonical, next), 30);
    },
    [sendMessage],
  );

  // ⌘K, ⌘N, Esc
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        setPaletteOpen((v) => !v);
      } else if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "n") {
        e.preventDefault();
        newChat();
      } else if (e.key === "Escape") {
        setPaletteOpen(false);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [newChat]);

  return (
    <div className="app">
      <Sidebar
        deals={deals}
        sessions={sessions}
        currentSessionId={currentId}
        scope={scope}
        onNewChat={() => newChat()}
        onPickSession={switchSession}
        onScopeDeal={scopeDeal}
        onOpenPalette={() => setPaletteOpen(true)}
      />
      <main style={{ minWidth: 0 }}>
        <ChatPanel
          key={currentId ?? "new"}
          scope={scope}
          messages={messages}
          isLoading={isLoading}
          onSend={sendMessage}
          onClearScope={clearScope}
          onPickThread={onPickThread}
        />
      </main>

      <CommandPalette
        open={paletteOpen}
        onClose={() => setPaletteOpen(false)}
        deals={deals}
        sessions={sessions}
        onScopeDeal={scopeDeal}
        onScopeStatus={scopeStatus}
        onPickSession={switchSession}
        onNewChat={newChat}
      />
    </div>
  );
}

function applyEvent(
  patch: (fn: (a: AssistantMessage) => AssistantMessage) => void,
  ev: StreamEvent,
): void {
  switch (ev.type) {
    case "tool_use_start":
      patch((a) => ({
        ...a,
        activity: [
          ...a.activity,
          { id: ev.id, name: ev.name, input: ev.input, status: "pending" },
        ],
      }));
      break;
    case "tool_use_end":
      patch((a) => ({
        ...a,
        activity: a.activity.map((it) =>
          it.id === ev.id
            ? { ...it, status: ev.ok ? "done" : "failed", durationMs: ev.durationMs }
            : it,
        ),
      }));
      break;
    case "text":
      patch((a) => ({ ...a, text: ev.text }));
      break;
    case "done":
      patch((a) => ({
        ...a,
        status: "done",
        citations: ev.citations,
        provenance: ev.provenance,
      }));
      break;
    case "error":
      patch((a) => ({
        ...a,
        status: "error",
        error: ev.message,
        provenance: {
          verdict: "fail",
          time: a.provenance?.time ?? "—",
          violations: 1,
        },
      }));
      break;
  }
}
