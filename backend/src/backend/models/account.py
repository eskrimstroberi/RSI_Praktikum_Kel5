from datetime import datetime
from sqlalchemy import Text, DateTime
from sqlalchemy.sql import func
from sqlmodel import Column, SQLModel, Relationship, Field


class Account(SQLModel, table=True):
    __tablename__ = "Account"

    id: int = Field(primary_key=True, index=True)
    user_id: int = Field(foreign_key="User.id")
    role_id: int = Field(foreign_key="Role.id")
    email: str = Field(Text, nullable=False, unique=True)
    username: str = Field(max_length=16, nullable=False, unique=True)
    password: str = Field(Text, nullable=False)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    updated_at: datetime | None = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=True,
        )
    )

    user: "User" = Relationship(back_populates="accounts")
    role: "Role" = Relationship(back_populates="accounts")
    logs: list["Log"] = Relationship(back_populates="account")
