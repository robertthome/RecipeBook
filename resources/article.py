from models.db import db
from models.article import *
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class Articles(Resource):
    def get(self):
        articles = Article.find_all()
        return articles

    def post(self):
        data = request.get_json()
        params = {}
        for k in data.keys():
            params[k] = data[k]
        article = Article(**params)
        article.create()
        return article.json(), 201


class ArticleDetails(Resource):
    def get(self, article_id):
        article = Article.query.options(joinedload(
            "user")).filter_by(id=article_id).first()
        return {**article.json(), "user": article.user.json()}

    def put(self, article_id):
        data = request.get_json()
        post = Article.find_by_id(article_id)
        for key in data:
            setattr(post, key, data[key])
        db.session.commit()
        return post.json()

    def delete(self, article_id):
        print(article_id)
        article = Articles.find_by_id(article_id)
        if not article:
            return {"Message": "Not Found"}, 404
        db.session.delete(article)
        db.session.commit()
        return {"Message": "article Deleted", "payload": article_id}
