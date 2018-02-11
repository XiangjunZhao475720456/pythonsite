#! encoding:utf-8

import datetime
from functools import reduce
from operator import or_

from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore, Security

from pythonsite import db, app


class Permission(object):
    LOGIN = 0x01
    EDITOR = 0x02
    OPERATOR = 0x04
    ADMINISTER = 0xff
    PERMISSION_MAP ={
        LOGIN:('login','Login user'),
        EDITOR:('editor','Editor'),
        OPERATOR:('operator','Operator'),
        ADMINISTER:('admin','Super Adminitrator')
    }

'''角色用户关系'''
common_role_user = db.Table(
    'common_role_user',
    db.Column('id',db.Integer(),primary_key=True,autoincrement=True),
    db.Column('common_user_id', db.Integer(), db.ForeignKey('common_user.id')),
    db.Column('common_role_id', db.Integer(), db.ForeignKey('common_role.id'))
)


class Role(db.Model, RoleMixin):
    '''角色'''
    __tablename__ = 'common_role'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, comment='角色名称')
    permissions = db.Column(db.Integer(),default=Permission.LOGIN)
    description = db.Column(db.String(255), comment='描述')

    def __init__(self, name, description):
        self.name = name
        self.description = description


class User(db.Model, UserMixin):
    '''用户'''
    __tablename__ = 'common_user'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False, comment='姓名')
    phone = db.Column(db.String(11), nullable=False, default=None, comment='电话')
    gender = db.Column(db.String(1), nullable=False, default='男', comment='性别')
    email = db.Column(db.String(255), unique=True, comment='电子邮箱')
    password = db.Column(db.String(255), comment='密码')
    active = db.Column(db.Boolean(),comment='用户是否处于激活状态')
    create_date = db.Column(db.DateTime(), default=datetime.datetime.now())
    roles = db.relationship('Role', secondary=common_role_user, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, name, phone, gender, email, password):
        self.name = name
        self.phone = phone
        self.gender = gender
        self.email = email
        self.password = password

    def can(self,permissions):
        if self.roles is None:
            return False
        all_permissions = reduce(or_,map(lambda x:x.permissions,self.roles))
        return all_permissions & permissions == permissions

    def can_admin(self):
        return self.can(Permission.ADMINISTER)

user_datastore = SQLAlchemyUserDatastore(db,User,Role)
security = Security(app,user_datastore)

@security.login_context_processor
def security_login_context_processor():
    print('Login')
    return {}

