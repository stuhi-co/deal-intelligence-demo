/** Anthropic tool-use loop, exposed as an async generator that yields events. */

import "server-only";

import Anthropic from "@anthropic-ai/sdk";
import { invokeTool, listTools } from "./tool-client";
import { buildCitation } from "./citations";
import type { ChatMessage, Citation, Provenance, ScopeContext } from "./types";

const MAX_HISTORY_PAIRS = 5;

const MODEL = "claude-sonnet-4-6";
const MAX_ITERATIONS = 8;
const MAX_TOKENS = 4096;

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

const SYSTEM_PROMPT = `You are Atlas Crossing's Deal Intelligence assistant — a research analyst for a mid-market private equity firm.

You have tools that query the firm's deal pipeline, portfolio companies, exited deals, documents (CIMs, IC memos, expert calls, DD reports), macro snapshots, and investment criteria. ALWAYS use tools to ground your answers in real firm data. Do not fabricate metrics, deal names, or quotes.

CITATIONS — critical and strict: The user's "Sources" rail only renders **documents** (IC memos, expert call transcripts, DD reports, CIMs, financial models). It does NOT render structured-data tool calls (\`get_deal\`, \`get_deal_outcome\`, \`compare_*\`, \`analyze_*\`, \`get_macro_snapshot\`, etc.) — those are reasoning fuel for you, not user-facing sources.

Therefore: every factual claim in your answer MUST be backed by a \`search_documents\` or \`get_document\` call, and you must cite that call. Even if you got the number from \`get_deal_outcome\` or \`get_portco_performance\`, you must then call \`search_documents\` (with a targeted query like the metric you're citing) to find the underlying IC memo / DD report / expert call / model output, and cite that document.

Marker format: \`<sup data-cite="N"></sup>\` immediately after the supporting phrase, before punctuation. N is the 1-indexed tool call. ASCII only, no markdown around it. Only cite \`search_documents\`, \`get_document\`, or \`parse_cim\` — citing any other tool's index will be stripped from the answer.

Workflow per claim: (1) compute the number from structured tools as needed, (2) call \`search_documents\` to surface the document that contains/supports that claim, (3) cite that document index. If multiple claims share a source, the same N can be reused.

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

/**
 * Build Anthropic-shaped history from prior UI messages.
 *
 * Hybrid policy: keep the last N completed (user, assistant) pairs as
 * plain-text turns. Intermediate tool_use / tool_result blocks from prior
 * turns are dropped — if the model needs the evidence again it will re-call
 * the tool. Stale <sup data-cite="N"> markers from prior assistant text are
 * stripped so the model doesn't copy meaningless citation numbers.
 */
export function buildHistory(messages: ChatMessage[]): Msg[] {
  const pairs: Array<{ user: string; assistant: string }> = [];
  let i = messages.length - 1;
  while (i >= 0 && pairs.length < MAX_HISTORY_PAIRS) {
    const m = messages[i];
    if (m.role !== "assistant" || m.status !== "done" || !m.text.trim()) {
      i--;
      continue;
    }
    const prev = messages[i - 1];
    if (!prev || prev.role !== "user") {
      i--;
      continue;
    }
    pairs.unshift({
      user: prev.content,
      assistant: m.text.replace(/<sup\s+data-cite=["']\d+["']\s*><\/sup>/g, ""),
    });
    i -= 2;
  }
  const out: Msg[] = [];
  for (const p of pairs) {
    out.push({ role: "user", content: p.user });
    out.push({ role: "assistant", content: p.assistant });
  }
  return out;
}

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
