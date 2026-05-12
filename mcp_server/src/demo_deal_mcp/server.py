"""FastMCP server entry point. Registers all tools."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from .tools import cim, criteria, deals, documents, macro, portco, precedents, sourcing

mcp = FastMCP("demo-deal-platform")

# --- Deal core ---
mcp.tool()(deals.list_deals)
mcp.tool()(deals.get_deal)
mcp.tool()(deals.get_deal_financials)
mcp.tool()(deals.get_deal_outcome)

# --- Precedents / comparables ---
mcp.tool()(precedents.find_precedent_deals)
mcp.tool()(precedents.compare_deals)
mcp.tool()(precedents.analyze_exit_drivers)

# --- Documents / experts ---
mcp.tool()(documents.search_documents)
mcp.tool(name="get_document")(documents.get_document_by_id)

# --- CIM ---
mcp.tool()(cim.parse_cim)
mcp.tool()(cim.evaluate_cim_against_criteria)

# --- Portco ---
mcp.tool()(portco.get_portco_performance)
mcp.tool()(portco.get_underwriting_case)
mcp.tool()(portco.compare_portco_vs_underwriting)

# --- Macro ---
mcp.tool()(macro.get_macro_snapshot)
mcp.tool()(macro.compare_macro)

# --- Sourcing ---
mcp.tool()(sourcing.get_company_profile)
mcp.tool()(sourcing.source_similar_companies)

# --- Criteria ---
mcp.tool()(criteria.get_investment_criteria)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
