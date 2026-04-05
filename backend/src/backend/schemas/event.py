from pydantic import BaseModel
from datetime import datetime


class EventBase(BaseModel):
    name: str
    description: str | None = None
    quota: int | None = None
    started_at: datetime | None = None
    ended_at: datetime | None = None


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

