from faker import Faker
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_user_controller import FindUserController


faker = Faker()


def test_hadle():
    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"user_id": faker.random_number(digits=5)})

    response = find_user_controller.handle(http_request)

    assert response.status_code == 200
    assert response.body is not None

    http_request = HttpRequest(query={"user_name": faker.name()})
    response = find_user_controller.handle(http_request)
    assert response.status_code == 200
    assert response.body is not None

    http_request = HttpRequest(
        query={"user_name": faker.name(), "user_id": faker.random_number(digits=5)}
    )
    response = find_user_controller.handle(http_request)
    assert response.status_code == 200
    assert response.body is not None

    http_request = HttpRequest(query={"bom dia": "teste"})
    response = find_user_controller.handle(http_request)
    assert response.status_code == 422

    http_request = HttpRequest()
    response = find_user_controller.handle(http_request)
    assert response.status_code == 400
