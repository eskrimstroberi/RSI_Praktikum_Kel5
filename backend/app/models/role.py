from sqlmodel import SQLModel, Field, Relationship
from app.models.enums import RoleName


class Role(SQLModel, table=True):
    __tablename__ = "Role"

    id: int = Field(primary_key=True, index=True)
    name: RoleName = Field(unique=True)

    accounts: list["Account"] = Relationship(back_populates="role")
