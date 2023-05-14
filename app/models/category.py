import enum

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
#from uuid import UUID

from db.db_setup import Base
from .mixins import Timestamp


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    cars = relationship('Car', back_populates='category')