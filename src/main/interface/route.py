from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class RouteInterface(ABC):
    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        raise NotImplementedError("Not implemented!")  # noqa: TC003
