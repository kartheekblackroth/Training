class Reports:
    """Generate reports for the library."""

    # LOGIC 1: Display all books that are currently available.
    def available_books_report(self, books: list) -> None:
        """Print books that have available copies."""
        print("Available Books Report:")

        # Check each book's availability.
        for book in books:
            if book.is_available():
                print(book)

    
    # LOGIC 2: Display books that are currently borrowed.
    def borrowed_books_report(self, books: list) -> None:
        """Print books that have borrowed copies."""
        print("Borrowed Books Report:")

        # Check whether any copies have been borrowed.
        for book in books:
            borrowed_copies = book.total_copies - book.available_copies

            if borrowed_copies > 0:
                print(
                    f"Title: {book.title}, "
                    f"Borrowed Copies: {borrowed_copies}"
                )
    
    # LOGIC 3: Display fine details for books returned late.
    def fine_report(self, issues: list) -> None:
        """Print issues that have a fine."""
        print("Fine Report:")

        # Display only issues with a fine greater than zero.
        for issue in issues:
            if issue.fine > 0:
                print(
                    f"Issue ID: {issue.issue_id}, "
                    f"Member ID: {issue.member_id}, "
                    f"Fine: ₹{issue.fine:.2f}"
                )

    
    # LOGIC 4: Show members who borrowed the most books.
    def top_borrowers_report(self, issues: list) -> None:
        """Display the top borrowers based on issued books."""
        print("Top Borrowers Report:")

        # Count how many books each member has borrowed.
        borrower_counts: dict[int, int] = {}

        for issue in issues:
            member_id = issue.member_id
            borrower_counts[member_id] = (
                borrower_counts.get(member_id, 0) + 1
            )

        # Display borrowers from highest to lowest count.
        sorted_borrowers = sorted(
            borrower_counts.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for member_id, count in sorted_borrowers:
            print(f"Member ID: {member_id}, Books Borrowed: {count}")




