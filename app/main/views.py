from flask import render_template, redirect, url_for, abort
from flask_login import login_required
from . import MAIN
from .forms import UpdateProfile
from ..models import User, Category, Pitch, Comment


@MAIN.route('/')
def index():

    '''
    View root function that returns the index page and its content
    '''

    categories = Category.query.all()

    return render_template('index.html', categories=categories)

@MAIN.route('/user/<uname>')
def profile(uname):

    '''
    Function that returns the user's profile page
    '''

    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user=user)
