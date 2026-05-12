"""Taxonomy governance.

Loads enums.yaml as the firm's Layer 1 taxonomy. Provides validation helpers and
the refuse-on-proposal commit gate. v1 has no acceptance path — if any
taxonomy_proposals exist when --commit is requested, the run refuses with the
proposals listed. v2 will add --accept-taxonomy-proposals.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml


def repo_root() -> Path:
    """services/ingestion/taxonomy.py → parents[2] is the repo root."""
    return Path(__file__).resolve().parents[2]


@lru_cache(maxsize=1)
def load_enums() -> dict[str, Any]:
    return yaml.safe_load((repo_root() / "enums.yaml").read_text())


def enums_yaml_text() -> str:
    """The raw text we inline into the tagger prompt so the LLM sees the taxonomy verbatim."""
    return (repo_root() / "enums.yaml").read_text()


def valid_subsectors(sector: str) -> list[str]:
    enums = load_enums()
    return list(enums.get("subsector", {}).get(sector, []))


def is_valid_subsector(sector: str | None, subsector: str | None) -> bool:
    if sector is None or subsector is None:
        return True
    return subsector in valid_subsectors(sector)


class TaxonomyGateError(RuntimeError):
    """Raised by enforce_commit_gate when proposals exist and --commit was requested."""


def enforce_commit_gate(proposals: list[dict]) -> None:
    """If any proposals exist, refuse the commit with a human-readable message.

    v1 has no acceptance path. The analyst must either:
      - edit enums.yaml manually and re-run, or
      - edit data/_ingested/<deal>/taxonomy_proposals.yaml to drop entries they reject.
    """
    if not proposals:
        return
    lines = [
        "Refusing --commit: taxonomy proposals require human review.",
        "",
        "The pipeline encountered values not in enums.yaml. The tagger persisted the",
        "closest existing value, but flagged a proposed addition for each:",
        "",
    ]
    for p in proposals:
        lines.append(
            f"  - {p.get('field')}: proposed={p.get('proposed_value')!r} "
            f"(used closest_existing={p.get('closest_existing')!r}, confidence={p.get('confidence')})"
        )
        if p.get("rationale"):
            lines.append(f"      rationale: {p['rationale']}")
    lines += [
        "",
        "To proceed:",
        "  1. Review the proposals in data/_ingested/<deal>/taxonomy_proposals.yaml",
        "  2. Manually add accepted values to enums.yaml (and update demo_deal_mcp/models.py if it's an enum class)",
        "  3. Re-run the ingestion (cached LLM calls are not yet implemented in v1, so it re-tags)",
        "",
        "(v2 will add --accept-taxonomy-proposals to automate step 2.)",
    ]
    raise TaxonomyGateError("\n".join(lines))
