from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.base_model import Base


class Registration(Base):
    __tablename__ = "Registration"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("Event.id"), nullable=False)

    user = relationship("User", back_populates="registrations")
    event = relationship("Event", back_populates="registrations")