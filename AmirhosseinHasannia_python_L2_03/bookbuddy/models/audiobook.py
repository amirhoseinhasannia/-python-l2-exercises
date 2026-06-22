from models.book import Book


class AudioBook(Book):
    def __init__(self, title, author, genre, duration_minutes, narrator):
        """
        For compatibility with Book:
        - pages  -> duration_minutes (total minutes)
        - __pages_read -> minutes listened
        """
        # We pass duration_minutes as pages to reuse progress logic
        super().__init__(title, author, genre, pages=duration_minutes)

        # Additional attributes specific to AudioBook
        self.duration_minutes = duration_minutes
        self.narrator = narrator

    @property
    def minutes_listened(self):
        """Alias for pages_read to make the intent clearer for audio books"""
        return self.pages_read

    @minutes_listened.setter
    def minutes_listened(self, value):
        """Setter that maps minutes listened to pages_read validation logic"""
        self.pages_read = value

    def __str__(self):
        """Human-readable string representation of an AudioBook"""
        return (
            f"[AudioBook] '{self.title}' by {self.author} "
            f"[{self.genre}] - {self.duration_minutes} minutes, "
            f"narrated by {self.narrator}"
        )

    @classmethod
    def from_dict(cls, data):
        """
        Factory method to create an AudioBook object from a dictionary.
        Expected keys: title, author, genre, duration_minutes, narrator
        """
        return cls(
            title=data["title"],
            author=data["author"],
            genre=data["genre"],
            duration_minutes=data["duration_minutes"],
            narrator=data["narrator"],
        )

    @staticmethod
    def validate_data(data):
        """
        Validate input data before creating an AudioBook instance.
        Extends the base Book validation with AudioBook-specific checks.
        """
        # For audio books we still reuse Book.validate_data,
        # but we treat duration as pages in this context.
        base_required = ["title", "author", "genre"]
        for key in base_required:
            if key not in data or not data[key]:
                return False

        # Validate duration_minutes
        if "duration_minutes" not in data or data["duration_minutes"] <= 0:
            return False

        # Validate narrator
        if "narrator" not in data or not data["narrator"]:
            return False

        return True
