from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):

    title = StringField('Pitch Title', validators=[Required()])
    pitch = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):

    title = StringField('Comment Title', validators=[Required()])
    comment = TextAreaField('Your Comment', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    
    bio = TextAreaField('Bio.', validators=[Required()])
    submit = SubmitField('Submit')
