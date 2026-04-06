from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from backend.db.session import get_db
from backend.schemas.log import LogCreate, LogRead, LogUpdate, LogPatch
from backend.services.log import LogService

router = APIRouter()

service = LogService()


@router.get("/", response_model=list[LogRead], status_code=status.HTTP_200_OK)
def get_logs(db: Session = Depends(get_db)):
    return service.get_logs(db)


@router.get("/{log_id}", response_model=LogRead, status_code=status.HTTP_200_OK)
def get_log(log_id: int, db: Session = Depends(get_db)):
    log = service.get_log(db, log_id)
    if not log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Log not found"
        )
    return log


@router.post("/", response_model=LogRead, status_code=status.HTTP_201_CREATED)
def create_log(data: LogCreate, db: Session = Depends(get_db)):
    return service.create_log(db, data)


@router.put("/{log_id}", response_model=LogRead, status_code=status.HTTP_200_OK)
def update_log(
    log_id: int,
    data: LogUpdate,
    db: Session = Depends(get_db)
):
    log = service.update_log(db, log_id, data)
    if not log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Log not found"
        )
    return log


@router.patch("/{log_id}", response_model=LogRead, status_code=status.HTTP_200_OK)
def patch_log(
    log_id: int,
    data: LogPatch,
    db: Session = Depends(get_db)
):
    log = service.patch_log(db, log_id, data)
    if not log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Log not found"
        )
    return log


@router.delete("/{log_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_log(log_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_log(db, log_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Log not found"
        )
    return None