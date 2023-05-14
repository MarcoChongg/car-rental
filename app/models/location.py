import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
#from uuid import UUID

from db.db_setup import Base
from .mixins import Timestamp


class Type(enum.IntEnum):
    STORE: int = 1
    AIRPORT: int = 2


class Location(Timestamp, Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default=True)
    location_type: int = Column(Integer, nullable=False, default=("1"))
    is_active = Column(Boolean, default=True)

    reservations = relationship('Reservation', back_populates='location', lazy='dynamic', cascade="all,delete")