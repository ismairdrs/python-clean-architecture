from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterUserController
from src.data.register_user import RegisterUser
from src.infra.repo.user_repository import UserRepository


def register_user_composer() -> RouteInterface:
    """Composing Register User Route"""
    repository = UserRepository()
    register_user_use_case = RegisterUser(repository)
    return RegisterUserController(register_user_use_case)
