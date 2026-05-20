import { Fragment } from "react";

/** Inline tokens: <sup data-cite="N"></sup>, **bold**, *italic*, `code`. */
export function renderInline(
  text: string,
  onCiteHover?: (n: number | null) => void,
): React.ReactNode[] {
  const re =
    /<sup\s+data-cite=["'](\d+)["']\s*><\/sup>|\*\*([^*]+)\*\*|~~([^~]+)~~|\*([^*]+)\*|`([^`]+)`/g;
  const out: React.ReactNode[] = [];
  let last = 0;
  let m: RegExpExecArray | null;
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
            const root = (e.currentTarget as HTMLElement).closest(".msg-asst");
            const fn = root?.querySelector(`[data-fn="${n}"]`) as HTMLElement | null;
            fn?.scrollIntoView({ behavior: "smooth", block: "center" });
            fn?.animate(
              [{ background: "var(--mint)" }, { background: "transparent" }],
              { duration: 900 },
            );
          }}
        >
          {n}
        </span>,
      );
    } else if (m[2]) {
      out.push(<strong key={`b${key++}`}>{m[2]}</strong>);
    } else if (m[3]) {
      out.push(<s key={`s${key++}`}>{m[3]}</s>);
    } else if (m[4]) {
      out.push(<em key={`i${key++}`}>{m[4]}</em>);
    } else if (m[5]) {
      out.push(
        <code key={`k${key++}`} className="mono">
          {m[5]}
        </code>,
      );
    }
    last = re.lastIndex;
  }
  if (last < text.length) out.push(text.slice(last));
  return out;
}

/** Tiny markdown: paragraphs, headings, lists, tables. */
export function renderBlocks(
  md: string,
  onCiteHover?: (n: number | null) => void,
): React.ReactNode[] {
  const blocks = md.replace(/\r\n/g, "\n").split(/\n\s*\n/);
  return blocks.map((blk, i) => {
    const lines = blk.split("\n").filter((l) => l.length);

    // Horizontal rule: a line of three or more -, *, or _
    if (lines.length === 1 && /^\s*([-*_])\s*\1\s*\1[-*_\s]*$/.test(lines[0])) {
      return <hr key={i} />;
    }

    // Blockquote: every line starts with > (one or more levels)
    if (lines.every((l) => /^>\s?/.test(l))) {
      const inner = lines.map((l) => l.replace(/^>\s?/, "")).join(" ");
      return (
        <blockquote key={i}>{renderInline(inner, onCiteHover)}</blockquote>
      );
    }

    // Heading
    if (/^#{1,4}\s/.test(lines[0] ?? "")) {
      const m = lines[0].match(/^(#{1,4})\s+(.+)$/);
      if (m) {
        const lvl = Math.min(3, m[1].length + 1);
        if (lvl === 2) return <h2 key={i}>{renderInline(m[2], onCiteHover)}</h2>;
        return <h3 key={i}>{renderInline(m[2], onCiteHover)}</h3>;
      }
    }

    // Table
    if (lines[0]?.startsWith("|") && lines[1] && /\|?\s*:?-+:?/.test(lines[1])) {
      const header = lines[0].split("|").slice(1, -1).map((s) => s.trim());
      const aligns = lines[1]
        .split("|")
        .slice(1, -1)
        .map((c) => {
          const t = c.trim();
          if (t.startsWith(":") && t.endsWith(":")) return "center" as const;
          if (t.endsWith(":")) return "right" as const;
          return "left" as const;
        });
      const rows = lines
        .slice(2)
        .map((r) => r.split("|").slice(1, -1).map((s) => s.trim()));
      return (
        <table key={i}>
          <thead>
            <tr>
              {header.map((h, j) => (
                <th key={j} style={{ textAlign: aligns[j] ?? "left" }}>
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row, ri) => (
              <tr key={ri}>
                {row.map((cell, ci) => {
                  const numeric =
                    /^[\-\$]?[\d.,]+[\d%×x]*$|^\([\d.,]+\)$/.test(cell.trim());
                  return (
                    <td
                      key={ci}
                      className={numeric ? "num" : ""}
                      style={{ textAlign: aligns[ci] ?? (numeric ? "right" : "left") }}
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

    // Unordered list
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
    return (
      <p key={i}>
        <Fragment>{renderInline(lines.join(" "), onCiteHover)}</Fragment>
      </p>
    );
  });
}
