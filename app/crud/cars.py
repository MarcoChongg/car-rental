from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.car import Car, Category
from schemas.car import CarCreate

from settings import Settings


settings = Settings()


def create_car(db: Session, car: CarCreate):
    category = db.query(Category).filter(Category.id == car.category_id).first()
    db_car= Car(plate=car.plate, color=car.color, brand=car.brand, year=car.year, model=car.model, category=category)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car