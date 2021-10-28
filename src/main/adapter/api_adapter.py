from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface as Route
from src.main.validations import FindValidations
from src.presenters.helpers import HttpRequest
from src.presenters.erros import HttpErrors, FactoryHttpError


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    if request.method == "POST":
        http_request = HttpRequest(body=request.json)

    if request.method == "GET":
        query_string_params = FindValidations(request=request).validate()
        http_request = HttpRequest(
            header=request.headers, body=request.json, query=query_string_params
        )

    try:
        http_response = api_route.route(http_request)
    except IntegrityError:
        return FactoryHttpError(HttpErrors.error_409()).run()
    except Exception as exc:  # pylint: disable=broad-except
        print(exc)
        return FactoryHttpError(HttpErrors.error_500()).run()
    return http_response
