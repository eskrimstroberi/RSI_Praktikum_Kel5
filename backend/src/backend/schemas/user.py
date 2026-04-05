from pydantic import BaseModel, Field
from datetime import datetime


class UserBase(BaseModel):
    first_name: str | None = Field(None, max_length=255)
    last_name: str | None = Field(None, max_length=255)
    whatsapp: str | None = Field(None, max_length=30)


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

