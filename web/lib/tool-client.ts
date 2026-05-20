/** Thin client over the FastAPI tool server (api/). */

import "server-only";

import { IdentityPoolClient, Impersonated } from "google-auth-library";

const TOOL_SERVER = process.env.TOOL_SERVER_URL || "http://localhost:8000";

const GCP_PROJECT_NUMBER = process.env.GCP_PROJECT_NUMBER;
const WIF_POOL = process.env.GCP_WIF_POOL;
const WIF_PROVIDER = process.env.GCP_WIF_PROVIDER;
const TARGET_SA = process.env.GCP_SA_EMAIL;

export type AnthropicToolDef = {
  name: string;
  description: string;
  input_schema: Record<string, unknown>;
};

let cached: Impersonated | null = null;

function impersonator(): Impersonated {
  if (cached) return cached;
  if (!GCP_PROJECT_NUMBER || !WIF_POOL || !WIF_PROVIDER || !TARGET_SA) {
    throw new Error("GCP WIF env vars missing (GCP_PROJECT_NUMBER, GCP_WIF_POOL, GCP_WIF_PROVIDER, GCP_SA_EMAIL)");
  }
  const source = new IdentityPoolClient({
    audience: `//iam.googleapis.com/projects/${GCP_PROJECT_NUMBER}/locations/global/workloadIdentityPools/${WIF_POOL}/providers/${WIF_PROVIDER}`,
    subject_token_type: "urn:ietf:params:oauth:token-type:jwt",
    token_url: "https://sts.googleapis.com/v1/token",
    subject_token_supplier: {
      getSubjectToken: async () => {
        const tok = process.env.VERCEL_OIDC_TOKEN;
        if (!tok) throw new Error("VERCEL_OIDC_TOKEN missing");
        return tok;
      },
    },
  });
  cached = new Impersonated({
    sourceClient: source,
    targetPrincipal: TARGET_SA,
    lifetime: 3600,
    delegates: [],
    targetScopes: [],
  });
  return cached;
}

async function authHeaders(): Promise<Record<string, string>> {
  if (!process.env.VERCEL_OIDC_TOKEN) return {};
  const idToken = await impersonator().fetchIdToken(TOOL_SERVER);
  return { Authorization: `Bearer ${idToken}` };
}

export async function listTools(): Promise<AnthropicToolDef[]> {
  const r = await fetch(`${TOOL_SERVER}/tools`, {
    cache: "no-store",
    headers: await authHeaders(),
  });
  if (!r.ok) throw new Error(`tool server /tools ${r.status}`);
  return r.json();
}

export async function invokeTool(
  name: string,
  args: Record<string, unknown>,
): Promise<unknown> {
  const r = await fetch(`${TOOL_SERVER}/tools/${encodeURIComponent(name)}`, {
    method: "POST",
    headers: { "content-type": "application/json", ...(await authHeaders()) },
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
