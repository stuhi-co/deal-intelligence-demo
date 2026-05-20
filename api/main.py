"""FastAPI wrapper around the demo_deal_mcp tool server.

Exposes the same tools the MCP server registers over HTTP so the Next.js
chat orchestrator can call them as Anthropic tool-use endpoints.
"""

from __future__ import annotations

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import tools

app = FastAPI(title="Atlas Crossing tool server")

_default_origins = "http://localhost:3000,http://127.0.0.1:3000"
_origins = [o.strip() for o in os.environ.get("CORS_ORIGINS", _default_origins).split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(tools.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
