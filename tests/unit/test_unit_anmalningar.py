from src.anmalningar.event import Event
from unittest.mock import Mock
import pytest

from src.anmalningar.member_service import MemberService


@pytest.mark.unit # marker som säger att detta är ett unit test
def test_sign_up(test_event, mocker):#vi använder oss av test_event fixture som ligger i conftest

    mock_ms = mocker.Mock(spec=MemberService) # skapar en mock_ms som kopierar allt från MemberService
    mock_ms.member_list = ["jonah hill"] # Vi mockar även member_list och lägger till en member i den

    test_event.sign_up("jonah hill", mock_ms) # funktionen körs där den letar efter ett redan existerande namn i MemberService och lägger till den i event property listan.

    assert "jonah hill" in test_event.property # här kollar vi att namnet sedan finns i event property listan


@pytest.mark.unit
def test_add_member_spy(mocker): # Vi använder oss av en mocker spy.
    ms = MemberService()

    spy = mocker.spy(ms, "register_new_member") # vi ger mocker.spy funktionen ett namn "spy"

    ms.register_new_member("Jens lauring") # vi kör sedan funktionen av att registrera en medlem isolerat till MemberService

    spy.assert_called_once_with("Jens lauring") # Här kickar spy att registreringen händer 1 gång.
    assert "Jens lauring" in ms.members_list # Sedan kikar vi att medlemen faktiskt hamnar i member_list.
