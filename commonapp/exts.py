#! encoding:utf-8

from pythonsite import app
from flask_login import LoginManager

from commonapp.models.usermodel import User

login_manager = LoginManager(app)
login_manager.login_view = 'common.login'
login_manager.session_protection = 'strong'
login_manager.login_message = '请登录……'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
