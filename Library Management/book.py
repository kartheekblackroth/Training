from validator import validate_id, validate_text, validate_copies

class Book:
    """Represents a book in the library."""

    # LOGIC 1: Initialize book details when a new Book object is created.
    def __init__(
        self,
        book_id: int,
        title: str,
        author: str,
        total_copies: int = 1
    ) -> None:
        # Validate book details before storing them.
        validate_id(book_id)
        validate_text(title, "Title")
        validate_text(author, "Author")
        validate_copies(total_copies)

        # Store the basic details of the book.
        self.book_id = book_id
        self.title = title
        self.author = author

        # Initially, all copies are available for borrowing.
        self.total_copies = total_copies
        self.available_copies = total_copies

    # LOGIC 2: Check whether at least one copy is available.
    def is_available(self) -> bool:
        return self.available_copies > 0  # True if copies are available
    
    # LOGIC 3: Update book details without changing fields that were not provided.
    def update_details(
        self,
        title: str | None = None,
        author: str | None = None,
        total_copies: int | None = None
    ) -> None:
        # Update title only if a new title is provided.
        if title is not None:
            validate_text(title, "Title")
            self.title = title

        # Update author only if a new author is provided.
        if author is not None:
            validate_text(author, "Author")
            self.author = author

        # Update copies while keeping borrowed copies unchanged.
        if total_copies is not None:
            validate_copies(total_copies)
            borrowed_copies = self.total_copies - self.available_copies

            # Prevent total copies from going below borrowed copies.
            if total_copies < borrowed_copies:
                raise ValueError("Total copies cannot be less than borrowed copies.")

            self.total_copies = total_copies
            self.available_copies = total_copies - borrowed_copies

    
    # LOGIC 4: Display book details in a readable format.
    def __str__(self) -> str:
        return (
            f"Book ID: {self.book_id}, "
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Available: {self.available_copies}/{self.total_copies}"
        )

        # LOGIC 5: Reduce available copies when a book is borrowed.
    def borrow_book(self) -> None:
        # Prevent borrowing when no copies are available.
        if not self.is_available():
            raise ValueError("No copies available for borrowing.")

        self.available_copies -= 1

    # LOGIC 6: Increase available copies when a book is returned.
    def return_book(self) -> None:
        # Prevent returning more copies than were borrowed.
        if self.available_copies >= self.total_copies:
            raise ValueError("All copies are already available.")

        self.available_copies += 1


