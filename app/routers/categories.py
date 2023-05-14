from datetime import datetime, timedelta
from typing import List, Optional

import fastapi
from db.db_setup import async_get_db, get_db
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import (HTTPAuthorizationCredentials, HTTPBearer,
                              OAuth2PasswordBearer, OAuth2PasswordRequestForm)
from schemas.token import Token
from schemas.category import (Category, CategoryCreate)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from settings import Settings
from crud.category import (create_category)


security = HTTPBearer()


settings = Settings()
ACCESS_TOKEN_EXPIRE_MINUTES = settings.token_expire

router = fastapi.APIRouter()


@router.post("/categories/create", response_model=Category, status_code=201)
async def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db=db, category=category)