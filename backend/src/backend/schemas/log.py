from pydantic import BaseModel, ConfigDict
from datetime import datetime


class LogBase(BaseModel):
    account_id: int
    action: str
    ip_address: str | None = None
    user_agent: str | None = None
    entity: str
    entity_id: int | None = None


class LogCreate(LogBase):
    pass


class LogResponse(LogBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

