# LOGIC 1: Import the Book class from book.py.
from book import Book
from exceptions import BookNotFoundError
from library import Library
from member import Member
from reports import Reports



# LOGIC 2: Create a Book object with its details.
book1 = Book(
    book_id=101,
    title="Python Basics",
    author="Guido van Rossum",
    total_copies=5
)

# LOGIC 3: Display the book details.
print("Book ID:", book1.book_id)
print("Title:", book1.title)
print("Author:", book1.author)
print("Total Copies:", book1.total_copies)
print("Available Copies:", book1.available_copies)

# LOGIC 4: Check whether the book is available.
if book1.is_available():
    print("Status: Book is available")
else:
    print("Status: Book is not available")

# Test the Member class.
from member import Member

# Create a member with valid details.
member1 = Member(
    member_id=1,
    name="Kartheek",
    email="kartheek@example.com"
)

# LOGIC 1: Display the member details.
print("Member Details:", member1)

# Test updating member details.
member1.update_details(name="Kartheek C")
print("Updated Name:", member1.name)

# Test saving and loading book data using JSON.
from storage import JSONStorage
from book import Book

book_storage = JSONStorage("data/books.json")

book1 = Book(
    book_id=1,
    title="Python Basics",
    author="John Smith",
    total_copies=5
)

book_data = [
    {
        "book_id": book1.book_id,
        "title": book1.title,
        "author": book1.author,
        "total_copies": book1.total_copies,
        "available_copies": book1.available_copies
    }
]

book_storage.save_data(book_data)
print("Saved books:", book_storage.load_data())

from book import Book
from library import Library

# LOGIC 1: Create a library and add a book.
library = Library()

book1 = Book(
    book_id=101,
    title="Python Basics",
    author="Guido van Rossum",
    total_copies=5
)

library.add_book(book1)
print("Added Book:", library.search_book(101))

# LOGIC 2: Update the book details.
library.update_book(101, title="Advanced Python")
print("Updated Book:", library.search_book(101))

# LOGIC 3: Delete the book from the library.
# try:
#     library.delete_book(101)
#     print("Book deleted successfully.")
# except ValueError as error:
#     print("Delete Error:", error)

# LOGIC 4: Display all books currently in the library.
print("Books in Library:")

for book in library.list_books():
    print(book)

# LOGIC 5: Test searching books by title or author.
print("Search Results:")
for book in library.search_books("Advanced"):
    print(book)

# LOGIC 6: Handle a search for a book that does not exist.
try:
    library.search_book(999)
except BookNotFoundError as error:
    print("Search Error:", error)

# LOGIC 7: Test borrowing and returning a book.
book1.borrow_book()
print("After borrowing:", book1)

book1.return_book()
print("After returning:", book1)

# LOGIC 8: Test deleting a book from the library.
#library.delete_book(101)
#print("Book deleted successfully.")

# LOGIC 9: Test book issue and late fine calculation.
from issue import Issue

issue1 = Issue(
    issue_id=1,
    book_id=101,
    member_id=1,
    issue_date="2026-10-20",
    due_date="2026-10-25"
)

# Record the return date.
issue1.return_book("2026-10-28")

# Display the issue details and fine.
print("Issue Details:", issue1)

# LOGIC 10: Test book input validation.
try:
    Book(
        book_id=102,
        title="",
        author="Test Author",
        total_copies=2
    )
except ValueError as error:
    print("Validation Error:", error)

# LOGIC 11: Test library member operations.
library = Library()

# Add a new member.
member1 = Member(
    member_id=1,
    name="Kartheek",
    email="kartheek@example.com"
)
library.add_member(member1)
print("Added Member:", library.search_member(1))

# Update the member details.
library.update_member(1, name="Kartheek C")
print("Updated Member:", library.search_member(1))

# List all registered members.
print("All Members:")
for member in library.list_members():
    print(member)

# Delete the member.
library.delete_member(1)
print("Members after deletion:", library.list_members())

# LOGIC 12: Test library reports.
reports = Reports()

# Display available books.
reports.available_books_report(library.list_books())

# Display borrowed books.
reports.borrowed_books_report(library.list_books())

# LOGIC 13: Test top borrowers and fine reports.

# Display the top borrowers.
reports.top_borrowers_report([issue1])

# Display the fine report.
reports.fine_report([issue1])

