import pytest
from rainfall import rainfall

@pytest.fixture
def test_data_set():
    return [1, 2, 3]

def test_simple(test_data_set):
    assert rainfall(test_data_set) == 2
