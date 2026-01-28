from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    current_user,
)
from werkzeug.security import check_password_hash
from ..models import User

jwt_bp = Blueprint("jwt_bp", __name__, url_prefix="/jwt")


@jwt_bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Incorrect username or password"})
    user_id = User.query.filter_by(username=username).first().id

    access_token = create_access_token(identity=str(user_id))

    return jsonify(access_token)


@jwt_bp.route("/", methods=["GET"])
@jwt_required()
def test_logged_in():
    current_user = get_jwt_identity()

    return jsonify({"Message": "You are logged in", "User": current_user.id})
