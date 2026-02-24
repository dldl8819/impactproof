from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class IngestTextRequest(BaseModel):
    source_type: str = Field(min_length=1, max_length=50)
    title: str = Field(min_length=1, max_length=255)
    content: str = Field(min_length=1)
    occurred_at: datetime | None = None


class SourceDocRead(BaseModel):
    id: int
    source_type: str
    title: str
    content: str
    occurred_at: datetime | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
