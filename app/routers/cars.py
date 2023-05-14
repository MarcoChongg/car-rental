from datetime import datetime, timedelta
from typing import List, Optional

import fastapi
from db.db_setup import async_get_db, get_db
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import (HTTPAuthorizationCredentials, HTTPBearer,
                              OAuth2PasswordBearer, OAuth2PasswordRequestForm)
from schemas.token import Token
from schemas.car import (Car, CarCreate)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from settings import Settings
from crud.cars import (create_car)


security = HTTPBearer()


settings = Settings()
ACCESS_TOKEN_EXPIRE_MINUTES = settings.token_expire

router = fastapi.APIRouter()


@router.post("/cars/create", response_model=Car, status_code=201)
async def create_new_car(car: CarCreate, db: Session = Depends(get_db)):
    return create_car(db=db, car=car)