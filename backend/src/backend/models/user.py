from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func
from backend.db.base_model import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    whatsapp: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), onupdate=func.now())

    accounts: Mapped[list["Account"]] = relationship(back_populates="user")
    registration: Mapped["Registration"] = relationship(back_populates="user", uselist=False)