"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { Icons } from "./icons";
import { MessageBubble } from "./message-bubble";
import { FRONT_THREADS } from "@/lib/fixtures";
import type { ChatMessage, FrontThread, ScopeContext } from "@/lib/types";

type Props = {
  scope: ScopeContext | null;
  messages: ChatMessage[];
  isLoading: boolean;
  onSend: (text: string) => void;
  onClearScope: () => void;
  onPickThread: (t: FrontThread) => void;
};

export function ChatPanel({
  scope,
  messages,
  onSend,
  onPickThread,
  isLoading,
}: Props) {
  const [input, setInput] = useState("");
  const streamRef = useRef<HTMLDivElement | null>(null);
  const taRef = useRef<HTMLTextAreaElement | null>(null);

  useEffect(() => {
    if (streamRef.current) {
      streamRef.current.scrollTo({
        top: streamRef.current.scrollHeight,
        behavior: "smooth",
      });
    }
  }, [messages]);

  function handleSend() {
    const t = input.trim();
    if (!t || isLoading) return;
    setInput("");
    onSend(t);
    requestAnimationFrame(() => taRef.current?.focus());
  }

  function handleKey(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  }

  const isGroup = !scope?.codename && !!scope?.statusGroup;

  const placeholder = scope?.codename
    ? `Ask anything about Project ${scope.codename}…`
    : scope?.statusGroup
    ? `Ask about ${scope.statusGroup.toLowerCase()} deals…`
    : "Ask about any deal, document, or market data…";

  return (
    <section className="chat" data-screen-label="Chat panel">
      <header className="chat-head">
        <div>
          <h1>
            {scope?.codename ? (
              <em>{scope.codename}</em>
            ) : isGroup ? (
              <>
                {scope!.statusGroup} <em>deals</em>
              </>
            ) : (
              <>
                Ask <em>the firm</em>
              </>
            )}
          </h1>
        </div>
        <div className="right" />
      </header>

      <div className="stream-wrap" ref={streamRef}>
        {messages.length === 0 ? (
          <EmptyState onPick={onPickThread} />
        ) : (
          <div className="stream">
            {messages.map((m) => (
              <MessageBubble key={m.id} message={m} />
            ))}
          </div>
        )}
      </div>

      <div className="dock">
        <div className="wrap">
          <div className="card">
            <textarea
              ref={taRef}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKey}
              placeholder={placeholder}
              rows={2}
              disabled={isLoading}
            />
            <div className="bar">
              <span className="kbd-tip" />
              <button
                className="send"
                onClick={handleSend}
                disabled={!input.trim() || isLoading}
                aria-label="Send"
                title="Send (↵)"
              >
                <Icons.ArrowUp size={14} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function EmptyState({ onPick }: { onPick: (t: FrontThread) => void }) {
  // Random sample chosen on mount (client-side only — avoids hydration mismatch
  // since Math.random would differ between server and client). A new chat
  // remounts EmptyState, so each visit shows a different rotation.
  const [suggestions, setSuggestions] = useState<FrontThread[]>([]);
  useEffect(() => {
    const shuffled = [...FRONT_THREADS].sort(() => Math.random() - 0.5);
    setSuggestions(shuffled.slice(0, Math.min(4, FRONT_THREADS.length)));
  }, []);

  return (
    <div className="empty">
      <h2 className="hed">
        What do you want to <em>know</em>?
      </h2>
      {suggestions.length > 0 && (
        <div className="suggestions">
          {suggestions.map((t) => (
            <button key={t.n} className="suggestion" onClick={() => onPick(t)}>
              {t.canonical}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
