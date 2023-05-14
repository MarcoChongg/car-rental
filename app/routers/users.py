from datetime import datetime, timedelta
from typing import List, Optional, Annotated

import fastapi
from db.db_setup import async_get_db, get_db
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import (HTTPAuthorizationCredentials, HTTPBearer,
                              OAuth2PasswordBearer, OAuth2PasswordRequestForm)
from schemas.token import Token
from schemas.user import (ChangePassword, User,
                          UserCreate)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from settings import Settings
from crud.users import (authenticate_user, change_password,
                         create_access_token, create_user, get_current_user,
                         get_password_hash, get_user,
                         get_user_by_email, get_users,
                         verify_password, get_current_user_id)

security = HTTPBearer()


settings = Settings()
ACCESS_TOKEN_EXPIRE_MINUTES = settings.token_expire

router = fastapi.APIRouter()

users = []

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")


@router.get("/users/list", response_model=List[User])
async def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users/create", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Email is already registered"
        )
    return create_user(db=db, user=user)


@router.get("/users/me")
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_user_id)], 
    ):
    return current_user


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(async_get_db)):
    db_user = await get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print(form_data)
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/users/change_password")
def change_pass(request: Request, change_pass:ChangePassword, db: Session = Depends(get_db), auth: HTTPAuthorizationCredentials = Depends(security)):
    #token = request.headers["Authorization"]
    token = auth.credentials
    user = get_current_user(db, token)
    if not user:
        False
    hashed_password = user.hashed_password
    if not verify_password(change_pass.current_password, hashed_password):
        return False
    if not change_password(db, change_pass.new_password, change_pass.confirm_password, user):
        return False
    return {"message": "success"}

