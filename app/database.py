from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from typing import Generator

from app.settings import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URI,
                       pool_pre_ping=True,
                       pool_recycle=3600,
                       pool_size=20,
                       max_overflow=0)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_session() -> Generator:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()