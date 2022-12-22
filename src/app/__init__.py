from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config

# Creating objects for external applications
db = SQLAlchemy()


def create_app(config_name='default') -> Flask:
    """Factory function for creating application instances

    This function creates new instance of flask application. Then it initializes external packages,
    loads in blueprints and returns constructed app instance.

    :returns:
        A instance of flask application
    """
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    # Initialization of external packages
    db.init_app(app)

    # Importing blueprints
    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
