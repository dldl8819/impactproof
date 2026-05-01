from datetime import datetime, timezone

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.work_item import WorkItem


def _ingest_payload(title: str, content: str) -> dict:
    return {
        "source_type": "ticket",
        "title": title,
        "content": content,
        "occurred_at": datetime.now(timezone.utc).isoformat(),
    }


def test_ingest_text_works(client: TestClient) -> None:
    payload = _ingest_payload("Incident follow-up", "Timeout issue resolved by pool tuning.")
    response = client.post("/ingest/text", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["id"] > 0
    assert body["source_type"] == payload["source_type"]
    assert body["title"] == payload["title"]
    assert body["content"] == payload["content"]


def test_extract_creates_items_once(client: TestClient) -> None:
    client.post("/ingest/text", json=_ingest_payload("A", "first evidence"))
    client.post("/ingest/text", json=_ingest_payload("B", "second evidence"))

    response = client.post("/work-items/extract")

    assert response.status_code == 200
    assert response.json()["created_count"] > 0

    items_response = client.get("/work-items")
    assert items_response.status_code == 200
    assert len(items_response.json()) == 2


def test_extract_is_idempotent_per_source_doc(client: TestClient) -> None:
    client.post("/ingest/text", json=_ingest_payload("Idempotent", "same source should not duplicate"))

    first = client.post("/work-items/extract")
    second = client.post("/work-items/extract")

    assert first.status_code == 200
    assert first.json()["created_count"] == 1
    assert second.status_code == 200
    assert second.json()["created_count"] == 0


def test_db_unique_constraint_on_source_doc_id(client: TestClient, db_session: Session) -> None:
    ingest_response = client.post(
        "/ingest/text", json=_ingest_payload("Constraint", "unique source_doc_id constraint")
    )
    source_doc_id = ingest_response.json()["id"]

    first = WorkItem(
        source_doc_id=source_doc_id,
        category="Ops",
        problem="p",
        action="a",
        result="r",
        impact_score=1.0,
        evidence_json={"source_type": "ticket", "title": "Constraint"},
    )
    second = WorkItem(
        source_doc_id=source_doc_id,
        category="Ops",
        problem="p2",
        action="a2",
        result="r2",
        impact_score=2.0,
        evidence_json={"source_type": "ticket", "title": "Constraint2"},
    )

    db_session.add(first)
    db_session.commit()

    db_session.add(second)
    with pytest.raises(IntegrityError):
        db_session.commit()

    db_session.rollback()
