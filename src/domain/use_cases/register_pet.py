from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Pets


class RegisterPet(ABC):
    """Interface to FintPet use case"""

    @abstractmethod
    def registry(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Registers a new pet"""
        raise NotImplementedError("Not implemented")  # noqa: TC003
