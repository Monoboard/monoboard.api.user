"""This module contains base orm model."""

from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()


class BaseModelMixin:
    """Class that includes base helpers operations."""

    @staticmethod
    def save(session: Session, *records: List[object], refresh: bool = True):
        """Commit changes to the database."""
        session.add(*records)
        session.commit()

        if refresh:
            session.refresh(*records)

        return records if len(records) > 1 else records[0]
