from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from backend.db.base_model import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(255))
    last_name = Column(String(255))
    whatsapp = Column(String(30))

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    accounts = relationship("Account", back_populates="user")
    registrations = relationship("Registration", back_populates="user")