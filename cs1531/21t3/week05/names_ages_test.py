import pytest
import requests


url = 'http://localhost:8080'

@pytest.fixture
def setup():
    '''A fixture to clear the state for each test'''
    requests.delete(f"{url}/clear")

def test_clear(setup):
    '''Test to see that /clear works'''
    response = requests.delete(f"{url}/clear")
    assert response.status_code == 200
    assert response.json() == {}

def test_add_person(setup):
    '''Testing /addperson route'''
    response = requests.post(f"{url}/addperson", json={
        "name": "Bob",
        "dob": "30/06/2000"
    })
    assert response.status_code == 200
    assert response.json() == {}

def test_get_people(setup):
    '''Testing /getpeople route'''
    # First we add a person
    response = requests.post(f"{url}/addperson", json={
        "name": "Bob",
        "dob": "30/06/2000"
    })

    # Minimum age is 20, so we should be able to get a person
    response = requests.get(f"{url}/getpeople?min_age=20")
    assert response.status_code == 200
    assert response.json() == [{
        "name": "Bob",
        "age": 21
    }]

    # Minimum age is 22, so should be empty
    response = requests.get(f"{url}/getpeople?min_age=22")
    assert response.status_code == 200
    assert response.json() == []
