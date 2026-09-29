from datetime import datetime


class IssueService:

    def __init__(self, database):
        self.database = database

    def issue_book(self, book_id, member_id):

        book = self.database.fetch_one(
            "SELECT * FROM books WHERE book_id = ?",
            (book_id,)
        )

        if not book:
            return False, "Book not found."

        if book["available"] == 0:
            return False, "Book is already issued."

        member = self.database.fetch_one(
            "SELECT * FROM members WHERE member_id = ?",
            (member_id,)
        )

        if not member:
            return False, "Member not found."

        issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.database.execute(
            """
            INSERT INTO issued_books
            (book_id, member_id, issue_date)
            VALUES (?, ?, ?)
            """,
            (book_id, member_id, issue_date)
        )

        self.database.execute(
            """
            UPDATE books
            SET available = 0
            WHERE book_id = ?
            """,
            (book_id,)
        )

        return True, "Book issued successfully."

    def return_book(self, book_id):

        record = self.database.fetch_one(
            """
            SELECT *
            FROM issued_books
            WHERE book_id = ?
            AND return_date IS NULL
            """,
            (book_id,)
        )

        if not record:
            return False, "This book is not currently issued."

        return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.database.execute(
            """
            UPDATE issued_books
            SET return_date = ?
            WHERE issue_id = ?
            """,
            (return_date, record["issue_id"])
        )

        self.database.execute(
            """
            UPDATE books
            SET available = 1
            WHERE book_id = ?
            """,
            (book_id,)
        )

        return True, "Book returned successfully."

    def get_issued_books(self):

        query = """
            SELECT
                issued_books.issue_id,
                books.book_id,
                books.title,
                members.member_id,
                members.name,
                issued_books.issue_date,
                issued_books.return_date
            FROM issued_books
            JOIN books
                ON issued_books.book_id = books.book_id
            JOIN members
                ON issued_books.member_id = members.member_id
            ORDER BY issued_books.issue_id
        """

        return self.database.fetch_all(query)

    def get_currently_issued_books(self):

        query = """
            SELECT
                issued_books.issue_id,
                books.book_id,
                books.title,
                members.member_id,
                members.name,
                issued_books.issue_date
            FROM issued_books
            JOIN books
                ON issued_books.book_id = books.book_id
            JOIN members
                ON issued_books.member_id = members.member_id
            WHERE issued_books.return_date IS NULL
            ORDER BY issued_books.issue_id
        """

        return self.database.fetch_all(query)
