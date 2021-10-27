from faker import Faker
from src.data.test import RegisterPetSpy
from src.infra.test import PetsRepositorySpy, UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .register_pet_controller import RegisterPetController


def test_router():
    faker = Faker()
    pet_register_spy = RegisterPetSpy(PetsRepositorySpy(), UserRepositorySpy())
    pet_controller = RegisterPetController(pet_register_spy)

    attributes = {
        "name": faker.name(),
        "specie": "fish",
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name(),
        },
    }
    response = pet_controller.route(HttpRequest(body=attributes))

    # testing input
    assert response.status_code == 200
    assert pet_register_spy.registry_param["name"] == attributes["name"]
    assert pet_register_spy.registry_param["specie"] == attributes["specie"]
    assert pet_register_spy.registry_param["age"] == attributes["age"]
    assert (
        pet_register_spy.registry_param["user_information"]["user_id"]
        == attributes["user_information"]["user_id"]
    )
    assert (
        pet_register_spy.registry_param["user_information"]["user_name"]
        == attributes["user_information"]["user_name"]
    )

    # testing output
    assert response.status_code == 200
    assert "error" not in response.body

    attributes["specie"] = 123
    response = pet_controller.route(HttpRequest(body=attributes))
    assert response.status_code == 422

    attributes["specie"] = "dog"
    del attributes["name"]
    response = pet_controller.route(HttpRequest(body=attributes))
    assert response.status_code == 400
