from datetime import datetime
from sqlmodel import SQLModel
from sqlmodel.main import SQLModelConfig


class AccountBase(SQLModel):
    user_id: int
    role_id: int
    email: str
    username: str

    model_config: SQLModelConfig = SQLModelConfig(from_attributes=True)


class AccountCreate(AccountBase):
    password: str


class AccountResponse(AccountBase):
    id: int
    created_at: datetime
    updated_at: datetime
