from flask import Blueprint, jsonify, request
from src.main.composer import register_user_composer
from src.main.adapter import flask_adapter

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/users/", methods=["POST"])
def register_user():
    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())
    if "error" in response.body:
        return jsonify(response.body), response.status_code
    message = {"Type": "users", "id": response.body.id, "name": response.body.name}

    return jsonify({"data": message}), response.status_code
