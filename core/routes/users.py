from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from ..schemas import user_schema, users_schema
from ..extensions import db

users = Blueprint("users", __name__, url_prefix="/users")


@users.route("/", methods=["POST"])
def create_user():
    data = request.get_json(silent=True) or {}
    new_user = user_schema.load(data)

    new_user.password_hash = generate_password_hash(data["password"], "scrypt")

    db.session.add(new_user)
    db.session.commit()

    return user_schema.dump(new_user), 201


@users.route("/", methods=["GET"])
def get_users():
    users = User.query.all()

    return users_schema.dump(users), 200


@users.route("/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.filter_by(id=id).first_or_404()

    return user_schema.dump(user), 200


@users.route("/<int:id>", methods=["PATCH"])
def edit_user(id):
    user = User.query.filter_by(id=id).first_or_404()

    data = request.get_json(silent=True) or {}
    try:
        updated_user = user_schema.load(data, instance=user, partial=True)
    except ValidationError as err:
        return {"errors": err.messages}, 400

    db.session.commit()
    return user_schema.dump(updated_user), 201


@users.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.filter_by(id=id).first_or_404()

    db.session.delete(user)
    db.session.commit()

    return {"message": f"successfully deleted user: {user.id}"}
