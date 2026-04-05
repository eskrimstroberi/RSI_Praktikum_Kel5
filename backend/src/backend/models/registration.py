from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from backend.db.base_model import Base


class Registration(Base):
    __tablename__ = "Registration"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("User.id"),
        nullable=False
    )

    event_id: Mapped[int] = mapped_column(
        ForeignKey("Event.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(back_populates="registrations")
    event: Mapped["Event"] = relationship(back_populates="registrations")