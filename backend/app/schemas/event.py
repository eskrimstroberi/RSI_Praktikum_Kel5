from datetime import datetime
from sqlmodel import SQLModel
from sqlmodel.main import SQLModelConfig


class EventBase(SQLModel):
    name: str
    description: str | None = None
    quota: int | None = None
    started_at: datetime | None = None
    ended_at: datetime | None = None

    model_config: SQLModelConfig = SQLModelConfig(from_attributes=True)


class EventCreate(EventBase):
    pass


class EventUpdate(EventBase):
    pass


class EventResponse(EventBase):
    id: int
    created_at: datetime
    updated_at: datetime
