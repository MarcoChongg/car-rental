from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.category import Category
from schemas.category import CategoryCreate

from settings import Settings


settings = Settings()


def create_category(db: Session, category: CategoryCreate):
    db_category= Category(name=category.name, price=category.price)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category