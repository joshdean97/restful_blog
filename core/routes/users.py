from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from ..schemas import user_schema, users_schema
from ..extensions import db

users = Blueprint("users", __name__, url_prefix="/users")


@users.route("/", methods=["POST"])
def create_user():
    new_user = user_schema.load(request.json)
    new_user.password = generate_password_hash(request.json.get("password"), "scrypt")

    db.session.add(new_user)
    db.session.commit()

    return user_schema.dump(new_user), 201


@users.route("/", methods=["GET"])
def get_users():
    pass


@users.route("/<int:id>", methods=["GET"])
def get_user(id):
    pass


@users.route("/<int:id>", methods=["PATCH"])
def edit_user(id):
    pass


@users.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    pass
