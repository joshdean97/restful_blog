from .extensions import ma
from .models import Post, User

from marshmallow import fields


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class UserSchema(ma.SQLAlchemyAutoSchema):
    password = fields.String(load_only=True, required=True)

    class Meta:
        model = User
        load_instance = True
        exclude = ("password_hash",)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
