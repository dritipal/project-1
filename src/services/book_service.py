class BookService:

    def __init__(self, database):
        self.database = database

    def add_book(self, book):
        try:
            query = """
                INSERT INTO books (title, author, isbn)
                VALUES (?, ?, ?)
            """

            self.database.execute(
                query,
                (book.title, book.author, book.isbn)
            )

            return True, "Book added successfully."

        except Exception as error:
            return False, f"Error: {error}"

    def get_all_books(self):
        query = """
            SELECT *
            FROM books
            ORDER BY book_id
        """

        return self.database.fetch_all(query)

    def get_available_books(self):
        query = """
            SELECT *
            FROM books
            WHERE available = 1
            ORDER BY book_id
        """

        return self.database.fetch_all(query)

    def search_books(self, keyword):
        query = """
            SELECT *
            FROM books
            WHERE title LIKE ?
               OR author LIKE ?
               OR isbn LIKE ?
        """

        search = f"%{keyword}%"

        return self.database.fetch_all(
            query,
            (search, search, search)
        )

    def delete_book(self, book_id):
        book = self.database.fetch_one(
            "SELECT * FROM books WHERE book_id = ?",
            (book_id,)
        )

        if not book:
            return False, "Book not found."

        if book["available"] == 0:
            return False, "Book is currently issued."

        self.database.execute(
            "DELETE FROM books WHERE book_id = ?",
            (book_id,)
        )

        return True, "Book deleted successfully."
