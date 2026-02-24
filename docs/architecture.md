# Architecture

## Overview

ImpactProof is a modular monolith with a Vue frontend, FastAPI backend, Postgres persistence, Redis-backed background worker, and a future reporting/export layer.

## Components

- `frontend/` (Vue 3 + TypeScript + Vite): ingestion UI, work-item review, reporting placeholder
- `backend/` (FastAPI + SQLAlchemy + Alembic): API endpoints, domain services, persistence
- `worker/` (Celery + Redis): asynchronous extraction/scoring jobs (placeholder implementation)
- `infra/` (Docker Compose): local dev infrastructure orchestration
- `docs/`: architecture and roadmap documentation

## Backend Design (Modular Monolith)

- `app/api/routes/*`: HTTP route handlers by feature
- `app/services/*`: business/application logic
- `app/models/*`: SQLAlchemy ORM models
- `app/schemas/*`: request/response schemas
- `app/core/*`: configuration, DB session, logging

This keeps boundaries explicit while remaining deployable as a single service.

## Data Flow (Current Placeholder)

1. User submits raw text evidence via `POST /ingest/text`
2. Backend stores `SourceDoc`
3. User triggers `POST /work-items/extract`
4. Backend creates placeholder `WorkItem` rows from `SourceDoc` rows
5. Frontend lists work items via `GET /work-items`

## Future Evolution

- Replace placeholder extraction with async Celery pipeline invoking LLM/provider adapters
- Add deduplication, idempotency keys, and retry policies
- Add authentication / tenancy
- Add report generation and evidence traceability UI
