from faker import Faker
from src.data.test import RegisterUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .register_user_controller import RegisterUserController


def test_user_route():
    faker = Faker()

    register_user = RegisterUserSpy(UserRepositorySpy())

    register_user_controller = RegisterUserController(register_user)
    attributtes = {
        "name": faker.name(),
        "password": faker.password(),
    }

    response = register_user_controller.route(HttpRequest(body=attributtes))

    # testing input
    assert register_user.registry_param["name"] == attributtes["name"]
    assert register_user.registry_param["password"] == attributtes["password"]

    # testing output
    assert response.status_code == 200
    assert "error" not in response.body

    # testing error 422
    attributtes["name"] = 1
    response = register_user_controller.route(HttpRequest(body=attributtes))
    assert response.status_code == 422

    # testing error 400
    del attributtes["name"]
    response = register_user_controller.route(HttpRequest(body=attributtes))
    assert response.status_code == 400
