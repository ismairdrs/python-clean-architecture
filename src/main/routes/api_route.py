from flask import Blueprint, jsonify, request
from src.main.composer import register_user_composer, register_pet_composer
from src.main.adapter import flask_adapter
from src.presenters.erros import HttpErrors, FactoryHttpError

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/users/", methods=["POST"])
def register_user():
    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())
    if "error" in response.body:
        return jsonify(response.body), response.status_code
    message = {"Type": "users", "id": response.body.id, "name": response.body.name}

    return jsonify({"data": message}), response.status_code


@api_routes_bp.route("/api/pets/", methods=["POST"])
def register_pet():
    message = {}
    response = flask_adapter(request=request, api_route=register_pet_composer())

    if response.status_code > 399:
        return jsonify(response.body), response.status_code

    message = (
        {
            "Type": "pets",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
                "specie": response.body.specie,
                "age": response.body.age,
                "owner": response.body.user_id,
            },
        },
    )
    return jsonify({"data": message}), response.status_code
