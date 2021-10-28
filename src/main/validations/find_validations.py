from src.main.interface import Validation
from src.presenters.erros import HttpErrors, FactoryHttpError


class FindValidations(Validation):
    def __init__(self, request):
        self.request = request

    def validate(self):
        try:
            if self.request.method == "GET":
                query_string_params = self.request.args.to_dict()
                if "user_id" in query_string_params:
                    query_string_params["user_id"] = int(query_string_params["user_id"])
                if "pet_id" in query_string_params:
                    query_string_params["pet_id"] = int(query_string_params["pet_id"])
            return query_string_params
        except Exception as exc:  # pylint: disable=broad-except
            print(exc)
            return FactoryHttpError(HttpErrors.error_400()).run()
