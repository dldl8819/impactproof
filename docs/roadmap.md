# Roadmap

## Phase 0 (This Scaffold)

- Monorepo structure and local dev stack
- FastAPI backend with Postgres models and Alembic
- Vue frontend pages for ingest/work-items/reports (placeholder)
- Celery worker + Redis broker sample task

## Phase 1 (Core Product Loop)

- Async extraction pipeline triggered from API to Celery
- Deterministic parsing heuristics + provider abstraction for future LLM calls
- Work item review/edit UI
- Filtering, pagination, and basic report templates

## Phase 2 (Quality & Trust)

- Evidence linking and provenance metadata
- Idempotent ingestion + duplicate detection
- Audit logs
- Tests (unit/integration/e2e) and CI pipeline

## Phase 3 (Production Features)

- Auth/RBAC
- Multi-workspace support
- Background scheduling and monitoring dashboards
- Export integrations (PDF, docs, HR systems)
