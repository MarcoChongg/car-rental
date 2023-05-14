import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from db.db_setup import Base
from .mixins import Timestamp

from .reservation import Reservation
from .billing_data import BillingData

'''
class Role(enum.IntEnum):
    DEV: int = 1
    USER: int = 2
    ADMIN: int = 3
'''

class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    #role: int = Column(Integer, nullable=False, default=("2"))

    reservations = relationship('Reservation', back_populates='user', lazy='dynamic', cascade="all,delete")
    billing_data = relationship("BillingData", back_populates="user", uselist=False, cascade="all,delete")

