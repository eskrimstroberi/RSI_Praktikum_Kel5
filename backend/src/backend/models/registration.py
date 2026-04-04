from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from backend.db.base_model import Base

class Registration(Base):
    __tablename__ = "registration"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    event_id: Mapped[int] = mapped_column(ForeignKey("event.id"))
    
    user: Mapped["User"] = relationship(back_populates="registrations")
    event: Mapped["Event"] = relationship(back_populates="registrations")
    