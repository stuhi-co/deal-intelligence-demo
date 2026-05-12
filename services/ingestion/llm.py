"""Anthropic client wrapper with Pydantic-enforced tool-use output.

call_with_schema sends a single message with one tool definition derived from a
Pydantic model. Claude is forced to call that tool, and the tool's input is
parsed back through the Pydantic model — invalid output raises ValidationError
at the SDK boundary rather than at our parsing step.
"""

from __future__ import annotations

import json
import os
from typing import TypeVar

from anthropic import Anthropic
from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)

DEFAULT_MODEL = "claude-sonnet-4-6"
DEFAULT_MAX_TOKENS = 4096


_client: Anthropic | None = None


def _get_client() -> Anthropic:
    global _client
    if _client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY not set in environment.")
        _client = Anthropic(api_key=api_key)
    return _client


def _strip_titles(schema: dict) -> dict:
    """Pydantic schemas include verbose 'title' fields that bloat the tool schema.
    Anthropic accepts them but they hurt the prompt economy. Strip recursively."""
    if isinstance(schema, dict):
        return {k: _strip_titles(v) for k, v in schema.items() if k != "title"}
    if isinstance(schema, list):
        return [_strip_titles(x) for x in schema]
    return schema


def call_with_schema(
    *,
    system: str,
    user: str,
    output_model: type[T],
    tool_name: str = "emit_output",
    tool_description: str | None = None,
    model: str = DEFAULT_MODEL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> T:
    """One Claude call that returns an instance of `output_model`.

    Uses tool-use with tool_choice forcing the named tool. Raises:
      - anthropic.APIError on API failure
      - pydantic.ValidationError if the tool input doesn't match output_model
      - RuntimeError if Claude doesn't emit a tool_use block (shouldn't happen with forced choice)
    """
    client = _get_client()

    schema = _strip_titles(output_model.model_json_schema())

    tool = {
        "name": tool_name,
        "description": tool_description or f"Emit a {output_model.__name__} object.",
        "input_schema": schema,
    }

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        tools=[tool],
        tool_choice={"type": "tool", "name": tool_name},
        messages=[{"role": "user", "content": user}],
    )

    for block in response.content:
        if getattr(block, "type", None) == "tool_use" and block.name == tool_name:
            return output_model.model_validate(block.input)

    raise RuntimeError(
        f"No tool_use block named {tool_name!r} in Claude response. "
        f"Got blocks: {[getattr(b, 'type', '?') for b in response.content]}"
    )


def render_schema_as_json(model: type[BaseModel]) -> str:
    """Useful for diagnostic logging of the schema we send to the LLM."""
    return json.dumps(_strip_titles(model.model_json_schema()), indent=2)
