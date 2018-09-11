from flask import render_template, redirect, url_for, abort, request
from flask_login import login_required

from . import MAIN
from .. import DB, PHOTOS

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


@MAIN.route('/user/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):

    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        DB.session.add(user)
        DB.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@MAIN.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_picture(uname):

    user = User.query.filter_by(username=uname).first()

    if 'photo' in request.files:
        filename = PHOTOS.save(request.files['photo'])
        path = f'photo/{filename}'
        user.profile_pic_path = path

        DB.session.commit()

    return redirect(url_for('main.profile', uname=uname))
