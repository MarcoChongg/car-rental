from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List
import enum
from .category import Category

class CarBase(BaseModel):
    plate: str = Field(
        example="Standard"
    )
    color: str = Field(
        example="blue"
    )
    brand: str = Field(
        example="Toyota"
    )
    model: str = Field(
        example="Yaris"
    )
    year: str = Field(
        example="2020"
    )
    category_id: int = Field(
        example="1"
    )

    async def category(self):
        return await Category.get(id=self.category_id)


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int = Field(
        example="5"
    )

    class Config:
        orm_mode = True