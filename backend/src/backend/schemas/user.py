from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    first_name: Optional[str] = Field(None, max_length=255)
    last_name: Optional[str] = Field(None, max_length=255)
    whatsapp: Optional[str] = Field(None, max_length=30)


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True