from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.work_item import ExtractWorkItemsResponse, WorkItemRead
from app.services.work_item_service import extract_work_items_from_sources, list_work_items

router = APIRouter()


@router.get("", response_model=list[WorkItemRead])
def get_work_items(db: Session = Depends(get_db)) -> list[WorkItemRead]:
    items = list_work_items(db=db)
    return [WorkItemRead.model_validate(item) for item in items]


@router.post("/extract", response_model=ExtractWorkItemsResponse)
def extract_work_items(db: Session = Depends(get_db)) -> ExtractWorkItemsResponse:
    created_count = extract_work_items_from_sources(db=db)
    # TODO: Queue Celery extraction job instead of synchronous placeholder processing.
    return ExtractWorkItemsResponse(created_count=created_count, task_queued=False)
