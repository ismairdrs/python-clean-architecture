from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import FindUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors, FactoryHttpError


class FindUserController(RouteInterface):
    def __init__(self, find_user_use_case: Type[FindUser]):
        self.find_user_use_case = find_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:

        if http_request.query:

            user_id = http_request.query.get("user_id")
            user_name = http_request.query.get("user_name")

            if user_id and user_name:
                response = self.find_user_use_case.by_id_and_name(
                    user_id=user_id, name=user_name
                )

            elif user_id:
                response = self.find_user_use_case.by_id(user_id=user_id)

            elif user_name:
                response = self.find_user_use_case.by_name(name=user_name)

            else:
                return FactoryHttpError(HttpErrors.error_422()).run()

            return HttpResponse(status_code=200, body=response["data"])

        return FactoryHttpError(HttpErrors.error_400()).run()
