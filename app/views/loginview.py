from flask import render_template

from app import app
from app.forms.loginform import LoginForm


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)
#
#
# @app.route('/')
# def index():
#     context = {
#         'title': 'home',
#         'nickname': 'Miguel'
#     }
#     return render_template('index.html', **context)
