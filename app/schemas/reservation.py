from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean, DateTime
from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel


class ReservationBase(BaseModel):
    is_active: Optional[bool] = True
    start_datetime: datetime
    end_datetime: datetime
    car_id: Optional[int] = None
    location_id: Optional[int] = None


class ReservationCreate(ReservationBase):
    pass


class ReservationUpdate(ReservationBase):
    is_active: Optional[bool] = None
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    user_id: Optional[int] = None
    car_id: Optional[int] = None
    location_id: Optional[int] = None


class Reservation(ReservationBase):
    id: int
    user_id: int
    car_id: int
    location_id: int
    reference_code: str
    price: float
    user_id: Optional[int] = None

    class Config:
        orm_mode = True

"""
class ReservationInDB(ReservationInDBBase):
    user: Optional["User"] = None
    car: Optional["Car"] = None
    location: Optional["Location"] = None
"""