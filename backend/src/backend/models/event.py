from datetime import datetime
from sqlalchemy import Text, SmallInteger, DateTime
from sqlalchemy.sql import func
from sqlmodel import Column, SQLModel, Relationship, Field


class Event(SQLModel, table=True):
    __tablename__ = "Event"

    id: int = Field(primary_key=True, index=True)

    name: str = Field(Text, nullable=False)
    description: str | None = Field(Text, nullable=True)
    quota: int | None = Field(SmallInteger, nullable=True)

    started_at: datetime | None = Field(DateTime(timezone=True), nullable=True)

    ended_at: datetime | None = Field(DateTime(timezone=True), nullable=True)

    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )

    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
        )
    )

    registrations: list["Registration"] = Relationship(back_populates="event")
