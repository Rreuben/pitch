from flask import Flask
from config import CONFIG_OPTIONS

# Import extensions
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

BOOTSTRAP = Bootstrap()
DB = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(CONFIG_OPTIONS[config_name])

    # Initializing flask extensions
    BOOTSTRAP.init_app(app)
    DB.init_app(app)

    # Registering th blueprint
    from .main import MAIN as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
