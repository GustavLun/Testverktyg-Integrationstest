from src.anmalningar import event
from src.anmalningar import member_service

def test_register_new_member():
    listan =
    member = "Jonah hill"
    test_register_new_member(member)

    assert member in member_service
    assert member in list