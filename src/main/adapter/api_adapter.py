from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface as Route
from src.presenters.helpers import HttpRequest
from src.presenters.erros import HttpErrors, FactoryHttpError


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    http_request = HttpRequest(body=request.json)
    try:
        http_response = api_route.route(http_request)
    except IntegrityError:
        return FactoryHttpError(HttpErrors.error_409()).run()
    except Exception as exc:  # pylint: disable=broad-except
        print(exc)
        return FactoryHttpError(HttpErrors.error_500()).run()
    return http_response
