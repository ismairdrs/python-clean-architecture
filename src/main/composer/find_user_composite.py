from src.presenters.controllers import FindUserController
from src.data.find_user import FindUser
from src.infra.repo.user_repository import UserRepository


def find_user_composer() -> FindUserController:
    repository = UserRepository()
    find_user = FindUser(repository)
    return FindUserController(find_user)
