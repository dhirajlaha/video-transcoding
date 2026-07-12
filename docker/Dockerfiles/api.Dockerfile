FROM python:3.12-bookworm

WORKDIR /app
RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock README.md ./
COPY apps ./apps
COPY backend ./backend

RUN uv sync --no-dev --frozen

EXPOSE 8000
CMD ["uv", "run", "--no-dev", "uvicorn", "apps.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
