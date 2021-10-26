from typing import List
from src.domain.models import Pets
from src.domain.test import mock_pets


class PetsRepositorySpy:
    def __init__(self) -> None:
        self.insert_pet_params = {}
        self.select_pet_params = {}

    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        self.insert_pet_params["name"] = name
        self.insert_pet_params["specie"] = specie
        self.insert_pet_params["age"] = age
        self.insert_pet_params["user_id"] = user_id

        return mock_pets()

    def select_pet(
        self, pet_id: int = None, name: str = None, user_id: int = None
    ) -> List[Pets]:
        """Spy to all the attributes"""
        self.select_pet_params["name"] = name
        self.select_pet_params["pet_id"] = pet_id
        self.select_pet_params["user_id"] = user_id

        return [mock_pets()]
