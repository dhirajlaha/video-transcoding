.PHONY: api worker web infra-up infra-down lint format typecheck test frontend-check backend-check check

api:
	uv run uvicorn apps.api.main:app --reload

worker:
	uv run python -m apps.worker.main

web:
	bun run dev

infra-up:
	docker compose -f docker/compose.yaml up --build

infra-down:
	docker compose -f docker/compose.yaml down

lint:
	uv run ruff check .
	bun run lint

format:
	uv run ruff format .
	bun run format

typecheck:
	uv run mypy .
	bun run typecheck

test:
	uv run pytest

frontend-check:
	bun run lint
	bun run typecheck
	bun run build

backend-check:
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy .
	uv run pytest

check: backend-check frontend-check
