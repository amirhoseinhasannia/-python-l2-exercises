class ProgressManager:
    """Service to manage and calculate reading progress across multiple books."""

    @staticmethod
    def get_summary(books):
        """Generates a summary of progress for all provided books."""
        summary = []
        for book in books:
            summary.append(
                f"'{book.title}': {book.reading_progress:.1f}% completed."
            )
        return "\n".join(summary)

    @staticmethod
    def find_book_by_title(books, title):
        """Helper to find a specific book instance in a list by its title."""
        for book in books:
            if book.title.lower() == title.lower():
                return book
        return None
