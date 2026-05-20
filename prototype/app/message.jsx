/* ─────────────────────────────────────────────────────────────────────
 *  MessageBubble — transcript-style, inline citations, footnote rail,
 *  mono provenance byline.
 *
 *  Renders a tiny subset of markdown: paragraphs, headings, lists,
 *  tables, bold, italic, and <sup data-cite="N"></sup> citation marks.
 * ───────────────────────────────────────────────────────────────────── */

const { useState: useStateM, useMemo: useMemoM } = React;

// ─── inline renderer ───────────────────────────────────────────────────
function renderInline(text, onCiteHover) {
  // Split out <sup data-cite="N"></sup> tokens, **bold**, *italic*
  // Use a single regex with alternation, then walk matches.
  const re = /<sup data-cite="(\d+)"><\/sup>|\*\*([^*]+)\*\*|\*([^*]+)\*|`([^`]+)`/g;
  const out = [];
  let last = 0;
  let m;
  let key = 0;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(text.slice(last, m.index));
    if (m[1]) {
      const n = Number(m[1]);
      out.push(
        <span
          key={`c${key++}`}
          className="cite"
          data-n={n}
          onMouseEnter={() => onCiteHover?.(n)}
          onMouseLeave={() => onCiteHover?.(null)}
          onClick={(e) => {
            // scroll to footnote
            const root = e.currentTarget.closest(".msg-asst");
            const fn = root?.querySelector(`[data-fn="${n}"]`);
            fn?.scrollIntoView({ behavior: "smooth", block: "center" });
            fn?.animate(
              [{ background: "var(--mint)" }, { background: "transparent" }],
              { duration: 900 }
            );
          }}
        >
          {n}
        </span>
      );
    } else if (m[2]) {
      out.push(<strong key={`b${key++}`}>{m[2]}</strong>);
    } else if (m[3]) {
      out.push(<em key={`i${key++}`}>{m[3]}</em>);
    } else if (m[4]) {
      out.push(<code key={`k${key++}`} className="mono">{m[4]}</code>);
    }
    last = re.lastIndex;
  }
  if (last < text.length) out.push(text.slice(last));
  return out;
}

// ─── block renderer ────────────────────────────────────────────────────
function renderBlocks(md, onCiteHover) {
  // Normalise line endings, split into blocks by blank line
  const blocks = md.replace(/\r\n/g, "\n").split(/\n\s*\n/);
  return blocks.map((blk, i) => {
    const lines = blk.split("\n").filter((l) => l.length);

    // Heading
    if (/^#{1,4}\s/.test(lines[0])) {
      const m = lines[0].match(/^(#{1,4})\s+(.+)$/);
      const lvl = Math.min(3, m[1].length + 1);
      const Tag = `h${lvl}`;
      return <Tag key={i}>{renderInline(m[2], onCiteHover)}</Tag>;
    }

    // Table: first line starts with | and second line has --- separators
    if (lines[0]?.startsWith("|") && lines[1] && /\|?\s*:?-+:?/.test(lines[1])) {
      const header = lines[0].split("|").slice(1, -1).map((s) => s.trim());
      const aligns = lines[1].split("|").slice(1, -1).map((c) => {
        const t = c.trim();
        if (t.startsWith(":") && t.endsWith(":")) return "center";
        if (t.endsWith(":"))                       return "right";
        return "left";
      });
      const rows = lines.slice(2).map((r) =>
        r.split("|").slice(1, -1).map((s) => s.trim())
      );
      return (
        <table key={i}>
          <thead>
            <tr>{header.map((h, j) => (
              <th key={j} style={{ textAlign: aligns[j] || "left" }}>{h}</th>
            ))}</tr>
          </thead>
          <tbody>
            {rows.map((row, ri) => (
              <tr key={ri}>
                {row.map((cell, ci) => {
                  const numeric = /^[\-\$]?[\d.,]+[\d%×x]*$|^\([\d.,]+\)$/.test(cell.trim());
                  return (
                    <td
                      key={ci}
                      className={numeric ? "num" : ""}
                      style={{ textAlign: aligns[ci] || (numeric ? "right" : "left") }}
                    >
                      {renderInline(cell, onCiteHover)}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      );
    }

    // Unordered list (lines starting with -)
    if (lines.every((l) => /^-\s/.test(l))) {
      return (
        <ul key={i}>
          {lines.map((l, j) => (
            <li key={j}>{renderInline(l.replace(/^-\s+/, ""), onCiteHover)}</li>
          ))}
        </ul>
      );
    }

    // Ordered list
    if (lines.every((l) => /^\d+\.\s/.test(l))) {
      return (
        <ol key={i}>
          {lines.map((l, j) => (
            <li key={j}>{renderInline(l.replace(/^\d+\.\s+/, ""), onCiteHover)}</li>
          ))}
        </ol>
      );
    }

    // Paragraph
    return <p key={i}>{renderInline(lines.join(" "), onCiteHover)}</p>;
  });
}

// ─── footnotes ─────────────────────────────────────────────────────────
function Footnotes({ citations, highlight }) {
  const typeLabel = { doc: "doc", deal: "deal", macro: "macro", criteria: "criteria" };
  return (
    <ol className="fns" style={{ listStyle: "none", margin: 0, padding: 0 }}>
      {citations.map((c) => (
        <li
          key={c.n}
          data-fn={c.n}
          className="fn"
          style={highlight === c.n ? { background: "color-mix(in oklch, var(--mint) 30%, transparent)" } : null}
        >
          <span className="n">[{c.n}]</span>
          <span className="src">
            <span className="title">{c.title}</span>
            {c.excerpt && <span className="ex">{c.excerpt}</span>}
          </span>
          <span className="meta">
            {typeLabel[c.type] || c.type} · {c.ref}
            <br />
            {c.date}
          </span>
        </li>
      ))}
    </ol>
  );
}

// ─── full message ──────────────────────────────────────────────────────
function MessageBubble({ message }) {
  const [hover, setHover] = useStateM(null);
  const [reviewOpen, setReviewOpen] = useStateM(false);

  if (message.role === "user") {
    // Italicise codenames inline (anything in *…* in the user's text)
    return (
      <div className="msg-user fade-in" data-role="user">
        <div className="who">You</div>
        <div className="what">{renderInline(message.content)}</div>
      </div>
    );
  }

  if (message.loading) {
    return (
      <div className="msg-asst fade-in">
        <div className="who">AC</div>
        <div className="body">
          <p className="muted serif italic" style={{ fontSize: 16 }}>
            Searching deal documents…
          </p>
          <div className="dots"><span /><span /><span /></div>
        </div>
      </div>
    );
  }

  const blocks = useMemoM(
    () => renderBlocks(message.content, setHover),
    [message.content]
  );

  const verdict = message.provenance?.verdict ?? "pass";
  const violations = message.provenance?.violations ?? 0;
  const time = message.provenance?.time ?? "—";
  const nCites = message.citations?.length ?? 0;

  return (
    <div className="msg-asst fade-in">
      <div className="who">AC</div>
      <div className="body">
        {blocks}

        {message.citations?.length > 0 && (
          <Footnotes citations={message.citations} highlight={hover} />
        )}

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
          <span className="tnum">{time}</span>
        </div>

        {verdict === "fail" && reviewOpen && (
          <div className="review-panel">
            <h5>Claims to verify</h5>
            <p style={{ margin: 0 }}>
              The judge model flagged {violations} claim{violations === 1 ? "" : "s"} where the
              draft text and the source excerpt diverge. Click each marker to inspect.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

window.MessageBubble = MessageBubble;
