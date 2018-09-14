'''Module containing classes'''

from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import DB, LOGIN_MANAGER


@LOGIN_MANAGER.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, DB.Model):

    '''
    Defining the user object
    '''

    __tablename__ = 'users'

    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(255))
    email = DB.Column(DB.String(255), unique=True)
    password_hash = DB.Column(DB.String(255))
    bio = DB.Column(DB.String(255))
    profile_pic_path = DB.Column(DB.String())

    pitches = DB.relationship('Pitch', backref='user', lazy='dynamic')
    comments = DB.relationship('Comment', backref='user', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')


    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'{self.username}'


class Category(DB.Model):

    '''
    Defining category object
    '''

    __tablename__ = 'categories'

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(255))

    pitches = DB.relationship('Pitch', backref='category', lazy="dynamic")


class Pitch(DB.Model):

    '''
    Defining pitch object
    '''

    __tablename__ = 'pitches'

    id = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(255))
    
    body = DB.Column(DB.String(255))
    time = DB.Column(DB.DateTime, default=datetime.utcnow)

    user_id = DB.Column(DB.Integer, DB.ForeignKey('users.id'))
    category_id = DB.Column(DB.Integer, DB.ForeignKey('categories.id'))
    comments = DB.relationship('Comment', backref='pitch', lazy='dynamic')


    def save_pitch(self):
        DB.session.add(self)
        DB.session.commit()


class Comment(DB.Model):

    '''
    Defining comment object
    '''

    __tablename__ = 'comments'

    id = DB.Column(DB.Integer, primary_key=True)
    post = DB.Column(DB.String)
    time = DB.Column(DB.DateTime, default=datetime.utcnow)

    user_id = DB.Column(DB.Integer, DB.ForeignKey('users.id'))
    pitch_id = DB.Column(DB.Integer, DB.ForeignKey('pitches.id'))


    def save_comment(self):
        DB.session.add(self)
        DB.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id=id).all()

        return comments
