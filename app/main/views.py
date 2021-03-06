from flask import render_template, redirect, url_for, abort, request, flash
from flask_login import login_required, current_user

from . import MAIN
from .. import DB, PHOTOS

from .forms import UpdateProfile, PitchForm, CommentForm
from ..models import User, Category, Pitch, Comment


@MAIN.route('/')
def index():

    '''
    View root function that returns the index page and its content
    '''

    title = 'Minute-Pitch - Homepage'

    return render_template('index.html', title=title)


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


@MAIN.route('/categories/pitches/new/', methods=['GET', 'POST'])
@login_required
def new_pitch():

    '''
    Function to render a form and get data from that form
    '''

    form = PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        # Pitch instance
        new_pitch = Pitch(title=title, body=body, user=current_user)

        # Save Pitch
        new_pitch.save_pitch()

        return redirect(url_for('.index'))

    return render_template('new_pitch.html', form=form)


@MAIN.route('/categories/pitches')
def pitches():

    '''
    Function to display all the pitches added
    '''

    pitches = Pitch.query.all()

    return render_template('pitches.html', pitches=pitches)


@MAIN.route('/categories/pitches/comments/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):

    '''
    Function to render a form and get data from that form
    '''

    form = CommentForm()
    pitch = Pitch.query.filter_by(id=id).first()

    if form.validate_on_submit():
        post = Comment(post=form.post.data)

        DB.session.add(post)
        DB.session.commit()

        flash('Your comment has been created!')
        return redirect(url_for('.index'))

    title = f'{pitch.title}'

    return render_template('new_comment.html', title=title, form=form, pitch=pitch)


@MAIN.route('/categories/pitches/comments/<int:id>')
def comments(id):

    '''
    Function that displays all comments for a pitch
    '''

    pitch = Pitch.query.get(id)
    comment = Comment.get_comments(pitch.id)
    title = f'{pitch.title}'

    return render_template('comments.html', title=title, pitch=pitch, comment=comment)
