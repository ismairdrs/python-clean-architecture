from typing import Type
from src.presenters.helpers import HttpResponse


class HttpErrors:
    @staticmethod
    def error_422():
        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_400():
        return {"status_code": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_409():
        return {"status_code": 409, "body": {"error": "Conflict"}}

    @staticmethod
    def error_500():
        return {"status_code": 500, "body": {"error": "Internal Server Error"}}

    @staticmethod
    def error_400_no_result_found():
        return {"status_code": 400, "body": {"error": "No result found"}}


class FactoryHttpError:
    def __init__(self, error: Type[HttpErrors]):
        self.error = error

    def run(self):
        return HttpResponse(
            status_code=self.error.get("status_code"), body=self.error.get("body")
        )
