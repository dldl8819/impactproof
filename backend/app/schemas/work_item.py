from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class WorkItemRead(BaseModel):
    id: int
    category: str
    problem: str
    action: str
    result: str
    impact_score: float | None
    evidence_json: dict[str, Any]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ExtractWorkItemsResponse(BaseModel):
    created_count: int
    task_queued: bool = False
