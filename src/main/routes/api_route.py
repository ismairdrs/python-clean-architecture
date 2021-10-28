from flask import Blueprint, jsonify, request
from src.main.composer import (
    register_user_composer,
    register_pet_composer,
    find_user_composer,
    find_pet_composer,
)
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


@api_routes_bp.route("/api/pets/", methods=["GET"])
def find_pet():
    response = flask_adapter(request=request, api_route=find_pet_composer())
    message = {}

    if response.status_code > 399:
        return jsonify(response.body), response.status_code

    message = [
        {
            "type": "pets",
            "id": element.id,
            "name": element.name,
            "specie": element.specie.value,
            "age": element.age,
            "relationships": {"owner": {"type": "users", "id": element.user_id}},
        }
        for element in response.body
    ]

    return jsonify({"data": message}), response.status_code
