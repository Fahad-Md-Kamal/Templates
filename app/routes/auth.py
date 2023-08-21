
from datetime import timedelta
from typing import Annotated

from databases import Database
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth import ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user, create_access_token, get_password_hash
from app.database import get_database
from app.models import users
from app.schemas.auth_token_schema import Token, UserDB, UserRegister

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    database: Database = Depends(get_database)
):
    db_query = users.select().where(users.c.username==form_data.username)
    db_user = await database.fetch_one(db_query)
    user = UserDB(**db_user)
    user = authenticate_user(user, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": "access_token", "token_type": "bearer"}


@router.post("/register")
async def user_registration(
    user_data: UserRegister,
    database: Database = Depends(get_database)
):
    hashed_password = get_password_hash(user_data.password)
    user_data.password = hashed_password
    insert_query = users.insert().values(user_data.model_dump())
    user_id = await database.execute(insert_query)

    db_query = users.select().where(users.c.id==user_id)
    db_user = await database.fetch_one(db_query)
    user = UserDB(**db_user)
    print(user.model_dump())
    return {"access_token": user.model_dump(), "token_type": "bearer"}
