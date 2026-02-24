from app.models.source_doc import SourceDoc
from app.schemas.ingest import IngestTextRequest


def create_source_doc(*, db, payload: IngestTextRequest) -> SourceDoc:
    source_doc = SourceDoc(
        source_type=payload.source_type,
        title=payload.title,
        content=payload.content,
        occurred_at=payload.occurred_at,
    )
    db.add(source_doc)
    db.commit()
    db.refresh(source_doc)
    return source_doc
