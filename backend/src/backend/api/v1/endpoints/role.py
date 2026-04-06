from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from backend.db.session import get_db
from backend.schemas.role import RoleCreate, RoleResponse
from backend.services.role import RoleService

router = APIRouter()

service = RoleService()


@router.get("/", response_model=list[RoleResponse], status_code=status.HTTP_200_OK)
def get_roles(db: Session = Depends(get_db)):
    return service.get_roles(db)


@router.get("/{role_id}", response_model=RoleResponse, status_code=status.HTTP_200_OK)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = service.get_role(db, role_id)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )
    return role


@router.post("/", response_model=RoleResponse, status_code=status.HTTP_201_CREATED)
def create_role(data: RoleCreate, db: Session = Depends(get_db)):
    return service.create_role(db, data)


@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_role(db, role_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Role not found"
        )
    return None