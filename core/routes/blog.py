from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from sqlalchemy import or_
from flask_jwt_extended import jwt_required, current_user

from ..extensions import db
from ..models import Post
from ..schemas import post_schema, posts_schema

blog_bp = Blueprint("blog_bp", __name__, url_prefix="/blog")


# create blog post
@blog_bp.route("/", methods=["POST"])
@jwt_required()
def create_blog():
    new_post = post_schema.load(request.json)
    new_post.author = current_user.username

    db.session.add(new_post)
    db.session.commit()

    return post_schema.dump(new_post), 201


# View all posts
@blog_bp.route("/", methods=["GET"])
def get_posts():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 10, type=int), 50)

    query = Post.query.order_by(Post.id.desc())

    search = request.args.get("search")
    if search:
        query = query.filter(
            or_(
                Post.title.ilike(f"%{search}%"),
                Post.content.ilike(f"%{search}%"),
                Post.author.ilike(f"%{search}%"),
                Post.category.ilike(f"%{search}%"),
            )
        )

    category = request.args.get("category")
    if category:
        query = query.filter(Post.category == category)

    author = request.args.get("author")
    if author:
        query = query.filter(Post.author == author)

    tag = request.args.get("tag")
    if tag:
        query = query.filter(Post.tags.contains([tag]))

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return {
        "items": posts_schema.dump(pagination.items),
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages,
    }, 200


# view single post
@blog_bp.route("/<int:id>", methods=["GET"])
def get_post(id):
    post = Post.query.filter_by(id=id).first_or_404()

    return post_schema.dump(post), 200


# edit post
@blog_bp.route("/<int:id>", methods=["PATCH"])
def update_post(id):
    post = Post.query.filter_by(id=id).first_or_404()

    data = request.get_json(silent=True) or {}

    try:
        updated_post = post_schema.load(data, instance=post, partial=True)
    except ValidationError as err:
        return {"errors": err.messages}, 400

    db.session.commit()
    return post_schema.dump(updated_post), 200


@blog_bp.route("/<int:id>", methods=["DELETE"])
def delete_post(id):
    post = Post.query.filter_by(id=id).first_or_404()

    db.session.delete(post)
    db.session.commit()

    return {"message": f"Post {post.id} deleted successfully"}, 200
