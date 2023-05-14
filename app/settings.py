import os

from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()

# Auth
ACCESS_TOKEN_EXPIRE_MINUTES=10080

class Settings(BaseSettings):
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')
    db_name: str = os.getenv('DB_NAME')

    secret_key: str = os.getenv('SECRET_KEY')
    token_expire: int = ACCESS_TOKEN_EXPIRE_MINUTES
    
    class Config:
        env_file = ".env"