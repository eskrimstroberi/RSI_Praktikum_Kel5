from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func
from backend.db.base_model import Base


class User(Base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    first_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    whatsapp: Mapped[str | None] = mapped_column(String(30), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    accounts: Mapped[list["Account"]] = relationship(back_populates="user")
    registrations: Mapped[list["Registration"]] = relationship(
        back_populates="user"
    )