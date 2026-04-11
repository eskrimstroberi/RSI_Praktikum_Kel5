from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.log import LogCreate, LogRead, LogUpdate, LogPatch
from app.services.log import LogService

router = APIRouter()


def get_log_service(session: Session = Depends(get_session)):
    return LogService(session)


@router.get("/", response_model=list[LogRead])
def get_logs(service: LogService = Depends(get_log_service)):
    return service.get_all()


@router.get("/{log_id}", response_model=LogRead, status_code=status.HTTP_200_OK)
def get_log(log_id: int, service: LogService = Depends(get_log_service)):
    log = service.get_by_id(log_id)
    if not log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Log not found"
        )
    return log


@router.post("/", response_model=LogRead, status_code=status.HTTP_201_CREATED)
def create_log(data: LogCreate, service: LogService = Depends(get_log_service)):
    return service.create(data)


@router.put("/{log_id}", response_model=LogRead, status_code=status.HTTP_200_OK)
def update_log(
    log_id: int, data: LogUpdate, service: LogService = Depends(get_log_service)
):
    log = service.put(log_id, data)
    if not log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Log not found"
        )
    return log


@router.patch("/{log_id}", response_model=LogRead, status_code=status.HTTP_200_OK)
def patch_log(
    log_id: int, data: LogPatch, service: LogService = Depends(get_log_service)
):
    log = service.patch(log_id, data)
    if not log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Log not found"
        )
    return log


@router.delete("/{log_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_log(log_id: int, service: LogService = Depends(get_log_service)):
    deleted = service.delete(log_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Log not found"
        )
    return None
