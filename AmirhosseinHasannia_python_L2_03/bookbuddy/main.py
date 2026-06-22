import sys
from models.book import Book
from storage.data_handler import DataHandler
from exceptions.errors import BookNotFoundError

# Path to the data file
DATA_FILE = "books_data.json"


def show_menu():
    print("\nMain Menu:")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Log reading progress")
    print("4. View reading progress")
    print("5. Export book data")
    print("6. Import book data")
    print("7. Exit")
    return input("Enter your choice (1-7): ")


def input_positive_int(prompt):
    """Get a positive integer from the user."""
    while True:
        value = input(prompt)
        try:
            number = int(value)
            if number <= 0:
                print("Please enter a positive number.")
                continue
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def find_book_by_title(books, title):
    """Find a book by title or raise an error."""
    for book in books:
        if book.title.lower() == title.lower():
            return book
    raise BookNotFoundError(f"Book '{title}' not found.")


def main():
    # Load data at startup
    try:
        books = DataHandler.load_books_from_json(DATA_FILE)
    except Exception:
        books = []

    print("💻 BookBuddy CLI Mockup")
    print("📖 Welcome to BookBuddy!")
    print("Track your reading, log progress, and manage your personal library.")

    while True:
        choice = show_menu()

        if choice == "1":
            print("\nAdd a New Book")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            pages = input_positive_int("Enter total pages: ")

            new_book = Book(title, author, genre, pages)
            books.append(new_book)
            print(f"\n✅ Book '{title}' added successfully!")
            print("Returning to main menu...")

        elif choice == "2":
            print("\n📖 Your Library:")
            if not books:
                print("Your library is empty.")
            else:
                for i, book in enumerate(books, 1):
                    print(f"{i}. {book}")
            print("\nReturning to main menu...")

        elif choice == "3":
            title = input("Enter book title to log progress: ")
            try:
                book = find_book_by_title(books, title)
                progress = input_positive_int(f"Enter pages read for '{book.title}': ")
                book.pages_read = progress
                print("Progress updated!")
            except BookNotFoundError as e:
                print(f"Error: {e}")
            print("Returning to main menu...")

        elif choice == "4":
            title = input("Enter book title to view progress: ")
            try:
                book = find_book_by_title(books, title)
                print(f"Book: {book.title} | Progress: {book.reading_progress:.2f}%")
            except BookNotFoundError as e:
                print(f"Error: {e}")
            print("Returning to main menu...")

        elif choice == "5":
            DataHandler.save_books_to_json(books, DATA_FILE)
            print("Data exported successfully.")
            print("Returning to main menu...")

        elif choice == "6":
            books = DataHandler.load_books_from_json(DATA_FILE)
            print("Data imported successfully.")
            print("Returning to main menu...")

        elif choice == "7":
            DataHandler.save_books_to_json(books, DATA_FILE)
            print("Exiting... Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
