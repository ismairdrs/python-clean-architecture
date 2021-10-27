from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import FindPet
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.erros import HttpErrors, FactoryHttpError


class FindPetController(RouteInterface):
    def __init__(self, find_pet_use_case: Type[FindPet]):
        self.find_pet_use_case = find_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        if http_request.query:
            response = None
            pet_id = http_request.query.get("pet_id")
            user_id = http_request.query.get("user_id")

            if pet_id and user_id:
                response = self.find_pet_use_case.by_pet_id_and_user_id(
                    pet_id=pet_id, user_id=user_id
                )
            elif pet_id:
                response = self.find_pet_use_case.by_pet_id(pet_id=pet_id)
            elif user_id:
                response = self.find_pet_use_case.by_user_id(user_id=user_id)
            else:
                return FactoryHttpError(HttpErrors.error_422()).run()
            return HttpResponse(status_code=200, body=response["data"])
        return FactoryHttpError(HttpErrors.error_400()).run()
