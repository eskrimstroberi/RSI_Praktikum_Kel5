from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventBase(BaseModel):
    name: str
    description: Optional[str] = None
    quota: Optional[int] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    pass


class EventResponse(EventBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True