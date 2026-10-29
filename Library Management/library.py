from book import Book
from exceptions import BookNotFoundError
from member import Member
from storage import JSONStorage

class Library:
    """Manage books in the library."""

    # LOGIC 1: Initialize an empty collection to store books.
    def __init__(self) -> None:
        self.books: dict[int, Book] = {}  # Store books using book ID
        self.members: dict[int, Member] = {}  # initialize a collection to store library members
        self.book_storage = JSONStorage("data/books.json")
        self.member_storage = JSONStorage("data/members.json")
        self.books_data = self.book_storage.load_data()
        self.members_data = self.member_storage.load_data()

        # LOGIC 2: Add a new book to the library.
    def add_book(self, book: Book) -> None:
        # Prevent duplicate book IDs.
        if book.book_id in self.books:
            raise ValueError("A book with this ID already exists.")

        # Store the book using its ID.
        self.books[book.book_id] = book
        self.book_storage.save_data([
            {
                "book_id": item.book_id,
                "title": item.title,
                "author": item.author,
                "total_copies": item.total_copies,
                "available_copies": item.available_copies
            }
            for item in self.books.values()
        ])

            # LOGIC 3: Register a new library member.
    def add_member(self, member: Member) -> None:
        # Prevent duplicate member IDs.
        if member.member_id in self.members:
            raise ValueError("A member with this ID already exists.")

        # Store the member using their ID.
        self.members[member.member_id] = member
        self.member_storage.save_data([
            {
                "member_id": item.member_id,
                "name": item.name,
                "email": item.email
            }
            for item in self.members.values()
        ])

            # LOGIC 4: Search for a member using their ID.
    def search_member(self, member_id: int) -> Member:
        # Check whether the member exists.
        if member_id not in self.members:
            raise ValueError("Member not found.")

        # Return the member details.
        return self.members[member_id]

        # LOGIC 5: Update the details of an existing member.
    def update_member(
        self,
        member_id: int,
        name: str | None = None,
        email: str | None = None
    ) -> None:
        # Find the member using their ID.
        member = self.search_member(member_id)

        # Update the provided member details.
        member.update_details(name=name, email=email)

            # LOGIC 6: Delete a member using their ID.
    def delete_member(self, member_id: int) -> None:
        # Check whether the member exists.
        self.search_member(member_id)

        # Remove the member from the collection.
        del self.members[member_id]

            # LOGIC 7: Display all registered library members.
    def list_members(self) -> list[Member]:
        # Return all registered members as a list.
        return list(self.members.values())

        # LOGIC 8: Search for a book using its ID.
    def search_book(self, book_id: int) -> Book:
        # Find the book and return its details.
        if book_id not in self.books:
            raise BookNotFoundError("Book not found.")

        return self.books[book_id] 

        # LOGIC 9: Update the details of an existing book.
    def update_book(
        self,
        book_id: int,
        title: str | None = None,
        author: str | None = None,
        total_copies: int | None = None
    ) -> None:
        
        # Find the book using its ID.
        book = self.search_book(book_id)

        # Update the provided book details.
        book.update_details(
            title=title,
            author=author,
            total_copies=total_copies
        )
        self.book_storage.save_data([
            {
                "book_id": item.book_id,
                "title": item.title,
                "author": item.author,
                "total_copies": item.total_copies,
                "available_copies": item.available_copies
            }
            for item in self.books.values()
        ])

        
        # LOGIC 10: Remove a book from the library using its ID.
    def delete_book(self, book_id: int) -> None:
        # Check whether the book exists.
        self.search_book(book_id)

        # Remove the book from the collection.
        del self.books[book_id]

        # LOGIC 11: Display all books in the library.
    def list_books(self) -> list[Book]:
        # Return all books as a list.
        return list(self.books.values())

        # LOGIC 12: Search books by title or author.
    def search_books(self, keyword: str) -> list[Book]:
        # Match the keyword without considering letter case.
        keyword = keyword.strip().lower()

        # Return books whose title or author contains the keyword.
        return [
            book
            for book in self.books.values()
            if keyword in book.title.lower()
            or keyword in book.author.lower()
        ]