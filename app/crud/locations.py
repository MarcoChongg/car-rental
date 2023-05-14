from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.location import Location, Type
from schemas.location import LocationCreate

from settings import Settings


settings = Settings()


def create_location(db: Session, location: LocationCreate):
    db_location= Location(name=location.name, location_type=location.location_type)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location