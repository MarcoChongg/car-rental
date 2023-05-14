from fastapi import FastAPI

from routers import users, categories, cars, locations, reservations, templates
from db.db_setup import engine
from models import user, category, car, location, reservation

#user.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Car Rental FASTAPI",
    description="Car Rental API",
    version="0.0.1",
    contact={
        "name": "Marco",
        "email": "marco@mail.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    responses={418: {"description": "I'm a teapot"}},
)
app.include_router(
    categories.router,
    prefix="/categories",
    tags=["categories"],
    responses={418: {"description": "I'm a teapot"}},
)
app.include_router(
    cars.router,
    prefix="/cars",
    tags=["cars"],
    responses={418: {"description": "I'm a teapot"}},
)
app.include_router(
    locations.router,
    prefix="/locations",
    tags=["locations"],
    responses={418: {"description": "I'm a teapot"}},
)
#app.include_router(reservations.router)
app.include_router(
    reservations.router,
    prefix="/reservations",
    tags=["reservations"],
    responses={418: {"description": "I'm a teapot"}},
)

app.include_router(
    templates.router,
    tags=["templates"]
)
