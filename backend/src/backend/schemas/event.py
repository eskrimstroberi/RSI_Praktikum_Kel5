from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class EventBase(BaseModel):
    name: str
    description: Optional[str] = None
    quota: int
    started_at: datetime
    ended_at: datetime

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)