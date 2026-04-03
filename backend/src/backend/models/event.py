from sqlalchemy import Column, Integer, Text, DateTime, SmallInteger
from sqlalchemy.orm import relationship
from backend.db.base_model import Base


class Event(Base):
    __tablename__ = "Event"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(Text)
    description = Column(Text)
    quota = Column(SmallInteger)

    started_at = Column(DateTime)
    ended_at = Column(DateTime)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    registrations = relationship("Registration", back_populates="event")