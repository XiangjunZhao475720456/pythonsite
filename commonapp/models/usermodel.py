# coding:UTF-8

import datetime
from functools import reduce
from operator import or_

from flask_security import UserMixin, RoleMixin
from sqlalchemy import text, func

from exts import db


class Permission(object):
    LOGIN = 0x01
    EDITOR = 0x02
    OPERATOR = 0x04
    ADMINISTER = 0xff
    PERMISSION_MAP = {
        LOGIN: ('login', 'Login user'),
        EDITOR: ('editor', 'Editor'),
        OPERATOR: ('operator', 'Operator'),
        ADMINISTER: ('admin', 'Super Adminitrator')
    }


'''角色用户关系'''
common_role_user = db.Table(
    'common_role_user',
    db.Column('id', db.Integer(), primary_key=True, autoincrement=True),
    db.Column('common_user_id', db.Integer(), db.ForeignKey('common_user.id')),
    db.Column('common_role_id', db.Integer(), db.ForeignKey('common_role.id'))
)


class Role(db.Model, RoleMixin):
    '''角色'''
    __tablename__ = 'common_role'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, comment='角色名称')
    permissions = db.Column(db.Integer(), default=Permission.LOGIN)
    description = db.Column(db.String(255), comment='描述')

    def __init__(self, name, description):
        self.name = name
        self.description = description


class User(db.Model, UserMixin):
    '''用户'''
    __tablename__ = 'common_user'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False, comment='姓名')
    phone = db.Column(db.String(11), default=None, comment='电话')
    gender = db.Column(db.String(1), nullable=False, comment='性别', server_default='男')
    email = db.Column(db.String(255), unique=True, comment='电子邮箱')
    password = db.Column(db.String(255), comment='密码')
    active = db.Column(db.Boolean(), nullable=False, comment='用户是否处于激活状态', server_default='1')
    create_date = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    roles = db.relationship('Role', secondary=common_role_user, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def can(self, permissions):
        if self.roles is None:
            return False
        all_permissions = reduce(or_, map(lambda x: x.permissions, self.roles))
        return all_permissions & permissions == permissions

    def can_admin(self):
        return self.can(Permission.ADMINISTER)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        if self.active and self.active is True:
            return True
        else:
            return False

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
