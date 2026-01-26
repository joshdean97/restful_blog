from flask import Flask
from .extensions import db, ma, migrate
from .models import Post, User
from .routes.blog import blog_bp
from .routes.users import users


def create_app():
    app = Flask(__name__)
    # config
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    app.register_blueprint(blog_bp)
    app.register_blueprint(users)

    return app
