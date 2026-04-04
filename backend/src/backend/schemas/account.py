from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class AccountBase(BaseModel):
    user_id: int
    role_id: int
    email: str
    username: str

class AccountCreate(AccountBase):
    password: str 

class AccountResponse(AccountBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)