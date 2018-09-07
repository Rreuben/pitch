from flask import Blueprint, Flask

MAIN = Blueprint('main', __name__)

from . import views, errors