from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):

    title = StringField('Title', validators=[Required()])
    body = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):

    post = TextAreaField('Your Comment', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):

    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
