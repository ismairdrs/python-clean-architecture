from typing import Type
from src.presenters.helpers import HttpResponse


class HttpErrors:
    @staticmethod
    def error_422():
        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_400():
        return {"status_code": 400, "body": {"error": "Bad Request"}}


class FactoryHttpError:
    def __init__(self, error: Type[HttpErrors]):
        self.error = error

    def run(self):
        return HttpResponse(
            status_code=self.error.get("status_code"), body=self.error.get("body")
        )
