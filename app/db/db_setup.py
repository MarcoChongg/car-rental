from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import Settings

settings = Settings()

db_user = settings.db_user
db_pass = settings.db_pass
db_name = settings.db_name
db_host = settings.db_host
db_port = settings.db_port

db_url = db_user + ":" + db_pass + "@" + db_host + ":" + db_port + "/" + db_name

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://" + db_url
ASYNC_SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://" + db_url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True, echo=True
)
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)
AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()