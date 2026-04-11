from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlmodel import Column, SQLModel, Relationship, Field


class User(SQLModel, table=True):
    __tablename__ = "User"

    id: int = Field(primary_key=True, index=True)

    first_name: str | None = Field(max_length=255, nullable=True)
    last_name: str | None = Field(max_length=255, nullable=True)
    whatsapp: str | None = Field(max_length=30, nullable=True)

    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )

    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
        )
    )

    accounts: list["Account"] = Relationship(back_populates="user")
    registrations: list["Registration"] = Relationship(back_populates="user")
