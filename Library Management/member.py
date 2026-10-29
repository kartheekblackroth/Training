from validator import validate_id, validate_text, validate_email

class Member:
    """Represents a library member."""

    # LOGIC 1: Initialize member details when a new Member object is created.
    def __init__(
        self,
        member_id: int,
        name: str,
        email: str
    ) -> None:
            
        # Validate member details before storing them.
        validate_id(member_id)
        validate_text(name, "Name")
        validate_email(email)

        # Store the validated member details.
        self.member_id = member_id
        self.name = name
        self.email = email
    
    # LOGIC 2: Update member details when new values are provided.
    def update_details(
        self,
        name: str | None = None,
        email: str | None = None
    ) -> None:
        # Validate and update the name if a new name is provided.
        if name is not None:
            validate_text(name, "Name")
            self.name = name

        # Validate and update the email if a new email is provided.
        if email is not None:
            validate_email(email)
            self.email = email

    # LOGIC 3: Display member details in a readable format.
    def __str__(self) -> str:
        return (
            f"Member ID: {self.member_id}, "
            f"Name: {self.name}, "
            f"Email: {self.email}"
        )
    