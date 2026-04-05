from pydantic import ConfigDict, BaseModel

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)