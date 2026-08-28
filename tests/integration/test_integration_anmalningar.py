from src.anmalningar import member_service, event
from src.anmalningar.event import Event
from src.anmalningar.member_service import MemberService
import pytest

@pytest.mark.unit
def test_register_new_member():
   event = Event()
   ms = MemberService()
   event.register_new_member("jonah hill", ms)

   assert "jonah hill" in event.property
   assert "jonah hill" in ms.members_list
