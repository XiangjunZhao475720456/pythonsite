# coding:UTF-8

import flask
from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user


def login():
    from commonapp.forms.userform import LoginForm
    from commonapp.models.usermodel import User

    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None:
            login_user(user)
            flask.flash('登录成功！')
            return redirect(url_for('index'))

    return render_template('common/login.html', login_form=login_form)

@login_required
def logout():
    logout_user()
    return redirect(url_for('common.login'))

def register():
    pass
