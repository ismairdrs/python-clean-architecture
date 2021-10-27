from typing import Type
from src.domain.use_cases import RegisterUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class RegisterUserController:
    def __init__(self, registry_user: Type[RegisterUser]) -> None:
        self.registry_user = registry_user

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        data = http_request.body
        if "name" not in data and "password" not in data:
            http_error = HttpErrors.error_400()
            return HttpResponse(http_error["status_code"], http_error["body"])
        return self.registry_user.execute(data["name"], data["password"])
