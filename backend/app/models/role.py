from sqlmodel import SQLModel, Field, Relationship, String
import sqlalchemy as sa
from app.models.enums import RoleName


class Role(SQLModel, table=True):
    __tablename__ = "Role"

    id: int = Field(primary_key=True, index=True)
    name: RoleName = Field(
        sa_column=sa.Column(sa.String(255), unique=True, nullable=False)
    )

    accounts: list["Account"] = Relationship(back_populates="role")
