import pytest

@pytest.fixture
def create_animal():
    name = "Lanky Joe"
    color = "Yellow"
    dob = "05/07/17"
    animal = "Giraffe"
    return (name, color, dob, animal)

def test_print_animal(create_animal):
    name, color, _, animal = create_animal
    print(f"{name} is a {color} {animal}")
