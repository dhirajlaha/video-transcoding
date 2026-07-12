FROM ghcr.io/astral-sh/uv:python3.12-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml README.md ./
COPY apps ./apps
COPY backend ./backend

RUN uv sync --no-dev

CMD ["uv", "run", "python", "-m", "apps.worker.main"]
