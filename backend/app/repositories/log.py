from sqlmodel import Session
from app.models.log import Log as LogModel
from app.repositories.base import BaseRepository


class LogRepository(BaseRepository[LogModel]):
    def __init__(self, session: Session):
        super().__init__(model=LogModel, session=session)
