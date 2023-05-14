from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
#from uuid import UUID

from db.db_setup import Base
from .mixins import Timestamp

from .car import Car
from .location import Location


class Reservation(Timestamp, Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    reference_code = Column(String, unique=True, nullable=False, index=True)
    price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    car_id = Column(Integer, ForeignKey("cars.id"), nullable=True)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=True)
    
    user = relationship("User", back_populates="reservations", cascade="all,delete")
    car = relationship("Car", back_populates="reservations", cascade="all,delete")
    location = relationship("Location", back_populates="reservations", cascade="all,delete")
