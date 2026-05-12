"""Per-document tagging stage. The only LLM call in v1.

One Claude Sonnet call per primary doc, with output enforced via tool-use against
the TaggerOutput schema. If a subsector value doesn't fit its chosen sector (a
two-level enum check that pydantic alone can't enforce), we mark an extraction
warning and clear the field rather than failing the whole doc.
"""

from __future__ import annotations

from pathlib import Path

from pydantic import ValidationError

from prompts.doc_tagger import build_system_prompt, build_user_prompt
from .extractors import extract
from .llm import call_with_schema
from .schemas import TaggerOutput, TriageEntry
from .taxonomy import enums_yaml_text, is_valid_subsector


# Rough head/tail truncation — Claude can handle long context but we don't need to
# pay for the full text of a 200-page CIM when the first and last chunks carry signal.
_HEAD_CHARS = 250_000
_TAIL_CHARS = 50_000


def _truncate(text: str) -> str:
    if len(text) <= _HEAD_CHARS + _TAIL_CHARS:
        return text
    return (
        text[:_HEAD_CHARS]
        + "\n\n... [middle truncated] ...\n\n"
        + text[-_TAIL_CHARS:]
    )


def tag_document(
    *,
    entry: TriageEntry,
    folder_codename: str,
) -> TaggerOutput:
    """Extract text from the doc, run one tagging call, return the validated output."""
    path = entry.file.abs_path

    try:
        text = extract(path)
    except Exception as e:  # noqa: BLE001
        # Build a minimal "I couldn't read this" payload so the pipeline can keep going.
        raise RuntimeError(f"extract failed for {path}: {e}") from e

    text = _truncate(text)

    system = build_system_prompt(enums_yaml=enums_yaml_text())
    user = build_user_prompt(
        folder_codename=folder_codename,
        file_path=entry.file.path,
        doc_type_hint=entry.doc_type_hint or "(none)",
        extracted_text=text,
    )

    try:
        output = call_with_schema(
            system=system,
            user=user,
            output_model=TaggerOutput,
            tool_name="emit_tagged_document",
            tool_description="Emit a structured TaggerOutput for the provided document.",
        )
    except ValidationError as e:
        raise RuntimeError(f"tagger output validation failed for {path}: {e}") from e

    # Post-parse subsector check (two-level enum constraint that can't live in the JSON schema).
    if output.deal_context is not None:
        sec = output.deal_context.sector.value if output.deal_context.sector else None
        sub = output.deal_context.subsector
        if not is_valid_subsector(sec, sub):
            output.extraction_warnings.append(
                f"subsector {sub!r} is not valid for sector {sec!r}; cleared."
            )
            output.deal_context.subsector = None

    return output
