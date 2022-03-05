from flask_script import Manager
from twittor1 import create_app

app = create_app()
manager = Manager(app)
# 从app.run换成manager.run
if __name__ == "__main__":
    manager.run()