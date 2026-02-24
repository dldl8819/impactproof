from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.ingest import IngestTextRequest, SourceDocRead
from app.services.ingestion_service import create_source_doc

router = APIRouter()


@router.post("/text", response_model=SourceDocRead, status_code=status.HTTP_201_CREATED)
def ingest_text(payload: IngestTextRequest, db: Session = Depends(get_db)) -> SourceDocRead:
    source_doc = create_source_doc(db=db, payload=payload)
    return SourceDocRead.model_validate(source_doc)
