from typing import Dict
from src.domain.models import Users
from src.domain.test import mock_users


class RegisterUserSpy:
    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.registry_param = {}

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        self.registry_param["name"] = name
        self.registry_param["password"] = password

        validate_entry = isinstance(name, str) and isinstance(password, str)

        response = mock_users() if validate_entry else None

        return {"success": validate_entry, "data": response}
