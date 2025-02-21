import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):

    # App
    APP_NAME:  str = os.environ.get("APP_NAME", "FastApi")
    DEBUG: bool = bool(os.environ.get("DEBUG", False))

    # PostgreSQL Database Config
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")  
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")  
    POSTGRES_SERVER: str = os.environ.get("POSTGRES_SERVER")  
    POSTGRES_PORT: int = int(os.environ.get("POSTGRES_PORT"))  
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")  
    DATABASE_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # JWT
    JWT_SECRET: str = os.environ.get("JWT_SECRET")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get("REFRESH_TOKEN_EXPIRE_MINUTES"))
    
    # APP SECRET
    SECRET_KEY: str = os.environ.get("SECRET_KEY")

    # SMTP 
    SMTP_EMAIL_CURRENT: str = os.environ.get('SMTP_EMAIL_CURRENT', 'test@gmail.com')
    SMTP_EMAIL_PASSWORD: str = os.environ.get('SMTP_EMAIL_PASSWORD', 'test@password')
    SMTP_EMAIL_PORT: int = os.environ.get('SMTP_EMAIL_PORT', 1025)
    SMTP_SERVER: str = os.environ.get('SMTP_SERVER', 'smtp')
    SMTP_USER: str = os.environ.get('SMTP_USER', 'pet')
    SMTP_PASS: str = os.environ.get('SMTP_PASS', 'pet$$123')
    SMTP_MAIL: str = os.environ.get('SMTP_MAIL', 'pet@gmail.com')
    SMTP_PORT: int = os.environ.get('SMTP_PORT', 1025)
    SMTP_TLS: bool = os.environ.get('SMTP_TLS', False)

    # FRONTEND
    FRONTEND_HOST: str = os.environ.get('FRONTEND_HOST', 'http://localhost:3000')

    # BACKEND
    BACKEND_HOST: str = os.environ.get('BACKEND_HOST')

    # ADMIN TEST
    FIRST_ADMIN_EMAIL: str = os.environ.get('FIRST_ADMIN_EMAIL')
    FIRST_ADMIN_PASSWORD: str = os.environ.get('FIRST_ADMIN_PASSWORD')
    FIRST_ADMIN_ACCOUNT_NAME: str = os.environ.get('FIRST_ADMIN_ACCOUNT_NAME')
    FIRST_ADMIN_ACCOUNT_LASTNAME: str = os.environ.get('FIRST_ADMIN_ACCOUNT_LASTNAME')

    # S3 BUCKET
    BUCKET_REGION: str = os.environ.get('BUCKET_REGION')
    BUCKET_NAME: str = os.environ.get('BUCKET_NAME')
    BUCKET_KEY: str = os.environ.get('BUCKET_KEY')
    BUCKET_SECRET: str = os.environ.get('BUCKET_SECRET')

    # MERCADO PAGO
    ACCESS_KEY_MERCADO_PAGO: str = os.environ.get('ACCESS_KEY_MERCADO_PAGO')
    MERCADOPAGO_WEBHOOK_SECRET: str = os.environ.get('MERCADOPAGO_WEBHOOK_SECRET')

    # GOOGLE MAPS
    GOOGLE_MAPS_KEY: str = os.environ.get('GOOGLE_MAPS_KEY')


@lru_cache()
def get_settings() -> Settings:
    return Settings()