from typing import Type, Dict, List
from src.domain.models import Pets
from src.data.interfaces import PetRepositoryInterface
from src.domain.use_cases import FindPet as FindPetInterface


class FindPet(FindPetInterface):
    """Class to define use case Find Pet"""

    def __init__(self, pet_repository: Type[PetRepositoryInterface]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""
        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)
        return {"success": validate_entry, "data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        response = None
        validate_entry = isinstance(user_id, int)
        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)
        return {"success": validate_entry, "data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)
        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, user_id=user_id)
        return {"success": validate_entry, "data": response}
