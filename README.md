# ImpactProof

ImpactProof is a local-first monorepo for turning raw operational evidence into structured, reviewable impact records. It includes a Vue 3 frontend for ingestion/report workflows, a FastAPI backend for APIs and persistence, and a Celery worker for background extraction/scoring jobs (LLM integrations intentionally stubbed with TODO placeholders).

## Local Setup (Docker Compose)

1. Copy env file:
   `cp .env.example .env` (PowerShell: `Copy-Item .env.example .env`)
2. Start services:
   `docker compose -f infra/docker-compose.yml up --build`
3. Open:
   - Backend API: `http://localhost:8000`
   - API docs: `http://localhost:8000/docs`
   - Frontend (if enabled in compose with `--profile ui`): `http://localhost:5173`
   - Postgres (host): `localhost:5433` (container `5432`)

### Common Compose Commands

- Start core stack (postgres, redis, backend, worker):
  `docker compose -f infra/docker-compose.yml up --build`
- Start with frontend too:
  `docker compose -f infra/docker-compose.yml --profile ui up --build`
- Stop stack:
  `docker compose -f infra/docker-compose.yml down`

## Run Frontend and Backend Separately (without Docker for app processes)

### Backend (FastAPI)

1. Ensure Postgres and Redis are running (via Docker compose or local installs).
2. From `backend/`:
   `python -m venv .venv`
   `./.venv/Scripts/Activate.ps1` (Windows PowerShell)
   `pip install -e .`
   `alembic upgrade head`
   `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

### Frontend (Vue 3 + Vite)

1. From `frontend/`:
   `npm install`
   `npm run dev`
2. Frontend uses `VITE_API_BASE_URL` (defaults to `http://localhost:8000`).

## API Endpoints Summary

- `GET /health` - service health check
- `POST /ingest/text` - store a source document (`source_type`, `title`, `content`, optional `occurred_at`)
- `POST /work-items/extract` - create placeholder work items from stored source docs
- `GET /work-items` - list work items

## Notes

- LLM extraction/scoring is not implemented yet. Placeholder logic and TODOs are included in backend services and worker tasks.
- Alembic migrations are included for initial database setup.

## Manual Verification Flow (Ingest -> Extract -> Work Items)

1. Ingest a source doc:
   ```bash
   curl -X POST http://localhost:8000/ingest/text \
     -H "Content-Type: application/json" \
     -d '{
       "source_type":"ticket",
       "title":"Payment timeout follow-up",
       "content":"Connection pool tuning reduced timeout frequency.",
       "occurred_at":"2026-05-01T08:00:00Z"
     }'
   ```
2. Extract work items:
   ```bash
   curl -X POST http://localhost:8000/work-items/extract
   ```
3. Read work items:
   ```bash
   curl http://localhost:8000/work-items
   ```
4. Re-run extract with same source docs:
   - Expected: `created_count` becomes `0`
   - Meaning: duplicate extraction for the same `source_doc_id` is blocked.

## Run Backend Tests

From `backend/`:

```bash
python -m venv .venv
./.venv/Scripts/Activate.ps1   # Windows PowerShell
pip install -e .[dev]
pytest
```
