"""This module includes custom errors."""


class BaseError(Exception):
    """Class that represents base error."""

    def __init__(self, message: str = None):
        """Initialize base custom error."""
        super().__init__()
        self.message = message

    def __str__(self):
        """Return message for str method."""
        return f"{self.__class__.__name__}: {self.message}"

    def __repr__(self):
        """Return message for repr method."""
        return f"{self.__class__.__name__}: {self.message}"


class TokenError(BaseError):
    """Class that represents errors caused on interaction with auth token."""


class RetryError(BaseError):
    """Class that represents errors caused for retry."""


class DatabaseError(BaseError):
    """Class that represents errors caused on interaction with database."""


class DBNoResultFoundError(DatabaseError):
    """Class that represents errors caused on not existing entity."""

    def __init__(self, message: str = None, search_fields: dict = None):
        """Initialize DBNoResultFoundError custom error."""
        super().__init__()
        self.message = message
        self.search_fields = search_fields


class DBUniqueViolationError(DatabaseError):
    """Class that represents errors caused on duplication."""

    def __init__(self, message: str = None, duplicate_fields: dict = None):
        """Initialize DBUniqueViolationError custom error."""
        super().__init__()
        self.message = message
        self.duplicate_fields = duplicate_fields
