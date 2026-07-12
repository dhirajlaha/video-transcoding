FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /app
COPY pyproject.toml README.md ./
COPY apps ./apps
COPY backend ./backend

RUN uv sync --no-dev

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "apps.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
