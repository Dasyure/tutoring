import pytest
from rainfall_sol import rainfall, rainfall_alternative

@pytest.fixture
def test_data_set():
    return [1, 2, 3]

def test_simple(test_data_set):
    assert rainfall(test_data_set) == 2

def test_simple_alternative(test_data_set):
    assert rainfall_alternative(test_data_set) == 2

def test_negative():
    assert rainfall([1, -5, 3, 4, 4]) == 3

def test_zero():
    assert rainfall([1, 0, 2, 3]) == 2

def test_empty():
    assert rainfall([-1, -2, -3]) == None
