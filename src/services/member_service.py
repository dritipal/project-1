class MemberService:

    def __init__(self, database):
        self.database = database

    def add_member(self, member):
        try:
            query = """
                INSERT INTO members (name, email, phone)
                VALUES (?, ?, ?)
            """

            self.database.execute(
                query,
                (member.name, member.email, member.phone)
            )

            return True, "Member registered successfully."

        except Exception as error:
            return False, f"Error: {error}"

    def get_all_members(self):
        query = """
            SELECT *
            FROM members
            ORDER BY member_id
        """

        return self.database.fetch_all(query)

    def search_members(self, keyword):
        query = """
            SELECT *
            FROM members
            WHERE name LIKE ?
               OR email LIKE ?
               OR phone LIKE ?
        """

        search = f"%{keyword}%"

        return self.database.fetch_all(
            query,
            (search, search, search)
        )

    def delete_member(self, member_id):
        member = self.database.fetch_one(
            "SELECT * FROM members WHERE member_id = ?",
            (member_id,)
        )

        if not member:
            return False, "Member not found."

        issued = self.database.fetch_one(
            """
            SELECT *
            FROM issued_books
            WHERE member_id = ?
            AND return_date IS NULL
            """,
            (member_id,)
        )

        if issued:
            return False, "Member has an issued book."

        self.database.execute(
            "DELETE FROM members WHERE member_id = ?",
            (member_id,)
        )

        return True, "Member deleted successfully."
