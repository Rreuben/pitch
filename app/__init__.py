from flask import Flask

# Import extensions
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail

# Import configurations
from config import CONFIG_OPTIONS


BOOTSTRAP = Bootstrap()
DB = SQLAlchemy()
LOGIN_MANAGER = LoginManager()
LOGIN_MANAGER.session_protection = 'strong'
LOGIN_MANAGER.login_view = 'auth.login'
PHOTOS = UploadSet('photos', IMAGES)
MAIL = Mail()


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(CONFIG_OPTIONS[config_name])

    # Initializing flask extensions
    BOOTSTRAP.init_app(app)
    DB.init_app(app)
    LOGIN_MANAGER.init_app(app)
    MAIL.init_app(app)

    # Registering app blueprints
    from .main import MAIN as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import AUTH as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    # Configuring UploadSet
    configure_uploads(app, PHOTOS)

    return app
