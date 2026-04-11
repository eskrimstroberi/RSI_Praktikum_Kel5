from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.models.role import Role
from app.schemas.role import RoleCreate, RoleResponse
from app.services.role import RoleService

router = APIRouter()


def get_role_service(session: Session = Depends(get_session)):
    return RoleService(session)


@router.get("/", response_model=list[RoleResponse], status_code=status.HTTP_200_OK)
def get_roles(service: RoleService = Depends(get_role_service)):
    return service.get_all()


@router.get("/{role_id}", response_model=RoleResponse, status_code=status.HTTP_200_OK)
def get_role(role_id: int, service: RoleService = Depends(get_role_service)):
    role = service.get_by_id(role_id)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Role not found"
        )
    return role


@router.post("/", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_role(data: RoleCreate, service: RoleService = Depends(get_role_service)):
    return service.create(data)


@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(role_id: int, service: RoleService = Depends(get_role_service)):
    deleted = service.delete(role_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Role not found"
        )
    return None
