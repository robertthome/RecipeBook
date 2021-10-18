from datetime import datetime
from models import user
from models.db import db


class Article(db.Model):
    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(280), nullable=False)
    content = db.Column(db.String(280), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    username = db.Column(db.String(80), db.ForeignKey(
        'users.username'), nullable=False)

    user = db.relationship('User', backref=db.backref('users', lazy=True))

    def __init__(self, image, content, username):
        self.content = content
        self.image = image
        self.username = username

    def json(self):
        return {"id": self.id, "image": self.image, "content": self.content,  "username": self.username, "created_at": str(self.created_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        articles = Article.query.all()
        return [p.json() for p in articles]

    @classmethod
    def find_by_id(cls, article_id):
        article = Article.query.filter_by(id=article_id).first()
        return article
