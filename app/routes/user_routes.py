from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db
from app.services.auth_services import create_password_hash
from app.utils.pagination import pagination


router = APIRouter(prefix="/users", tags=["USERS"])

@router.post("/", status_code=status.HTTP_201_CREATED, 
    response_model=schemas.UserResponse)
async def register_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    user.password = create_password_hash(user.password)
    new_user = models.Users(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=list[schemas.UserResponse])
async def get_all_users(
    pagination: tuple[int, int] = Depends(pagination), 
    db: Session = Depends(get_db)):
    skip, limit = pagination
    users = db.query(models.Users).offset(skip).limit(limit).all()
    if len(users) <= 0:
        raise HTTPException(
            detail="No Post Exists", status_code=status.HTTP_404_NOT_FOUND
        )
    return users


@router.get("/{user_id}", response_model=schemas.UserResponse)
async def get_user_detail(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == user_id).first()
    if not user:
        raise HTTPException(detail="Not-Found", status_code=status.HTTP_404_NOT_FOUND)
    return user
