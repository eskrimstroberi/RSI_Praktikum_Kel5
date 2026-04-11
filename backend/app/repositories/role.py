from sqlmodel import Session
from app.models.role import Role as RoleModel
from app.repositories.base import BaseRepository


class RoleRepository(BaseRepository[RoleModel]):
    def __init__(self, session: Session):
        super().__init__(model=RoleModel, session=session)
