from typing import List, Dict
from src.domain.models import Pets
from src.domain.test import mock_pets


class FindPetSpy:
    def __init__(self, pet_repository: any):
        self.pet_repository = pet_repository
        self.by_pet_id_param = {}
        self.by_user_id_param = {}
        self.by_pet_id_and_user_id_param = {}

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        self.by_pet_id_param["pet_id"] = pet_id
        validate_entry = isinstance(pet_id, int)
        response = mock_pets() if validate_entry else None
        return {"success": validate_entry, "data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        self.by_user_id_param["user_id"] = user_id
        validate_entry = isinstance(user_id, int)
        response = mock_pets() if validate_entry else None
        return {"success": validate_entry, "data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        self.by_pet_id_and_user_id_param["pet_id"] = pet_id
        self.by_pet_id_and_user_id_param["user_id"] = user_id
        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)
        response = mock_pets() if validate_entry else None
        return {"success": validate_entry, "data": response}
