from datetime import datetime


class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.date_added = datetime.now().strftime("%Y-%m-%d")
        self.__pages_read = 0

    @property
    def pages_read(self):
        """Getter to retrieve the number of pages read"""
        return self.__pages_read

    @pages_read.setter
    def pages_read(self, value):
        """Setter to update pages read with validation"""
        if 0 <= value <= self.pages:
            self.__pages_read = value
        else:
            raise ValueError(f"Pages read must be between 0 and {self.pages}.")

    @property
    def reading_progress(self):
        """Calculate the reading progress as a percentage"""
        return (self.__pages_read / self.pages) * 100 if self.pages > 0 else 0

    @classmethod
    def from_dict(cls, data):
        """Factory method to create a Book object from a dictionary"""
        return cls(
            title=data["title"],
            author=data["author"],
            genre=data["genre"],
            pages=data["pages"],
        )

    @staticmethod
    def validate_data(data: dict) -> bool:
        required_keys = ["title", "author", "genre", "pages"]
        for key in required_keys:
            if key not in data:
                return False

        if not isinstance(data["title"], str) or not data["title"].strip():
            return False
        if not isinstance(data["author"], str) or not data["author"].strip():
            return False
        if not isinstance(data["genre"], str) or not data["genre"].strip():
            return False
        if not isinstance(data["pages"], int) or data["pages"] <= 0:
            return False

        return True

    def __str__(self):
        return f"{self.title} by {self.author} [{self.genre}] - {self.pages} pages"
