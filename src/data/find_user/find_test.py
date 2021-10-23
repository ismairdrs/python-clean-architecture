from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import FindUser


faker = Faker()
user_repo = UserRepositorySpy()
find_user = FindUser(user_repo)


def test_by_id():
    """Testing by_id method"""

    attributes = {"id": faker.random_number(digits=5)}
    response = find_user.by_id(attributes["id"])

    assert user_repo.select_user_params["user_id"] == attributes["id"]

    assert response["success"] is True
    assert response["data"]


def test_by_name():
    """Testing by_name method"""
    attributes = {"name": faker.name()}
    response = find_user.by_name(name=attributes["name"])

    assert user_repo.select_user_params["name"] == attributes["name"]
    assert response["success"] is True
    assert response["data"]


def test_by_id_and_name():
    """Testing by id and name"""

    attributes = {"id": faker.random_number(digits=5), "name": faker.name()}

    response = find_user.by_id_and_name(
        user_id=attributes["id"], name=attributes["name"]
    )
    assert user_repo.select_user_params["user_id"] == attributes["id"]
    assert user_repo.select_user_params["name"] == attributes["name"]
    assert response["success"] is True
    assert response["data"]
