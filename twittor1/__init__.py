
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from twittor1.config import Config

db = SQLAlchemy()
migrate = Migrate()

from twittor1.route import index, login

def create_app():
    app = Flask(__name__)  # 加载成controller
    app.config.from_object(Config)
    db.init_app(app)  # 初始化controller时，也初始化和database的连接
    migrate.init_app(app, db)
    app.add_url_rule("/index", "index", index)
    app.add_url_rule("/login", "login", login, methods=['GET', 'POST'])
    return app
