from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface as Route
from src.presenters.helpers import HttpRequest
from src.presenters.erros import HttpErrors, FactoryHttpError


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    try:
        http_request = HttpRequest(body=request.json)
    except IntegrityError:
        http_request = FactoryHttpError(HttpErrors.error_409())
    except Exception:  # pylint: disable=broad-except
        http_request = FactoryHttpError(HttpErrors.error_400())
    return api_route.route(http_request)
