import { NextResponse } from "next/server";
import { loadDealTree } from "@/lib/deals-loader";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const deals = await loadDealTree();
    return NextResponse.json({ deals });
  } catch (e) {
    console.error("[deals] load failed", e);
    return NextResponse.json(
      { error: (e as Error).message, deals: [] },
      { status: 500 },
    );
  }
}
