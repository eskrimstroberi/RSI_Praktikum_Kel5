from datetime import datetime
from sqlalchemy import Text, DateTime
from sqlalchemy.sql import func
from sqlmodel import Column, SQLModel, Relationship, Field


class Log(SQLModel, table=True):
    __tablename__ = "Log"

    id: int = Field(primary_key=True, index=True)
    account_id: int | None = Field(default=None, foreign_key="Account.id")
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    action: str = Field(max_length=75, nullable=False)
    endpoint: str = Field(max_length=255, nullable=False)
    method: str = Field(max_length=10, nullable=False)
    response_status: int = Field(nullable=False)
    duration_ms: float = Field(nullable=False)
    ip_address: str | None = Field(Text, nullable=False)
    user_agent: str | None = Field(Text, nullable=False)
    entity: str = Field(max_length=50, nullable=False)
    entity_id: int | None = Field(nullable=True)

    account: "Account" = Relationship(back_populates="logs")
