from database import Database

from models.book import Book
from models.member import Member

from services.book_service import BookService
from services.member_service import MemberService
from services.issue_service import IssueService

from utils.validators import (
    get_non_empty_input,
    get_integer_input,
    get_email_input
)


def print_line():
    print("=" * 60)


def display_books(books):
    if not books:
        print("No books found.")
        return

    print_line()
    print(
        f"{'ID':<5}"
        f"{'TITLE':<25}"
        f"{'AUTHOR':<20}"
        f"{'STATUS':<10}"
    )
    print_line()

    for book in books:
        status = "Available" if book["available"] else "Issued"

        title = book["title"][:23]
        author = book["author"][:18]

        print(
            f"{book['book_id']:<5}"
            f"{title:<25}"
            f"{author:<20}"
            f"{status:<10}"
        )

    print_line()


def display_members(members):
    if not members:
        print("No members found.")
        return

    print_line()

    print(
        f"{'ID':<5}"
        f"{'NAME':<25}"
        f"{'EMAIL':<30}"
        f"{'PHONE':<15}"
    )

    print_line()

    for member in members:

        name = member["name"][:23]
        email = member["email"][:28]
        phone = member["phone"] or ""

        print(
            f"{member['member_id']:<5}"
            f"{name:<25}"
            f"{email:<30}"
            f"{phone:<15}"
        )

    print_line()


def display_issued_books(records):

    if not records:
        print("No issued books found.")
        return

    print_line()

    print(
        f"{'ID':<5}"
        f"{'BOOK':<25}"
        f"{'MEMBER':<20}"
        f"{'ISSUED DATE':<20}"
    )

    print_line()

    for record in records:

        title = record["title"][:23]
        member = record["name"][:18]

        print(
            f"{record['book_id']:<5}"
            f"{title:<25}"
            f"{member:<20}"
            f"{record['issue_date']:<20}"
        )

    print_line()


def add_book(book_service):

    print("\n--- Add Book ---")

    title = get_non_empty_input("Enter book title: ")
    author = get_non_empty_input("Enter author name: ")
    isbn = get_non_empty_input("Enter ISBN: ")

    book = Book(
        title,
        author,
        isbn
    )

    success, message = book_service.add_book(book)

    print(message)


def view_books(book_service):

    print("\n--- All Books ---")

    books = book_service.get_all_books()

    display_books(books)


def search_books(book_service):

    print("\n--- Search Book ---")

    keyword = get_non_empty_input(
        "Enter title, author or ISBN: "
    )

    books = book_service.search_books(keyword)

    display_books(books)


def delete_book(book_service):

    print("\n--- Delete Book ---")

    book_id = get_integer_input(
        "Enter book ID: "
    )

    success, message = book_service.delete_book(book_id)

    print(message)


def add_member(member_service):

    print("\n--- Register Member ---")

    name = get_non_empty_input(
        "Enter member name: "
    )

    email = get_email_input(
        "Enter email: "
    )

    phone = get_non_empty_input(
        "Enter phone number: "
    )

    member = Member(
        name,
        email,
        phone
    )

    success, message = member_service.add_member(member)

    print(message)


def view_members(member_service):

    print("\n--- All Members ---")

    members = member_service.get_all_members()

    display_members(members)


def search_members(member_service):

    print("\n--- Search Member ---")

    keyword = get_non_empty_input(
        "Enter name, email or phone: "
    )

    members = member_service.search_members(keyword)

    display_members(members)


def delete_member(member_service):

    print("\n--- Delete Member ---")

    member_id = get_integer_input(
        "Enter member ID: "
    )

    success, message = member_service.delete_member(member_id)

    print(message)


def issue_book(issue_service):

    print("\n--- Issue Book ---")

    book_id = get_integer_input(
        "Enter book ID: "
    )

    member_id = get_integer_input(
        "Enter member ID: "
    )

    success, message = issue_service.issue_book(
        book_id,
        member_id
    )

    print(message)


def return_book(issue_service):

    print("\n--- Return Book ---")

    book_id = get_integer_input(
        "Enter book ID: "
    )

    success, message = issue_service.return_book(
        book_id
    )

    print(message)


def view_issued_books(issue_service):

    print("\n--- Currently Issued Books ---")

    records = issue_service.get_currently_issued_books()

    display_issued_books(records)


def main():

    database = Database()

    book_service = BookService(database)
    member_service = MemberService(database)
    issue_service = IssueService(database)

    while True:

        print()
        print_line()

        print("       LIBRARY MANAGEMENT SYSTEM")

        print_line()

        print("1.  Add Book")
        print("2.  View All Books")
        print("3.  Search Book")
        print("4.  Delete Book")
        print()
        print("5.  Register Member")
        print("6.  View All Members")
        print("7.  Search Member")
        print("8.  Delete Member")
        print()
        print("9.  Issue Book")
        print("10. Return Book")
        print("11. View Issued Books")
        print()
        print("0.  Exit")

        print_line()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_book(book_service)

        elif choice == "2":

            view_books(book_service)

        elif choice == "3":

            search_books(book_service)

        elif choice == "4":

            delete_book(book_service)

        elif choice == "5":

            add_member(member_service)

        elif choice == "6":

            view_members(member_service)

        elif choice == "7":

            search_members(member_service)

        elif choice == "8":

            delete_member(member_service)

        elif choice == "9":

            issue_book(issue_service)

        elif choice == "10":

            return_book(issue_service)

        elif choice == "11":

            view_issued_books(issue_service)

        elif choice == "0":

            print("\nThank you for using Library Management System!")

            database.close()

            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
