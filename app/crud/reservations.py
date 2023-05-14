from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.reservation import Reservation
from models.category import Category
from models.location import Location, Type
from models.car import Car
from schemas.reservation import ReservationCreate

from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from passlib.context import CryptContext

from schemas.token import TokenData
from settings import Settings


import string
import random

from pytz import timezone
from .users import get_current_user
 
N=7

settings = Settings()

def generate_reference_code():
    rand = ''.join(random.choices(string.ascii_letters, k=N))
    return rand


def create_reservation(db: Session, reservation: ReservationCreate, user_id):
    car = db.query(Car).get(reservation.car_id)
    if not car:
        raise HTTPException(
            status_code=404, detail=f"Car with id {reservation.car_id} does not exist in the database."
        )

    location = db.query(Location).get(reservation.location_id)
    if not location:
        raise HTTPException(
            status_code=404, detail=f"Location with id {reservation.location_id} does not exist in the database."
        )
    location_price = 150 if location.location_type == Type.AIRPORT else 0

    server_tz = timezone('Mexico/General')
    start_datetime = reservation.start_datetime

    if reservation.start_datetime < datetime.now(server_tz):
        raise HTTPException(
            status_code=404, detail="Start datetime cannot be in the past."
        )
    if reservation.end_datetime < reservation.start_datetime:
        raise HTTPException(
            status_code=404, detail="End datetime cannot be before start datetime."
        )
        

    #user = db.query(User).get(reservation.user_id)
    #token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJteWVtYWlsMkBlbWFpbC5jb20iLCJleHAiOjE2ODM2ODg5NDV9.fSF2DVWioWmWSzNH6f-ScSD2_dg5-vLLI_nLg6Hta50"

    category_price = db.query(Category.price).join(Car).filter(Car.id == reservation.car_id).scalar()

    db_reservation = Reservation(
        start_datetime=reservation.start_datetime,
        end_datetime=reservation.end_datetime,
        user_id=user_id,
        car_id=reservation.car_id,
        location_id=reservation.location_id,
        reference_code=generate_reference_code(),
        price=category_price + location_price,
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def get_reservations(db: Session, current_user_id: int, skip: int = 0, limit: int = 100, ):
    return db.query(Reservation).filter(Reservation.user_id == current_user_id).offset(skip).limit(limit).all()