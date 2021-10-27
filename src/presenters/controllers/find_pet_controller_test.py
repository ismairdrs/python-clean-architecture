from faker import Faker
from src.data.test import FindPetSpy
from src.infra.test import PetsRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_pet_controller import FindPetController


def test_find_pet_controller():
    faker = Faker()
    find_pet_spy = FindPetSpy(PetsRepositorySpy())
    find_pet_controller = FindPetController(find_pet_spy)

    http_request = HttpRequest(query={"pet_id": faker.random_number(digits=5)})
    response = find_pet_controller.route(http_request)

    assert response.status_code == 200
    assert response.body is not None

    http_request = HttpRequest(
        query={
            "pet_id": faker.random_number(digits=5),
            "user_id": faker.random_number(digits=5),
        }
    )

    response = find_pet_controller.route(http_request)
    assert response.status_code == 200
    assert response.body is not None

    http_request = HttpRequest(query={"bom dia": "teste"})
    response = find_pet_controller.route(http_request)
    assert response.status_code == 422

    http_request = HttpRequest()
    response = find_pet_controller.route(http_request)
    assert response.status_code == 400
    assert "error" in response.body
