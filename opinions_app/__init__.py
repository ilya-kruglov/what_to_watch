# what_to_watch/opinions_app/__init__.py

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importing modules below intentionally to ensure that they have access
# to the instances of classes created above. Placing them before the
# instances are created would lead to issues as they rely on these instances.
from . import api_views, cli_commands, error_handlers, views
