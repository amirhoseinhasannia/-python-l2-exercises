from datetime import datetime


class ReadingLog:
    """Class to represent a single reading session log."""

    def __init__(self, book_title, pages_read, session_date=None):
        self.book_title = book_title
        self.pages_read = pages_read
        # Default to current date if none provided
        self.session_date = session_date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (
            f"[{self.session_date}] Read {self.pages_read} pages of '{self.book_title}'"
        )
