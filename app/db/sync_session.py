# app/database/sync_session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

SYNC_DATABASE_URL = settings.sync_database_url  # sync URL in .env

sync_engine = create_engine(SYNC_DATABASE_URL, future=True)
SyncSessionLocal = sessionmaker(bind=sync_engine, autoflush=False, autocommit=False)

Base = declarative_base()
