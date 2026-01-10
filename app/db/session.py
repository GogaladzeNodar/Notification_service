# app/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool
from typing import AsyncGenerator
from contextlib import asynccontextmanager

from app.config import settings

# Async setup
async_engine = create_async_engine(
    settings.async_database_url,
    future=True,
    echo=True,
    poolclass=NullPool
)
async_session = sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Sync setup
sync_engine = create_engine(
    settings.sync_database_url,
    future=True,
    echo=True
)
sync_session = sessionmaker(
    bind=sync_engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()

# Dependency for FastAPI
def get_db():
    db = sync_session()
    try:
        yield db
    finally:
        db.close()

# Async dependency
@asynccontextmanager
async def get_async_db():
    session = async_session()
    try:
        yield session
    finally:
        await session.close()
