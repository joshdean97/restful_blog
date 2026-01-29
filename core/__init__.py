from flask import Flask
import datetime

from .extensions import db, ma, migrate, jwt
from .models import Post, User
from .routes.blog import blog_bp
from .routes.users import users
from .routes.jwt import jwt_bp
from .data_set import jwt_blocklist


def create_app():
    app = Flask(__name__)
    # config
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "DJFOIEFREIF"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=2)

    # initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # function that finds the identity behind the JWT token that was used when the token was created
    # access_token = create_access_token(identity=str(user_id)) --> identity is the user ID

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        return jwt_payload["jti"] in jwt_blocklist

    # register blueprints
    app.register_blueprint(blog_bp)
    app.register_blueprint(users)
    app.register_blueprint(jwt_bp)

    return app
