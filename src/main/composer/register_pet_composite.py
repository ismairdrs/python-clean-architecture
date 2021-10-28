from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterPetController
from src.data.register_pet import RegisterPet
from src.data.find_user import FindUser
from src.infra.repo.pet_repository import PetsRepository
from src.infra.repo.user_repository import UserRepository


def register_pet_composer() -> RouteInterface:
    """Composing Register Pet Route"""
    user_repository = UserRepository()
    pet_repository = PetsRepository()
    find_user = FindUser(user_repository)
    register_pet_use_case = RegisterPet(pet_repository, find_user)
    return RegisterPetController(register_pet_use_case)
