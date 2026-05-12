# demo-deal-mcp

Fake-data MCP server for a private-equity deal intelligence demo. Plugs into Claude Desktop and answers questions like "list pet food deals we've looked at in the last 3 years," "compare this portco to our underwriting base case," or "review this CIM against our investment criteria."

All data is fixture-based — JSON files under `../data/`. No external APIs, no LLM calls inside tools.

## Run

The project is now rooted at the repo root (single `pyproject.toml`). Run from there:

```bash
uv sync
uv run demo-deal-mcp
```

Inspect the tool surface:

```bash
npx @modelcontextprotocol/inspector uv run demo-deal-mcp
```

## Claude Desktop wiring

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "demo-deal-platform": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/gdeshayes/Dev/Stuhi/demo-deal-platform",
        "run",
        "demo-deal-mcp"
      ]
    }
  }
}
```

Restart Claude Desktop.

## Tools

| Tool | Purpose |
|---|---|
| `list_deals` | Filtered listing of deals (sector/subsector/status/year/keyword). |
| `get_deal` | Full record for a deal by ID, codename, alias, or canonical name. |
| `get_deal_financials` | Revenue, EBITDA, margin, EV, **EV/EBITDA entry multiple**. |
| `get_deal_outcome` | Decision, **IRR, MOIC**, hold period, exit type, narrative. |
| `find_precedent_deals` | Precedents by deal anchor or free-form CompanyProfile. |
| `compare_deals` | Side-by-side comparison across financial/outcome dimensions. |
| `analyze_exit_drivers` | Aggregate stats + common patterns for exits in a sector. |
| `search_documents` | Fuzzy search CIMs/expert calls/IC memos/DD reports for quotes. |
| `get_document` | Full doc record by ID, with expert attribution. |
| `parse_cim` | Structured CIM profile (revenue, EBITDA, growth, thesis, risks). |
| `evaluate_cim_against_criteria` | Pass/proceed verdict vs fund criteria. |
| `get_portco_performance` | Portco actuals time series (annual rows; quarterly rows may be interleaved when reported). |
| `get_underwriting_case` | Underwriting base case (semantic year labels — e.g. year_1 / 3 / 5_exit; LLM-chosen). |
| `compare_portco_vs_underwriting` | Per-metric per-year variance report. Quarterly actuals are skipped (case is annual). |
| `get_macro_snapshot` | Sector macro snapshot at a quarter. |
| `compare_macro` | Delta between two snapshots + narrative. |
| `get_company_profile` | Normalized profile (gate before sourcing). |
| `source_similar_companies` | Top-k market universe matches to a profile. |
| `get_investment_criteria` | Fund's size/sector/thesis/return targets. |

## Demo question → tool map

1. **Pet food deals last 3 years** → `list_deals(subsector="pet_food", year_from=2023)`
2. **EBITDA entry multiple for X** → `get_deal_financials(deal="X")`
3. **Review CIM vs precedents** → `parse_cim` → `find_precedent_deals(profile=…)` → `compare_deals`
4. **Manufacturing exits — common traits** → `analyze_exit_drivers(sector="manufacturing")`
5. **IRR on X** → `get_deal_outcome(deal="X")`
6. **Pet food: macro now vs 2020** → `compare_macro("consumer_products", "2020-Q2", "2026-Q1")`
7. **Source similar companies (profile first)** → `get_company_profile` → confirm → `source_similar_companies`
8. **Expert who said channel pricing power had declined** → `search_documents(query="channel pricing power declined", deal="X", doc_type="expert_call")`
9. **Portco vs underwriting** → `compare_portco_vs_underwriting(deal="X")`
10. **Pass/proceed on a CIM** → `get_investment_criteria` + `parse_cim` → `evaluate_cim_against_criteria`

## Data consistency

From the repo root:

```bash
uv run python scripts/check_consistency.py
```

## Ingestion

To ingest a new deal folder, pass `--kind` matching the folder shape:

```bash
# Active diligence (default): CIM / IC memo / expert calls / DD reports
uv run python scripts/ingest_folder.py "01. Project Aurora" --kind active

# Held portfolio company: board packages + financial supplements
uv run python scripts/ingest_folder.py "data/_staged/vanguard_auto" --kind portfolio

# Exited deal: entry IC memo + exit IC memo + returns summary + sell-side process
uv run python scripts/ingest_folder.py "03. Exited Deals/01. Cardinal Filtration Co." --kind exited
```

Each run writes a staged record under `data/_ingested/<codename>/`. Add `--commit` (or `--commit-only` after reviewing the staging dir) to merge into `data/deals.json` and `data/documents.jsonl`. Requires `ANTHROPIC_API_KEY`.

### Cost-saving staging for portfolio companies

A portco folder typically holds ~25 quarterly board packages + ~25 financial
supplements. The portfolio resolver only needs **one row per fiscal year**, so
~75% of those LLM calls are wasted. Use `scripts/stage_portfolio_q4.py` to copy
only the Q4 files (annual rollup per FY) + the most recent quarter into a
staging directory before ingesting:

```bash
uv run python scripts/stage_portfolio_q4.py \
  "/path/to/02. Portfolio Companies/02. Vanguard Auto" \
  data/_staged/vanguard_auto
uv run python scripts/ingest_folder.py data/_staged/vanguard_auto --kind portfolio
```

Note: the tagger (v1.4+) emits quarterly rows when a single-quarter file is
tagged. If you intentionally want quarterly granularity in `portco_actuals`,
stage the desired quarter files in addition to Q4s.

## Cost
- exited deals: 3 deals for $13.36
- portfolio companies (Q4-staged): TBD