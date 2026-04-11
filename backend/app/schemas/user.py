from pydantic import Field
from datetime import datetime
from sqlmodel import SQLModel
from sqlmodel.main import SQLModelConfig


class UserBase(SQLModel):
    first_name: str | None = Field(None, max_length=255)
    last_name: str | None = Field(None, max_length=255)
    whatsapp: str | None = Field(None, max_length=30)

    model_config: SQLModelConfig = SQLModelConfig(from_attributes=True)


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
