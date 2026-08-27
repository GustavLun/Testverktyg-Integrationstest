from src.anmalningar.event import Event
from unittest.mock import Mock

from src.anmalningar.member_service import MemberService


def test_sign_up(event, mocker):

    mock_ms = mocker.Mock(spec=MemberService)
    mock_ms.member_list = ["jonah hill"]

    event.sign_up("jonah hill", mock_ms)

    assert "jonah hill" in event.property