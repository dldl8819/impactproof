COMPOSE_FILE=infra/docker-compose.yml

.PHONY: up up-ui down logs backend-dev frontend-dev migrate lint format test

up:
	docker compose -f infra/docker-compose.yml up --build

up-ui:
	docker compose -f infra/docker-compose.yml --profile ui up --build

down:
	docker compose -f infra/docker-compose.yml down

logs:
	docker compose -f infra/docker-compose.yml logs -f --tail=200

backend-dev:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend-dev:
	cd frontend && npm run dev -- --host 0.0.0.0 --port 5173

migrate:
	cd backend && alembic upgrade head

lint:
	cd backend && ruff check app
	cd frontend && npm run typecheck

format:
	cd backend && ruff format app

test:
	cd backend && pytest -q
