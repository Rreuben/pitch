from flask import render_template
from . import MAIN


@MAIN.route('/')

def index():

    '''
    View root function that returns the index page
    '''

    return render_template('index.html')
