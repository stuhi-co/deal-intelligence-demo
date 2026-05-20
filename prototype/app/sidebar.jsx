/* ─────────────────────────────────────────────────────────────────────
 *  Sidebar — icon rail (status dots) + chats column
 * ───────────────────────────────────────────────────────────────────── */

const { useMemo, useState: useStateS } = React;

function Sidebar({
  sessions,
  currentSessionId,
  scope,
  onNewChat,
  onPickSession,
  onPickStatus,
  onScopeDeal,
  onOpenPalette,
  onToggleTheme,
  theme,
}) {
  const [tab, setTab] = useStateS("deals");          // "deals" | "chats"
  const [query, setQuery] = useStateS("");

  const groups = ["Active", "Portfolio", "Exited", "Dead"];

  // sort sessions by recency
  const sorted = useMemo(
    () => [...sessions].sort((a, b) => b.updatedAt - a.updatedAt),
    [sessions]
  );

  // ── deals grouped by status, optionally filtered by query ──
  const dealsByGroup = useMemo(() => {
    const q = query.trim().toLowerCase();
    const out = { Active: [], Portfolio: [], Exited: [], Dead: [] };
    for (const d of window.DEALS) {
      if (q) {
        const hay = [d.codename, d.company, window.SECTOR_SHORT[d.sector] || d.sector]
          .join(" ").toLowerCase();
        if (!hay.includes(q)) continue;
      }
      (out[d.status] ?? []).push(d);
    }
    return out;
  }, [query]);

  // ── sessions grouped by deal status, filtered by query ──
  const grouped = useMemo(() => {
    const q = query.trim().toLowerCase();
    const out = { Active: [], Portfolio: [], Exited: [], Dead: [], Other: [] };
    for (const s of sorted) {
      if (q && !s.title.toLowerCase().includes(q)) continue;
      const k = s.scope?.status || s.scope?.statusGroup || "Other";
      (out[k] ?? out.Other).push(s);
    }
    return out;
  }, [sorted, query]);

  const totalDeals = window.DEALS.length;
  const totalChats = sessions.length;

  return (
    <aside className="side">
      {/* Icon rail */}
      <div className="rail">
        <div className="brand" title="Atlas Crossing">A</div>
        <button
          className="rail-btn"
          onClick={onNewChat}
          aria-label="New chat"
        >
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
          onClick={onToggleTheme}
          aria-label="Toggle theme"
        >
          {theme === "dark" ? <Icons.Sun size={16} /> : <Icons.Moon size={16} />}
          <span className="tip">{theme === "dark" ? "Light mode" : "Dark mode"}</span>
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
            aria-selected={tab === "deals"}
            className={tab === "deals" ? "active" : ""}
            onClick={() => setTab("deals")}
          >
            Deals <span className="tnum count">{totalDeals}</span>
          </button>
          <button
            role="tab"
            aria-selected={tab === "chats"}
            className={tab === "chats" ? "active" : ""}
            onClick={() => setTab("chats")}
          >
            Chats <span className="tnum count">{totalChats}</span>
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
            groups.map((g) =>
              dealsByGroup[g].length ? (
                <DealGroup
                  key={g}
                  label={g}
                  color={window.STATUS_COLOR[g]}
                  deals={dealsByGroup[g]}
                  activeDealId={scope?.dealId}
                  onPick={onScopeDeal}
                />
              ) : null
            )
          ) : (
            <>
              {groups.map((g) =>
                grouped[g].length ? (
                  <SessionGroup
                    key={g}
                    label={g}
                    color={window.STATUS_COLOR[g]}
                    sessions={grouped[g]}
                    currentId={currentSessionId}
                    onPick={onPickSession}
                  />
                ) : null
              )}
              {grouped.Other.length ? (
                <SessionGroup
                  key="other"
                  label="Unscoped"
                  color="var(--fg-faint)"
                  sessions={grouped.Other}
                  currentId={currentSessionId}
                  onPick={onPickSession}
                />
              ) : null}
            </>
          )}

          {/* Empty search result */}
          {tab === "deals" && Object.values(dealsByGroup).every((a) => !a.length) && (
            <div className="empty-result">No deals match “{query}”.</div>
          )}
          {tab === "chats" && Object.values(grouped).every((a) => !a.length) && (
            <div className="empty-result">No chats match “{query}”.</div>
          )}
        </div>

        <div className="col-foot">
          <span>v0.5 — demo</span>
          <span>
            <span className="stuhi">Stuhi</span>
          </span>
        </div>
      </div>
    </aside>
  );
}

function DealGroup({ label, color, deals, activeDealId, onPick }) {
  return (
    <div>
      <div className="chats-h">
        <span className="cat" style={{ "--cat-color": color }}>
          {label}
        </span>
        <span className="tnum">{deals.length}</span>
      </div>
      {deals.map((d) => (
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

function DealItem({ d, active, onClick }) {
  return (
    <button
      className={`deal-item ${active ? "active" : ""}`}
      onClick={onClick}
      title={d.company}
    >
      <div className="t">
        <em>{d.codename}</em>
      </div>
      <div className="m">
        <span className="co">{d.company}</span>
      </div>
    </button>
  );
}

function SessionGroup({ label, color, sessions, currentId, onPick }) {
  return (
    <div>
      <div className="chats-h">
        <span className="cat" style={{ "--cat-color": color }}>
          {label}
        </span>
        <span className="tnum">{sessions.length}</span>
      </div>
      {sessions.map((s) => (
        <ChatItem
          key={s.id}
          s={s}
          color={color}
          active={s.id === currentId}
          onClick={() => onPick(s.id)}
        />
      ))}
    </div>
  );
}

function ChatItem({ s, color, active, onClick }) {
  // Italicise codename when it appears in the title
  const title = useMemo(() => {
    if (!s.scope?.codename) return s.title;
    const re = new RegExp(`(${s.scope.codename})`, "i");
    const parts = s.title.split(re);
    return parts.map((p, i) =>
      re.test(p) ? <em key={i}>{p}</em> : <span key={i}>{p}</span>
    );
  }, [s.title, s.scope?.codename]);

  return (
    <button
      className={`chat-item ${active ? "active" : ""}`}
      onClick={onClick}
    >
      <div className="t">{title}</div>
      <div className="m">
        <span className="tnum">{window.relativeTime(s.updatedAt)}</span>
        <span>·</span>
        <span className="tnum">{s.turns} turns</span>
      </div>
    </button>
  );
}

window.Sidebar = Sidebar;
