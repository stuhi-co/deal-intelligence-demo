"""Tool discovery + invocation endpoints.

`GET /tools` returns Anthropic-shaped tool schemas derived from the FastMCP
server's registered tool list. `POST /tools/{name}` invokes a single tool
with a JSON body of arguments and returns its result.
"""

from __future__ import annotations

import json
from typing import Any

from fastapi import APIRouter, Body, HTTPException

from demo_deal_mcp.server import mcp

router = APIRouter()


def _to_anthropic_schema(tool: Any) -> dict[str, Any]:
    """Convert a FastMCP Tool to the Anthropic tool-definition shape."""
    return {
        "name": tool.name,
        "description": tool.description or "",
        "input_schema": tool.inputSchema or {"type": "object", "properties": {}},
    }


@router.get("/tools")
async def list_tools() -> list[dict[str, Any]]:
    tools = await mcp.list_tools()
    return [_to_anthropic_schema(t) for t in tools]


def _flatten_content(result: Any) -> Any:
    """Turn FastMCP CallToolResult content into a JSON-serializable payload.

    FastMCP returns either a list of content blocks or a (content, structured)
    tuple. Prefer the structured payload when present; otherwise stitch text
    blocks together and try to parse JSON.
    """
    # Newer FastMCP returns a tuple (content_blocks, structured_content).
    if isinstance(result, tuple) and len(result) == 2:
        content, structured = result
        if structured is not None:
            return structured
    else:
        content = result

    texts: list[str] = []
    for block in content or []:
        text = getattr(block, "text", None)
        if text is not None:
            texts.append(text)
    joined = "".join(texts).strip()
    if not joined:
        return None
    try:
        return json.loads(joined)
    except json.JSONDecodeError:
        return joined


@router.post("/tools/{name}")
async def invoke_tool(name: str, payload: dict[str, Any] = Body(default_factory=dict)) -> dict[str, Any]:
    try:
        raw = await mcp.call_tool(name, payload)
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Unknown tool: {name}")
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(e))
    return {"result": _flatten_content(raw)}
