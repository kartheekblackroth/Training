"""Custom exceptions for the Library Management System."""


# LOGIC 1: Handle errors when a book is not found.
class BookNotFoundError(Exception):
    """Raised when a requested book does not exist."""
    pass


# LOGIC 2: Handle errors when a member is not found.
class MemberNotFoundError(Exception):
    """Raised when a requested member does not exist."""
    pass


# LOGIC 3: Handle errors when a book is unavailable.
class BookNotAvailableError(Exception):
    """Raised when no copies of a book are available."""
    pass


# LOGIC 4: Handle errors when a member is not eligible.
class InvalidMemberError(Exception):
    """Raised when a member is not eligible to borrow books."""
    pass