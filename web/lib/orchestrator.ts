/** Anthropic tool-use loop, exposed as an async generator that yields events. */

import "server-only";

import Anthropic from "@anthropic-ai/sdk";
import { invokeTool, listTools } from "./tool-client";
import { buildCitation } from "./citations";
import type { Citation, Provenance, ScopeContext } from "./types";

const MODEL = "claude-sonnet-4-6";
const MAX_ITERATIONS = 8;
const MAX_TOKENS = 4096;

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const SYSTEM_PROMPT = `You are Atlas Crossing's Deal Intelligence assistant — a research analyst for a mid-market private equity firm.

You have tools that query the firm's deal pipeline, portfolio companies, exited deals, documents (CIMs, IC memos, expert calls, DD reports), macro snapshots, and investment criteria. ALWAYS use tools to ground your answers in real firm data. Do not fabricate metrics, deal names, or quotes.

CITATIONS — critical: After every factual claim, emit an inline citation marker in the exact format \`<sup data-cite="N"></sup>\` where N is the 1-indexed tool call (in the order you invoked them) that supports the claim. Put the marker immediately after the supporting phrase, before punctuation. Markers must be plain ASCII, no markdown around them. Cite data-bearing tool calls only — e.g. \`get_deal_outcome\`, \`search_documents\`, \`compare_portco_vs_underwriting\`, \`analyze_exit_drivers\`. Do NOT cite directory / index calls like \`list_deals\` or \`source_similar_companies\` — those are navigation, not evidence; the actual numbers come from the per-deal record you load next.

PREFER DOCUMENT SOURCES: When you can support a claim with an actual document (IC memo, expert call transcript, DD report, CIM), prefer \`search_documents\` and \`get_document\` over structured deal records. Document citations let the user open the original — that's how they verify your answer. Reserve deal-record citations for quantitative claims that come from structured data (financials, outcomes, performance).

FORMAT: Write in clean, tight Markdown. Use tables for multi-row comparisons. Use bold for key drivers / themes. Use short paragraphs and avoid filler. Allowed elements: ## and ### headings, **bold**, *italic*, tables, ordered / unordered lists, blockquotes (\`> \`), horizontal rules (\`---\`). DO NOT use emojis, strikethrough (\`~~ ~~\`), or any decorative characters. The audience is a partner who wants the answer first, the evidence next — be editorial, not chatty.

SCOPE: If the user has selected a specific deal or status group (provided below), prefer that scope when choosing what tools to call.`;

type Block =
  | { type: "text"; text: string }
  | { type: "tool_use"; id: string; name: string; input: Record<string, unknown> }
  | { type: "tool_result"; tool_use_id: string; content: string };

type Msg = { role: "user" | "assistant"; content: string | Block[] };

export type OrchestrateInput = {
  message: string;
  scope: ScopeContext | null;
  history?: Msg[];
};

export type StreamEvent =
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

function scopeNote(scope: ScopeContext | null): string {
  if (!scope) return "Scope: none (firm-wide).";
  if (scope.codename)
    return `Scope: Project ${scope.codename} (${scope.company ?? ""}, status ${scope.status ?? "unknown"}).`;
  if (scope.statusGroup) return `Scope: ${scope.statusGroup} deals.`;
  return "Scope: none.";
}

export async function* orchestrateStream({
  message,
  scope,
  history = [],
}: OrchestrateInput): AsyncGenerator<StreamEvent> {
  const t0 = Date.now();
  let tools: Awaited<ReturnType<typeof listTools>>;
  try {
    tools = await listTools();
  } catch (e) {
    yield { type: "error", message: `tool server unavailable: ${(e as Error).message}` };
    return;
  }

  const messages: Msg[] = [
    ...history,
    { role: "user", content: `${scopeNote(scope)}\n\n${message}` },
  ];

  const allCalls: { displayCitation: Omit<Citation, "n"> | null }[] = [];
  let iterations = 0;
  let finalText = "";

  for (let i = 0; i < MAX_ITERATIONS; i++) {
    iterations++;

    let resp;
    try {
      resp = await client.messages.create({
        model: MODEL,
        max_tokens: MAX_TOKENS,
        system: SYSTEM_PROMPT,
        tools: tools as unknown as Anthropic.Tool[],
        messages: messages as unknown as Anthropic.MessageParam[],
      });
    } catch (e) {
      yield { type: "error", message: `Anthropic API: ${(e as Error).message}` };
      return;
    }

    const assistantBlocks: Block[] = resp.content.map((b) => {
      if (b.type === "text") return { type: "text", text: b.text };
      if (b.type === "tool_use")
        return {
          type: "tool_use",
          id: b.id,
          name: b.name,
          input: (b.input ?? {}) as Record<string, unknown>,
        };
      return { type: "text", text: "" };
    });
    messages.push({ role: "assistant", content: assistantBlocks });

    if (resp.stop_reason === "tool_use") {
      const toolUses = assistantBlocks.filter(
        (b): b is Extract<Block, { type: "tool_use" }> => b.type === "tool_use",
      );

      const results: Block[] = [];
      for (const tu of toolUses) {
        const tStart = Date.now();
        yield { type: "tool_use_start", id: tu.id, name: tu.name, input: tu.input };

        let resultPayload: unknown = null;
        let contentStr: string;
        let ok = false;
        try {
          resultPayload = await invokeTool(tu.name, tu.input);
          contentStr =
            typeof resultPayload === "string"
              ? resultPayload
              : JSON.stringify(resultPayload);
          ok = true;
        } catch (e) {
          contentStr = `Tool error: ${(e as Error).message}`;
        }
        yield {
          type: "tool_use_end",
          id: tu.id,
          ok,
          durationMs: Date.now() - tStart,
        };
        results.push({ type: "tool_result", tool_use_id: tu.id, content: contentStr });
        allCalls.push({
          displayCitation: buildCitation(tu.name, tu.input, resultPayload),
        });
      }
      messages.push({ role: "user", content: results });
      continue;
    }

    // end_turn / max_tokens / stop_sequence
    finalText = assistantBlocks
      .filter((b): b is Extract<Block, { type: "text" }> => b.type === "text")
      .map((b) => b.text)
      .join("\n")
      .trim();
    break;
  }

  // Filter + renumber citations, rewrite <sup> markers.
  const citations: Citation[] = [];
  const indexMap = new Map<number, number>();
  let display = 0;
  allCalls.forEach((c, idx) => {
    if (c.displayCitation) {
      display += 1;
      citations.push({ n: display, ...c.displayCitation });
      indexMap.set(idx + 1, display);
    }
  });

  const rewrittenText = finalText.replace(
    /<sup\s+data-cite=["'](\d+)["']\s*><\/sup>/g,
    (_full, raw) => {
      const orig = Number(raw);
      const mapped = indexMap.get(orig);
      return mapped ? `<sup data-cite="${mapped}"></sup>` : "";
    },
  );

  const elapsedSeconds = (Date.now() - t0) / 1000;

  yield { type: "text", text: rewrittenText };
  yield {
    type: "done",
    citations,
    provenance: {
      verdict: "pass",
      time: elapsedSeconds.toFixed(1) + "s",
      violations: 0,
    },
    elapsedSeconds,
    iterations,
  };
}
