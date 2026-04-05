from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from backend.db.base_model import Base

class Account(Base):
    __tablename__ = "Account"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    role_id: Mapped[int] = mapped_column(ForeignKey("Role.id"))
    email: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="accounts")
    role: Mapped["Role"] = relationship("Role", back_populates="accounts")
    logs: Mapped[list["Log"]] = relationship("Log", back_populates="account")