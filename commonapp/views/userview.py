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
            if user.check_password(password):
                login_user(user)
                flask.flash('登录成功！')
                return redirect(url_for('index'))

    return render_template('common/login.html', login_form=login_form)


def regist():
    from commonapp.forms.userform import RegistForm

    regist_form = RegistForm()
    if regist_form.validate_on_submit():
        username = regist_form.username.data
        realname = regist_form.realname.data
        password = regist_form.password.data
        password_again = regist_form.password_again.data
        phone = regist_form.phone.data
        email = regist_form.email.data

        if password.__eq__(password_again):
            from commonapp.models.usermodel import User
            from exts import db

            user = User.query.filter_by(username=username).first()
            if user:
                flask.flash('用户名已经被注册了……')
            else:
                user = User(username=username, realname=realname, password=password, phone=phone, email=email)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('common.login'))
        else:
            flask.flash('两次输入的密码不一致……')
        return redirect(url_for('common.regist'))
    else:
        return render_template('common/regist.html', regist_form=regist_form)


@login_required
def logout():
    logout_user()
    return redirect(url_for('common.login'))
