from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class LogBase(BaseModel):
    account_id: int
    action: str
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    entity: str
    entity_id: Optional[int] = None

class LogCreate(LogBase):
    pass

class LogResponse(LogBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)