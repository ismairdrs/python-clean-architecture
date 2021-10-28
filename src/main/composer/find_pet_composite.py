from src.presenters.controllers import FindPetController
from src.data.find_pet import FindPet
from src.infra.repo.pet_repository import PetsRepository


def find_pet_composer() -> FindPetController:
    repository = PetsRepository()
    find_pet = FindPet(repository)
    return FindPetController(find_pet)
