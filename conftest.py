from src.anmalningar.event import Event
import pytest
@pytest.fixture
def test_event():
    e = Event("Promenad")
    return e