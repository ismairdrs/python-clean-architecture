from faker import Faker
from src.infra.test import PetsRepositorySpy
from .find import FindPet


faker = Faker()
pet_repo = PetsRepositorySpy()
find_pet = FindPet(pet_repo)


def test_by_pet_id():
    attributes = {"pet_id": faker.random_number(digits=4)}
    response = find_pet.by_pet_id(attributes["pet_id"])

    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]

    assert response["success"] is True
    assert response["data"]


def by_user_id():
    attributes = {"user_id": faker.random_number(digits=4)}
    response = find_pet.by_user_id(attributes["user_id"])

    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    assert response["success"] is True
    assert response["data"]


def by_pet_id_and_user_id():
    attributes = {
        "pet_id": faker.random_number(digits=4),
        "user_id": faker.random_number(digits=4),
    }
    response = find_pet.by_pet_id_and_user_id(
        attributes["pet_id"], attributes["user_id"]
    )

    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]
    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    assert response["success"] is True
    assert response["data"]
