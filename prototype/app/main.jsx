/* ─────────────────────────────────────────────────────────────────────
 *  Main app — state, routing between sessions, ⌘K, theme
 * ───────────────────────────────────────────────────────────────────── */

const { useState: useStateA, useEffect: useEffectA, useCallback: useCallbackA, useRef: useRefA } = React;

function App() {
  // ── theme ──
  const [theme, setTheme] = useStateA(() => {
    return localStorage.getItem("ac-theme") || "light";
  });
  useEffectA(() => {
    document.documentElement.classList.toggle("dark", theme === "dark");
    localStorage.setItem("ac-theme", theme);
  }, [theme]);

  // ── sessions / current ──
  const [sessions, setSessions]   = useStateA(() => window.SESSIONS);
  const [currentId, setCurrentId] = useStateA(null);
  const [scope,     setScope]     = useStateA(null);
  const [messages,  setMessages]  = useStateA([]);
  const [isLoading, setIsLoading] = useStateA(false);
  const [paletteOpen, setPaletteOpen] = useStateA(false);

  // ── ⌘K ──
  useEffectA(() => {
    const onKey = (e) => {
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
  }, []);

  // ── helpers ──
  const newChat = useCallbackA((prefill) => {
    setCurrentId(null);
    setMessages([]);
    setIsLoading(false);
    if (typeof prefill === "string" && prefill.trim()) {
      // Defer so the empty state never flashes
      setTimeout(() => sendMessage(prefill), 30);
    }
  }, []);

  const switchSession = useCallbackA((id) => {
    const s = sessions.find((s) => s.id === id);
    if (!s) return;
    setCurrentId(id);
    setScope(s.scope || null);
    setMessages(s.messages || []);
    setIsLoading(false);
  }, [sessions]);

  const pickStatus = useCallbackA((g) => {
    setScope({ statusGroup: g });
    setCurrentId(null);
    setMessages([]);
  }, []);

  const scopeDeal = useCallbackA((deal) => {
    setScope({
      dealId: deal.id,
      codename: deal.codename,
      company: deal.company,
      status: deal.status,
    });
    setCurrentId(null);
    setMessages([]);
  }, []);

  const clearScope = useCallbackA(() => setScope(null), []);

  const onPickThread = useCallbackA((thread) => {
    const next = thread.scope || null;
    setScope(next);
    setCurrentId(null);
    setMessages([]);
    // Pass the scope explicitly so the new session is tagged correctly
    setTimeout(() => sendMessage(thread.canonical, next), 30);
  }, [sendMessage]);

  // ── send a message ──
  // sendMessage accepts an optional scopeOverride so callers (e.g. onPickThread)
  // can guarantee the new scope is captured even though setScope hasn't flushed yet.
  const sendMessage = useCallbackA((text, scopeOverride) => {
    const useScope = scopeOverride !== undefined ? scopeOverride : scope;
    const userMsg = {
      id: "u_" + Date.now(),
      role: "user",
      content: text,
    };
    const loadingMsg = {
      id: "l_" + Date.now(),
      role: "assistant",
      loading: true,
    };

    setMessages((m) => [...m, userMsg, loadingMsg]);
    setIsLoading(true);

    const a = window.findAnswer(text);
    // Simulate thinking + tool-call delay
    const delay = 1100 + Math.random() * 500;

    setTimeout(() => {
      const asstMsg = {
        id: "a_" + Date.now(),
        role: "assistant",
        content: a.text,
        citations: a.citations,
        provenance: {
          verdict: a.provenance?.violations ? "fail" : "pass",
          time: a.provenance.time,
          violations: a.provenance.violations || 0,
        },
      };
      setMessages((m) => {
        const next = [...m];
        if (next.length === 0) return [userMsg, asstMsg];
        next[next.length - 1] = asstMsg;
        return next;
      });
      setIsLoading(false);

      // persist into sessions: create or update
      setSessions((all) => {
        if (currentId && all.some((s) => s.id === currentId)) {
          return all.map((s) =>
            s.id === currentId
              ? { ...s, updatedAt: Date.now(), turns: (s.turns || 0) + 1 }
              : s
          );
        }
        const title = text.length > 70 ? text.slice(0, 70) + "…" : text;
        const newId = "s_" + Date.now();
        const newSession = {
          id: newId,
          title,
          scope: useScope || null,
          updatedAt: Date.now(),
          turns: 1,
          messages: [userMsg, asstMsg],
        };
        // Defer setCurrentId out of the updater to avoid React warnings
        queueMicrotask(() => setCurrentId(newId));
        return [newSession, ...all];
      });
    }, delay);
  }, [scope, currentId]);

  // ── render ──
  return (
    <div className="app">
      <window.Sidebar
        sessions={sessions}
        currentSessionId={currentId}
        scope={scope}
        onNewChat={newChat}
        onPickSession={switchSession}
        onPickStatus={pickStatus}
        onScopeDeal={scopeDeal}
        onOpenPalette={() => setPaletteOpen(true)}
        onToggleTheme={() => setTheme((t) => (t === "dark" ? "light" : "dark"))}
        theme={theme}
      />
      <main style={{ minWidth: 0 }}>
        <window.ChatPanel
          scope={scope}
          messages={messages}
          isLoading={isLoading}
          onSend={sendMessage}
          onClearScope={clearScope}
          onPickThread={onPickThread}
        />
      </main>

      <window.Palette
        open={paletteOpen}
        onClose={() => setPaletteOpen(false)}
        sessions={sessions}
        onScopeDeal={scopeDeal}
        onScopeStatus={pickStatus}
        onPickSession={switchSession}
        onNewChat={newChat}
      />
    </div>
  );
}

window.App = App;
ReactDOM.createRoot(document.getElementById("root")).render(<App />);
