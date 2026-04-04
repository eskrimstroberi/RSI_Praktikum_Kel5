from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    whatsapp: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)