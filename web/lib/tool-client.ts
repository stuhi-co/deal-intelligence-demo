/** Thin client over the FastAPI tool server (api/). */

import "server-only";

const TOOL_SERVER = process.env.TOOL_SERVER_URL || "http://localhost:8000";

export type AnthropicToolDef = {
  name: string;
  description: string;
  input_schema: Record<string, unknown>;
};

export async function listTools(): Promise<AnthropicToolDef[]> {
  const r = await fetch(`${TOOL_SERVER}/tools`, { cache: "no-store" });
  if (!r.ok) throw new Error(`tool server /tools ${r.status}`);
  return r.json();
}

export async function invokeTool(
  name: string,
  args: Record<string, unknown>,
): Promise<unknown> {
  const r = await fetch(`${TOOL_SERVER}/tools/${encodeURIComponent(name)}`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(args ?? {}),
    cache: "no-store",
  });
  if (!r.ok) {
    const detail = await r.text().catch(() => "");
    throw new Error(`tool ${name} failed: ${r.status} ${detail.slice(0, 200)}`);
  }
  const j = (await r.json()) as { result: unknown };
  return j.result;
}
