from abc import ABC, abstractmethod
from typing import List
from src.entities import Pets


class PetRepositoryInterface(ABC):
    """xpto"""

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """abstractmethod"""
        raise NotImplementedError

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """abstractmethod"""
        raise NotImplementedError
