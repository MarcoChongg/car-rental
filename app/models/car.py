import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from db.db_setup import Base
from .mixins import Timestamp

from .category import Category


class Car(Timestamp, Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    plate = Column(String(100), unique=True, index=True, nullable=False)
    color = Column(String)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    category = relationship("Category", back_populates="cars", cascade="all,delete")
    reservations = relationship('Reservation', back_populates='car', lazy='dynamic', cascade="all,delete")
