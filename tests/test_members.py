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
from models.member import Member
from services.member_service import MemberService


def test_add_member():

    database = Database(":memory:")

    service = MemberService(database)

    member = Member(
        "John Smith",
        "john@example.com",
        "9876543210"
    )

    success, message = service.add_member(member)

    assert success is True

    members = service.get_all_members()

    assert len(members) == 1
    assert members[0]["name"] == "John Smith"

    database.close()


if __name__ == "__main__":
    test_add_member()
    print("Member test passed.")
