from src.anmalningar.event import Event
import pytest

@pytest.fixture # En fixture som härmar Event klassen.
def test_event():
    return Event()