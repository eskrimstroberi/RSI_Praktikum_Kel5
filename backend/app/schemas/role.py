from sqlmodel import SQLModel
from sqlmodel.main import SQLModelConfig
from app.models.enums import RoleName


class RoleBase(SQLModel):
    name: RoleName

    model_config: SQLModelConfig = SQLModelConfig(from_attributes=True)


class RoleCreate(RoleBase):
    pass


class RoleResponse(RoleBase):
    id: int
