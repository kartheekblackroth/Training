class Issue:
    """Represents a book issued to a library member."""

    # LOGIC 1: Initialize the details of an issued book.
    def __init__(
        self,
        issue_id: int,
        book_id: int,
        member_id: int,
        issue_date: str,
        due_date: str
    ) -> None:
        # Store the issue and book details.
        self.issue_id = issue_id
        self.book_id = book_id
        self.member_id = member_id
        self.issue_date = issue_date
        self.due_date = due_date

        # Initially, the book has not been returned.
        self.return_date: str | None = None
        self.fine: float = 0.0

        # LOGIC 2: Record the book return and calculate any late fine.
    def return_book(self, return_date: str) -> None:
        """Record the return date and calculate the fine."""

        from datetime import date

        # Convert the date strings into date objects.
        due = date.fromisoformat(self.due_date)
        returned = date.fromisoformat(return_date)

        # Calculate a fine of ₹5 for each day after the due date.
        late_days = max(0, (returned - due).days)
        self.fine = late_days * 5

        # Store the return date.
        self.return_date = return_date

    # LOGIC 3: Display issue details in a readable format.
    def __str__(self) -> str:
        return (
            f"Issue ID: {self.issue_id}, "
            f"Book ID: {self.book_id}, "
            f"Member ID: {self.member_id}, "
            f"Issue Date: {self.issue_date}, "
            f"Due Date: {self.due_date}, "
            f"Return Date: {self.return_date}, "
            f"Fine: ₹{self.fine:.2f}"
        )