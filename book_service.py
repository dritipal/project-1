class BookService:

    def __init__(self, database):
        self.database = database

    def add_book(self, book):
        query = """
        INSERT INTO books (book_id, title, author, isbn)
        VALUES (?, ?, ?, ?)
        """
        self.database.execute(
            query,
            (book.book_id, book.title, book.author, book.isbn)
        )

    def get_books(self):
        return self.database.execute(
            "SELECT * FROM books"
        ).fetchall()

    def delete_book(self, book_id):
        self.database.execute(
            "DELETE FROM books WHERE book_id = ?",
            (book_id,)
        )
