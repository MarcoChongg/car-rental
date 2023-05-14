from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import enum
from models.location import Type

class LocationBase(BaseModel):
    name: str = Field(
        example="Sucursal Cancún"
    )
    location_type: Type = Field(
        example=Type.STORE,
        description="The type of the location"
    )

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int = Field(
        example="5"
    )

    class Config:
        orm_mode = True