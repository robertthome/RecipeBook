from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models.user import User
from models.post import Post
from resources.user import Users, UserDetail
from resources.post import Posts, PostDetails

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.run