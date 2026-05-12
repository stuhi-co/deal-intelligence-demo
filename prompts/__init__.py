"""Prompts package.

## Structure

    prompts/
    ├── __init__.py          # minimal — just enables `import prompts.<name>`
    ├── loader.py            # load_version() + list_versions() helpers
    └── <prompt_name>/
        ├── __init__.py      # PROMPT_VERSION = "v1.0"; re-exports build_* from current version
        └── v1_0.py          # SYSTEM_PROMPT, USER_PROMPT_TEMPLATE, build_system_prompt, build_user_prompt

## Adding a new prompt

1. Create `prompts/<your_prompt>/v1_0.py` with `build_system_prompt` and `build_user_prompt`.
2. Create `prompts/<your_prompt>/__init__.py` that loads via `prompts.loader.load_version`.
3. Import as `from prompts.<your_prompt> import build_system_prompt, build_user_prompt`.

## Adding a new version of an existing prompt

1. Copy `v1_0.py` → `v1_1.py` (or `v2_0.py` for breaking changes).
2. Update `PROMPT_VERSION` in that prompt's `__init__.py`.
"""
