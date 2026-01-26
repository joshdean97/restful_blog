from .extensions import ma
from .models import Post, User


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password",)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
