from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from backend.db.base_model import Base

class Role(Base):
    __tablename__ = "Role"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))

    accounts: Mapped[list["Account"]] = relationship("Account", back_populates="role")