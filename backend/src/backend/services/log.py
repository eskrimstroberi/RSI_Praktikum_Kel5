from sqlmodel import Session
from fastapi import HTTPException

from backend.models.log import Log as LogModel
from backend.schemas.log import LogCreate, LogUpdate, LogPatch


class LogService:

    def get_logs(self, db: Session):
        return db.query(LogModel).all()

    def get_log(self, db: Session, log_id: int):
        return db.get(LogModel, log_id)

    def create_log(self, db: Session, data: LogCreate):
        log = LogModel(**data.model_dump())
        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    def update_log(self, db: Session, log_id: int, data: LogUpdate):
        log = db.get(LogModel, log_id)
        if not log:
            return None

        for key, value in data.model_dump().items():
            setattr(log, key, value)

        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    def patch_log(self, db: Session, log_id: int, data: LogPatch):
        log = db.get(LogModel, log_id)
        if not log:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(log, key, value)

        db.add(log)
        db.commit()
        db.refresh(log)
        return log

    def delete_log(self, db: Session, log_id: int):
        log = db.get(LogModel, log_id)
        if not log:
            return False

        db.delete(log)
        db.commit()
        return True