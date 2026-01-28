from flask import Flask
from .extensions import db, ma, migrate, jwt
from .models import Post, User
from .routes.blog import blog_bp
from .routes.users import users
from .routes.jwt import jwt_bp


def create_app():
    app = Flask(__name__)
    # config
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "DJFOIEFREIF"

    # initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # register blueprints
    app.register_blueprint(blog_bp)
    app.register_blueprint(users)
    app.register_blueprint(jwt_bp)

    return app
