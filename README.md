# Video Transcoding Platform

Plain monorepo for a React frontend, FastAPI backend, and Python queue worker.

## Stack

- Frontend: Bun, React 19, Vite, TypeScript, Tailwind CSS, TanStack Query, React Router, React Hook Form, Zod, ESLint, Prettier
- Backend: FastAPI, SQLAlchemy, Alembic, Pydantic v2, uv, Ruff, Mypy, Pytest, pytest-cov
- Infrastructure: PostgreSQL, RabbitMQ, MinIO, FFmpeg, Docker Compose
- Architecture: Clean/Hexagonal Architecture, domain events, outbox-ready persistence boundary, queue worker, presigned uploads

## Layout

```text
apps/
  api/       FastAPI entrypoint
  worker/    queue worker entrypoint
  web/       React/Vite frontend
backend/
  domain/
  application/
  infrastructure/
  config/
docker/
  compose.yaml
  Dockerfiles/
scripts/
tests/
```

## Backend

```bash
uv sync
uv run uvicorn apps.api.main:app --reload
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy .
```

## Frontend

```bash
bun install
bun run dev
bun run lint
bun run typecheck
bun run build
```

## Infrastructure

```bash
docker compose -f docker/compose.yaml up --build
```

During development, the frontend is intentionally kept outside Docker for Vite speed.

## API contract generation

FastAPI exposes OpenAPI at `/openapi.json`. Generate frontend types from a running API:

```bash
bun run generate:api
```
