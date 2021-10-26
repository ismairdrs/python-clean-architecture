from typing import Type
from src.domain.use_cases import FindUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors


class FindUserController:
    def __init__(self, find_user_use_case: Type[FindUser]):
        self.find_user_use_case = find_user_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:

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
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"],
                    body=http_error["body"],
                )
            return HttpResponse(status_code=200, body=response["data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"],
            body=http_error["body"],
        )
