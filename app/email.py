from flask_mail import Message
from flask import render_template
from . import MAIL


SENDER_EMAIL = 'harryjbenj@gmail.com'

def mail_message(subject, template, to, **kwargs):

    email = Message(subject, sender=SENDER_EMAIL, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    MAIL.send(email)
