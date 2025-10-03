"""Custom exceptions for the foundations package."""


class FoundationsError(Exception):
    """Base exception for the package."""


class NotFoundError(FoundationsError):
    """Raised when an expected item is not found."""
