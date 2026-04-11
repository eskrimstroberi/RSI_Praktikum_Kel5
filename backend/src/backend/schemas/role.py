from sqlmodel import SQLModel
from sqlmodel.main import SQLModelConfig


class RoleBase(SQLModel):
    name: str

    model_config: SQLModelConfig = SQLModelConfig(from_attributes=True)


class RoleCreate(RoleBase):
    pass


class RoleResponse(RoleBase):
    id: int

