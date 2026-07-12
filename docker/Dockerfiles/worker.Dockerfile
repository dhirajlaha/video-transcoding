FROM python:3.12-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && pip install --no-cache-dir uv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml uv.lock README.md ./
COPY apps ./apps
COPY backend ./backend

RUN uv sync --no-dev --frozen

CMD ["uv", "run", "--no-dev", "python", "-m", "apps.worker.main"]
