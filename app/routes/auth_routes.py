from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db
from app.services.auth_services import create_access_token, verify_password_hash


router = APIRouter( tags=["AUTH"])

@router.post("/login", response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(detail="Invalid Credentials", status_code=status.HTTP_403_FORBIDDEN)
    if not verify_password_hash(user_credentials.password, user.password):
        raise HTTPException(detail="Invalid Credentials", status_code=status.HTTP_403_FORBIDDEN)
    
    access_token = create_access_token(data={"user_id":user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}
