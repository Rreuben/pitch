from flask import Blueprint

AUTH = Blueprint('auth', __name__)

from . import views, forms
