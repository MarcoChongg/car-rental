from datetime import datetime, timedelta
from typing import List, Optional

import fastapi
from db.db_setup import async_get_db, get_db
from fastapi import Depends, HTTPException, Request, status
from schemas.reservation import (Reservation,
                          ReservationCreate)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from settings import Settings
from crud.reservations import (create_reservation, get_reservations)
from crud.users import get_current_user_id
from fastapi.security import (HTTPAuthorizationCredentials, HTTPBearer,
                              OAuth2PasswordBearer, OAuth2PasswordRequestForm)

security = HTTPBearer()
router = fastapi.APIRouter()


@router.post("/reservations/create", response_model=Reservation, status_code=201)
async def create_new_reservation(reservation: ReservationCreate, db: Session = Depends(get_db), current_user_id= Depends(get_current_user_id)):
    return create_reservation(db=db, reservation=reservation, user_id = current_user_id)


@router.get("/reservations/list", response_model=List[Reservation])
async def read_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user_id= Depends(get_current_user_id)):
    reservations = get_reservations(db, skip=skip, limit=limit, current_user_id=current_user_id)
    return reservations
