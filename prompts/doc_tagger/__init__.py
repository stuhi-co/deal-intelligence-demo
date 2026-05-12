"""Doc tagger prompt.

## Adding a new version

1. Create a new file with version in name: v1_1.py, v2_0.py, etc.
2. Update PROMPT_VERSION below
3. Done!

## Version History
- v1.0 (2026-05-10): Initial version — per-doc tagger for PE deal folder ingestion.
- v1.1 (2026-05-10): Drop full_text_excerpt from output; add xlsx-specific guidance.
- v1.2 (2026-05-11): Strict subsector–sector consistency rule (rule 2 rewrite).
- v1.3 (2026-05-11): Broaden beyond active diligence — add memo_purpose,
  returns_extract, underwriting_case_extract, period_actuals conditional rules
  for portfolio + exited deal kinds.
- v1.4 (2026-05-11): period_actuals supports optional quarterly granularity
  (annual rows have quarter=null; single-quarter rows have quarter=1-4).
"""

from prompts.loader import load_version

# =============================================================================
# CURRENT VERSION - Only change this line to deploy a new prompt version
# =============================================================================
PROMPT_NAME = "doc-tagger"
PROMPT_VERSION = "v1.4"

_current = load_version(__name__, PROMPT_VERSION)

build_system_prompt = _current.build_system_prompt
build_user_prompt = _current.build_user_prompt

__all__ = [
    "PROMPT_NAME",
    "PROMPT_VERSION",
    "build_system_prompt",
    "build_user_prompt",
]
