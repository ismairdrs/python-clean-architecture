from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import RegisterUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors, FactoryHttpError


class RegisterUserController(RouteInterface):
    def __init__(self, register_user_use_case: Type[RegisterUser]) -> None:
        self.register_user = register_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        data = http_request.body
        if "name" not in data or "password" not in data:
            return FactoryHttpError(HttpErrors.error_400()).run()
        response = self.register_user.register(data["name"], data["password"])

        if response["success"] is False:
            return FactoryHttpError(HttpErrors.error_422()).run()

        return HttpResponse(status_code=200, body=response["data"])
