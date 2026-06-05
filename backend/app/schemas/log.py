from pydantic import BaseModel
from datetime import datetime
from sqlmodel import SQLModel
from sqlmodel.main import SQLModelConfig


class LogBase(SQLModel):
    account_id: int | None = None
    action: str
    endpoint: str
    method: str
    response_status: int
    duration_ms: float
    ip_address: str | None = None
    user_agent: str | None = None
    entity: str
    entity_id: int | None = None

    model_config: SQLModelConfig = SQLModelConfig(from_attributes=True)


class LogCreate(LogBase):
    pass


class LogUpdate(LogBase):
    pass


class LogPatch(BaseModel):
    account_id: int | None = None
    action: str | None = None
    endpoint: str | None = None
    method: str | None = None
    response_status: int | None = None
    duration_ms: float | None = None
    ip_address: str | None = None
    user_agent: str | None = None
    entity: str | None = None
    entity_id: int | None = None


class LogRead(LogBase):
    id: int
    created_at: datetime
