from typing import Type
from src.domain.use_cases import RegisterPet
from src.presenters.helpers import HttpResponse, HttpRequest
from src.presenters.erros import FactoryHttpError, HttpErrors


class RegisterPetController:
    def __init__(self, register_pet_use_case: Type[RegisterPet]):
        self.register_pet_use_case = register_pet_use_case

    def route(self, request: HttpRequest) -> HttpResponse:
        required_fields = ["name", "specie", "user_information"]
        for field in required_fields:
            if field not in request.body.keys():
                return FactoryHttpError(HttpErrors.error_400()).run()

        user_information_params = request.body.get("user_information")
        if not any(
            [
                "user_id" in user_information_params,
                "user_name" in user_information_params,
            ]
        ):
            return FactoryHttpError(HttpErrors.error_400()).run()

        name = request.body.get("name")
        specie = request.body.get("specie")
        user_information = request.body.get("user_information")
        age = request.body.get("age", None)

        response = self.register_pet_use_case.registry(
            name=name, specie=specie, user_information=user_information, age=age
        )

        if response["success"] is False:
            return FactoryHttpError(HttpErrors.error_422()).run()

        return HttpResponse(status_code=200, body=response["data"])
