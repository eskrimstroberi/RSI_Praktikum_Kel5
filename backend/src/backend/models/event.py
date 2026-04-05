from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, SmallInteger, DateTime
from sqlalchemy.sql import func
from backend.db.base_model import Base


class Event(Base):
    __tablename__ = "Event"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    quota: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)

    started_at: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    ended_at: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    registrations = relationship("Registration", back_populates="event")