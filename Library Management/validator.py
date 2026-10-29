"""Input validation functions for the Library Management System."""

# LOGIC 1: Validate that an ID is a positive integer.
def validate_id(value: int) -> None:
    """Raise an error if the ID is not positive."""
    if value <= 0:
        raise ValueError("ID must be a positive integer.")


# LOGIC 2: Validate that a text field is not empty.
def validate_text(value: str, field_name: str) -> None:
    """Raise an error if the text field is empty."""
    if not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")


# LOGIC 3: Validate an email address.
def validate_email(email: str) -> None:
    """Raise an error if the email address is invalid."""
    if not email.strip() or "@" not in email:
        raise ValueError("Please provide a valid email address.")


# LOGIC 4: Validate that the number of copies is positive.
def validate_copies(copies: int) -> None:
    """Raise an error if the number of copies is not positive."""
    if copies <= 0:
        raise ValueError("Number of copies must be positive.")