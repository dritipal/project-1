import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../src"
        )
    )
)

from database import Database
from models.book import Book
from services.book_service import BookService


def test_add_book():

    database = Database(":memory:")

    service = BookService(database)

    book = Book(
        "Python Programming",
        "John Smith",
        "TEST-001"
    )

    success, message = service.add_book(book)

    assert success is True

    books = service.get_all_books()

    assert len(books) == 1
    assert books[0]["title"] == "Python Programming"

    database.close()


if __name__ == "__main__":
    test_add_book()
    print("Book test passed.")
