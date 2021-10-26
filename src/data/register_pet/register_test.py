from faker import Faker
from src.data.test import FindUserSpy
from src.infra.test import PetsRepositorySpy, UserRepositorySpy
from .register import RegisterPet

faker = Faker()


def test_register():
    """test registry pet"""
    pet_repo = PetsRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributtes = {
        "name": faker.name(),
        "specie": faker.name(),
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name(),
        },
    }

    response = register_pet.registry(
        name=attributtes["name"],
        specie=attributtes["specie"],
        age=attributtes["age"],
        user_information=attributtes["user_information"],
    )

    assert pet_repo.insert_pet_params["name"] == attributtes["name"]
    assert pet_repo.insert_pet_params["specie"] == attributtes["specie"]
    assert pet_repo.insert_pet_params["age"] == attributtes["age"]

    assert (
        find_user.by_id_and_name_param["user_id"]
        == attributtes["user_information"]["user_id"]
    )
    assert (
        find_user.by_id_and_name_param["name"]
        == attributtes["user_information"]["user_name"]
    )

    assert response["success"] is True
    assert response["data"]
