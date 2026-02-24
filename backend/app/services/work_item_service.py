from sqlalchemy import select

from app.models.source_doc import SourceDoc
from app.models.work_item import WorkItem


def list_work_items(*, db) -> list[WorkItem]:
    stmt = select(WorkItem).order_by(WorkItem.created_at.desc(), WorkItem.id.desc())
    return list(db.scalars(stmt).all())


def extract_work_items_from_sources(*, db) -> int:
    source_docs = list(db.scalars(select(SourceDoc).order_by(SourceDoc.id.asc())).all())
    created_count = 0

    for doc in source_docs:
        # TODO: Replace placeholder extraction/scoring with async Celery + LLM pipeline.
        snippet = doc.content.strip().replace("\n", " ")[:220]
        work_item = WorkItem(
            category="Operational Improvement",
            problem=f"Evidence captured from {doc.source_type}: {doc.title}",
            action=f"Placeholder extraction generated from source text snippet: {snippet}",
            result="Structured work item created for later review and refinement.",
            impact_score=min(max(len(doc.content) / 100.0, 1.0), 10.0),
            evidence_json={
                "source_doc_id": doc.id,
                "source_type": doc.source_type,
                "title": doc.title,
            },
        )
        db.add(work_item)
        created_count += 1

    if created_count:
        db.commit()

    return created_count
