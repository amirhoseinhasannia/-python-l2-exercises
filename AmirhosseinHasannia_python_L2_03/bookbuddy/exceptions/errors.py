"""Custom exception classes for the BookBuddy application."""

class BookBuddyError(Exception):
    """Base class for all custom exceptions in BookBuddy."""
    pass


class BookNotFoundError(BookBuddyError):
    """Raised when a requested book cannot be found in the library."""
    pass


class InvalidLogError(BookBuddyError):
    """Raised when a reading log entry is invalid."""
    pass


class DataLoadError(BookBuddyError):
    """Raised when there is a problem loading data from storage."""
    pass
