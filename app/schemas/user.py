from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
import enum

class UserBase(BaseModel):
    email: EmailStr = Field(
        example="myemail@email.com"
    )
    first_name: str = Field(
        example="Marco"
    )
    last_name: str = Field(
        example="Chong"
    )

class UserCreate(UserBase):
    password: str = Field(
        min_length=8,
        max_length=64,
        example="validpassword"
    )

class User(UserBase):
    id: int = Field(
        example="5"
    )

    class Config:
        orm_mode = True

class ChangePassword(BaseModel):
    current_password : str
    new_password : str
    confirm_password : str
