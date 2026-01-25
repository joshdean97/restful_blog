from .extensions import db
from sqlalchemy.dialects.postgresql import ARRAY


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(55), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(24), nullable=False)
    tags = db.Column(db.JSON, nullable=False)
    author = db.Column(db.String(50), nullable=True, default="Anon")

    def __init__(self, title, content, category, tags, author):
        self.title = title
        self.content = content
        self.category = category
        self.tags = tags
        self.author = author
