
from flask_script import Manager
from twittor1 import create_app
from flask_migrate import MigrateCommand

app = create_app()
manager = Manager(app)
manager.add_command("db", MigrateCommand)
# 从app.run换成manager.run
if __name__ == "__main__":
    manager.run()
