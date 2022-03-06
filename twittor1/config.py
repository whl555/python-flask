import os
path = os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(path, 'twittor.db'))
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:271826@localhost:3306/twittor'
    SQLALCHEMY_TRACK_MODIFICATIONS = False