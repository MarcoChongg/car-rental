from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List
import enum

class CategoryBase(BaseModel):
    name: str = Field(
        example="Standard"
    )
    price: float = Field(
        example="200"
    )

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int = Field(
        example="5"
    )

    class Config:
        orm_mode = True
