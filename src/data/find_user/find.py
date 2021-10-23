from typing import Type, List, Dict
from src.domain.use_cases import FindUser as FindUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models import Users


class FindUser(FindUserInterface):
    """Class to define use case Find User"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select User by id
        :param - user_id: id of the user
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)
        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)
        return {"success": validate_entry, "data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select User by name
        :param - user_name: name of the user
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)
        if validate_entry:
            response = self.user_repository.select_user(name=name)
        return {"success": validate_entry, "data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Select User by name and id
        :param - user_name: name of the user
        :param - user_id: id of the user
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(user_id, int)
        if validate_entry:
            response = self.user_repository.select_user(name=name, user_id=user_id)
        return {"success": validate_entry, "data": response}
