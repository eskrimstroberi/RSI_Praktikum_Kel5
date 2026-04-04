from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from backend.db.base_model import Base

class Item(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float, default=0.0)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)