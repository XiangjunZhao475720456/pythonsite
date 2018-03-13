# coding:UTF-8

from flask_admin import Admin
from flask_bootstrap3 import Bootstrap
from flask_login import LoginManager
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy

from pythonsite import app

db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

admin = Admin(app=app, name='commonapp')

from commonapp.models.usermodel import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app=app, datastore=user_datastore)

login_manager = LoginManager(app)
login_manager.login_view = 'common.login'
login_manager.login_message = '请登录以访问此页面！'
login_manager.login_message_category = 'info'
login_manager.session_protection = 'strong'

nav = Nav(app)
nav.register_element('top',Navbar('Flask自动化测试平台',
                                  View('主页','index'),
                                  View('退出','common.logout')
                                  ))


@login_manager.user_loader
def load_user(id):
    from commonapp.models.usermodel import User
    return User.query.filter_by(id = id).first()