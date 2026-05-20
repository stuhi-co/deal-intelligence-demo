FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

COPY api ./api
COPY mcp_server ./mcp_server
COPY data ./data

ENV PYTHONPATH=/app/mcp_server/src
ENV PORT=8080
EXPOSE 8080

CMD ["sh", "-c", "uv run --no-sync uvicorn api.main:app --host 0.0.0.0 --port ${PORT}"]
