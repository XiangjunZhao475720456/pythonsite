#! encoding:utf-8

from flask_admin import Admin
from flask_bootstrap3 import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from pythonsite import app

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
admin = Admin(app=app, name='commonapp')

login_manager = LoginManager(app)
login_manager.login_view = 'common.login'
login_manager.login_message = '请登录……'
login_manager.login_message_category = 'info'
login_manager.session_protection = 'strong'
