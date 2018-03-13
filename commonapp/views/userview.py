# coding:UTF-8

import flask
from flask import render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user


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


def register():
    from commonapp.forms.userform import RegisterForm

    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        realname = register_form.realname.data
        password = register_form.password.data
        password_again = register_form.password_again.data
        phone = register_form.phone.data
        email = register_form.email.data

        if password.__eq__(password_again):
            from exts import db
            from commonapp.models.usermodel import User

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
        return redirect(url_for('common.register'))
    return render_template('common/register.html', register_form=register_form)


@login_required
def reset_pwd(username):
    '''重置密码'''
    from exts import db
    from commonapp.models.usermodel import User

    if username and username.strip():
        user = db.session.query(User).filter_by(username=username).first()
        if not user:
            user.password = username + '123456'
            db.session.commit()
        return
    else:
        return '请选择需要重置密码的用户！'


@login_required
def change_pwd():
    '''修改密码'''
    from exts import db
    from commonapp.forms.userform import ChangePwdForm
    from commonapp.models.usermodel import User

    change_pwd_form = ChangePwdForm()

    if change_pwd_form.validate_on_submit():
        current_pwd = change_pwd_form.current_pwd.data.strip()
        password = change_pwd_form.password.data.strip()
        password_again = change_pwd_form.password_again.data.strip()
        if current_user.check_password(current_pwd) and password.__eq__(password_again):
            username = current_user.username
            user = db.session.query(User).filter_by(username=username).first()
            user.password = password
            db.session.commit()
            return redirect(url_for('common.logout'))
    return render_template('common/changepwd.html',change_pwd_form = change_pwd_form)


@login_required
def logout():
    logout_user()
    return redirect(url_for('common.login'))
