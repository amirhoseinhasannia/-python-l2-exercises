from models.book import Book


class EBook(Book):
    def __init__(self, title, author, genre, pages, file_size_mb, file_format):
        # Initialize base Book attributes
        super().__init__(title, author, genre, pages)

        # Additional attributes specific to EBook
        self.file_size_mb = file_size_mb
        self.file_format = file_format

    def __str__(self):
        """Human-readable string representation of an EBook"""
        return (
            f"[E-Book] '{self.title}' by {self.author} "
            f"[{self.genre}] - {self.pages} pages, "
            f"{self.file_size_mb} MB, format: {self.file_format}"
        )

    @classmethod
    def from_dict(cls, data):
        """
        Factory method to create an EBook object from a dictionary.
        Expected keys: title, author, genre, pages, file_size_mb, file_format
        """
        return cls(
            title=data["title"],
            author=data["author"],
            genre=data["genre"],
            pages=data["pages"],
            file_size_mb=data["file_size_mb"],
            file_format=data["file_format"],
        )

    @staticmethod
    def validate_data(data):
        """
        Validate input data before creating an EBook instance.
        Extends the base Book validation with EBook-specific checks.
        """
        # First, validate the common Book fields
        if not Book.validate_data(data):
            return False

        # Validate EBook-specific fields
        if "file_size_mb" not in data or data["file_size_mb"] <= 0:
            return False
        if "file_format" not in data or not data["file_format"]:
            return False

        return True
