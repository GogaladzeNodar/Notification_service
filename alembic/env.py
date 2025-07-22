from logging.config import fileConfig

from sqlalchemy import pool
from alembic import context

# import your settings and sync engine
from app.config import settings
from sqlalchemy import create_engine

# import your Base and models
from app.db.session import Base
from app.models import notification, delivery_log, template

# Alembic Config object
config = context.config

# Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Provide metadata for autogenerate
target_metadata = Base.metadata

# use URL from your Pydantic settings
url = settings.sync_database_url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(url, poolclass=pool.NullPool, future=True)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()