"""This module includes database sessions."""

import settings

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_ENGINE = create_engine(settings.DATABASE_URL)
DATABASE_SESSION = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=DATABASE_ENGINE
    # TODO: pool_size
)
