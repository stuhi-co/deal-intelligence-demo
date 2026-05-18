/* ─────────────────────────────────────────────────────────────────────
 *  ChatPanel — editorial header, empty state, message stream, input dock
 * ───────────────────────────────────────────────────────────────────── */

const { useEffect: useEffectC, useRef: useRefC, useState: useStateC } = React;

function ChatPanel({
  scope,
  messages,
  onSend,
  onClearScope,
  onPickThread,
  isLoading,
}) {
  const [input, setInput] = useStateC("");
  const streamRef = useRefC(null);
  const taRef = useRefC(null);

  useEffectC(() => {
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

  function handleKey(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  }

  const deal = scope?.codename
    ? window.DEALS.find((d) => d.id === scope.dealId) || null
    : null;
  const isGroup = !scope?.codename && !!scope?.statusGroup;

  // Build placeholder based on scope
  const placeholder = scope?.codename
    ? `Ask anything about Project ${scope.codename}…`
    : scope?.statusGroup
    ? `Ask about ${scope.statusGroup.toLowerCase()} deals…`
    : "Ask about any deal, document, or market data…";

  return (
    <section className="chat" data-screen-label="Chat panel">
      {/* ── Header ────────────────────────────────────────────────── */}
      <header className="chat-head">
        <div>
          <h1>
            {scope?.codename ? (
              <>Project <em>{scope.codename}</em></>
            ) : isGroup ? (
              <>{scope.statusGroup} <em>deals</em></>
            ) : (
              <>Ask <em>the firm</em></>
            )}
          </h1>
        </div>

        <div className="right" />
      </header>

      {/* ── Stream ────────────────────────────────────────────────── */}
      <div className="stream-wrap" ref={streamRef}>
        {messages.length === 0 ? (
          <EmptyState onPick={onPickThread} scope={scope} />
        ) : (
          <div className="stream">
            {messages.map((m) => (
              <MessageBubble key={m.id} message={m} />
            ))}
          </div>
        )}
      </div>

      {/* ── Input dock ────────────────────────────────────────────── */}
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
              >
                <span>Send</span>
                <Icons.ArrowUp size={12} />
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

const kbdStyle = {
  fontFamily: "var(--mono)",
  fontSize: 10.5,
  padding: "1px 5px",
  border: "1px solid var(--border)",
  borderRadius: 3,
  background: "var(--bg-card)",
  color: "var(--fg-soft)",
  margin: "0 2px",
};

// ─── Empty state — quiet centered prompt + suggestion chips ───────────
function EmptyState({ onPick, scope }) {
  const suggestions = (window.FRONT_THREADS || []).slice(0, 4);
  return (
    <div className="empty">
      <h2 className="hed">
        What do you want to <em>know</em>?
      </h2>
      {suggestions.length > 0 && (
        <div className="suggestions">
          {suggestions.map((t) => (
            <button
              key={t.n}
              className="suggestion"
              onClick={() => onPick(t)}
            >
              {t.canonical}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

window.ChatPanel = ChatPanel;
