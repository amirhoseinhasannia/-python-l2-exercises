import json
from pathlib import Path

from models.book import Book
from models.ebook import EBook
from models.audiobook import AudioBook


class DataHandler:
    """
    Handles saving and loading book data to/from JSON files.
    """

    @staticmethod
    def _book_to_dict(book):
        """Convert a Book/EBook/AudioBook instance to a serializable dictionary."""
        base = {
            "type": book.__class__.__name__,  # Book / EBook / AudioBook
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "pages": book.pages,
            "date_added": book.date_added,
            "pages_read": book.pages_read,
        }

        # Add specific fields based on type
        if isinstance(book, EBook):
            base["file_size_mb"] = book.file_size_mb
            base["file_format"] = book.file_format
        elif isinstance(book, AudioBook):
            base["duration_minutes"] = book.duration_minutes
            base["narrator"] = book.narrator

        return base

    @staticmethod
    def _dict_to_book(data):
        """Create a Book/EBook/AudioBook instance from a dictionary."""
        book_type = data.get("type", "Book")

        if book_type == "EBook":
            book = EBook(
                title=data["title"],
                author=data["author"],
                genre=data["genre"],
                pages=data["pages"],
                file_size_mb=data["file_size_mb"],
                file_format=data["file_format"],
            )
        elif book_type == "AudioBook":
            book = AudioBook(
                title=data["title"],
                author=data["author"],
                genre=data["genre"],
                duration_minutes=data["duration_minutes"],
                narrator=data["narrator"],
            )
        else:
            book = Book(
                title=data["title"],
                author=data["author"],
                genre=data["genre"],
                pages=data["pages"],
            )

        # Restore progress if available
        pages_read = data.get("pages_read")
        if pages_read is not None:
            book.pages_read = pages_read

        return book

    @classmethod
    def save_books_to_json(cls, books, file_path):
        """
        Save a list of book objects to a JSON file.
        :param books: list of Book/EBook/AudioBook instances
        :param file_path: path to JSON file (string or Path)
        """
        file_path = Path(file_path)
        data = [cls._book_to_dict(book) for book in books]

        with file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @classmethod
    def load_books_from_json(cls, file_path):
        """
        Load books from a JSON file and return a list of instances.
        :param file_path: path to JSON file (string or Path)
        :return: list of Book/EBook/AudioBook instances
        """
        file_path = Path(file_path)
        if not file_path.exists():
            return []  # No file yet -> empty list

        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        books = [cls._dict_to_book(item) for item in data]
        return books
