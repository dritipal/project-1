from database import Database
from services.book_service import BookService
from models.book import Book


def main():
    db = Database()
    book_service = BookService(db)

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")

            book = Book(book_id, title, author, isbn)
            book_service.add_book(book)

            print("Book added successfully.")

        elif choice == "2":
            books = book_service.get_books()

            for book in books:
                print(book)

        elif choice == "3":
            book_id = input("Enter Book ID: ")
            book_service.delete_book(book_id)
            print("Book deleted.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
