class HttpErrors:
    @staticmethod
    def error_422():
        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_400():
        return {"status_code": 400, "body": {"error": "Bad Request"}}
