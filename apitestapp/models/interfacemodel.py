# coding:UTF-8
from sqlalchemy import func

from exts import db

class CaseResult(db.Model):
    '''用例执行结果'''
    __tablename__ = 'apitest_caseresult'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    interface_case_id = db.Column(db.INTEGER(),db.ForeignKey('apitest_interface_case.id'),comment='接口用例id')
    create_date = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(),comment='测试结果生成时间')
    result = db.Column(db.String(255),comment='测试结果')
    user_id = db.Column(db.INTEGER(),db.ForeignKey('common_user.id'),comment='测试执行者id')

class InterfaceCase(db.Model):
    '''接口测试用例'''
    __tablename__ = 'apitest_interface_case'
    id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    interface_url = db.Column(db.String(255),comment='接口url')
    interface_headers = db.Column(db.String(255),comment='http请求消息头')
    interface_method = db.Column(db.String(255),server_default='GET',comment='接口请求方式')
    interface_params = db.Column(db.String(255),comment='请求参数')
    interface_response = db.Column(db.String(255),comment='请求响应')
    interface_response_assert = db.Column(db.String(255),comment='请求响应断言')
    create_date = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(),comment='用例创建时间')
    modify_date = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='用例修改时间')
    status = db.Column(db.Boolean(),default=False,comment='是否开启')
    interface_id = db.Column(db.Integer(), db.ForeignKey('apitest_interface.id'), comment='接口id')
    user_id = db.Column(db.INTEGER(), db.ForeignKey('common_user.id'), comment='测试执行者id')
    case_result = db.relationship('CaseResult',backref=db.backref('interface_case', lazy='dynamic'))


class Interface(db.Model):
    '''接口'''
    __tablename__ = 'apitest_interface'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    interface_name = db.Column(db.String(255), comment='接口名')
    interface_url = db.Column(db.String(255),comment='接口url')
    interface_headers = db.Column(db.String(255),comment='http请求消息头')
    interface_method = db.Column(db.String(255),server_default='GET',comment='接口请求方式')
    interface_params = db.Column(db.String(255),comment='请求参数示例')
    interface_response = db.Column(db.String(255),comment='请求响应示例')
    interface_description = db.Column(db.String(255),comment='接口描述')
    create_date = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='接口创建时间')
    modify_date = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='接口修改时间')
    status = db.Column(db.Boolean(), default=False)
    developer_id = db.Column(db.Integer(), db.ForeignKey('common_user.id'), comment='接口开发者id')
    tester_id = db.Column(db.Integer(), db.ForeignKey('common_user.id'), comment='接口负责者id')
    project_id = db.Column(db.Integer(), db.ForeignKey('common_user.id'), comment='项目id')
    module_id = db.Column(db.Integer(), db.ForeignKey('apitest_module.id'), comment='模块id')
    interface_case = db.relationship('InterfaceCase',backref=db.backref('interface',lazy='dynamic'))

    def __str__(self):
        return self.interface_name

class Module(db.Model):
    '''模块，有的接口是根据模块来划分的'''
    __tablename__ ='apitest_module'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    module_name = db.Column(db.String(255), comment='模块名')
    module_description = db.Column(db.String(255),comment='模块描述')
    create_date = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='模块创建时间')
    modify_date = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='模块修改时间')
    status = db.Column(db.Boolean(), default=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('common_user.id'), comment='模块负责者id')
    project_id = db.Column(db.Integer(), db.ForeignKey('apitest_project.id'), comment='项目id')
    interface = db.relationship('Interface',backref = db.backref('module',lazy='dynamic'))

    def __str__(self):
        return  self.module_name


class Project(db.Model):
    '''项目'''
    __tablename__='apitest_project'
    id=db.Column(db.Integer(), primary_key=True, autoincrement=True)
    project_name=db.Column(db.String(255),comment='项目名')
    project_description = db.Column(db.String(255),comment='项目描述')
    module_count=db.Column(db.Integer(),comment='模块数量')
    interface_count=db.Column(db.Integer(),comment='接口数量')
    create_date = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='项目创建时间')
    modify_date = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now(), comment='项目修改时间')
    status = db.Column(db.Boolean(), default=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('common_user.id'), comment='项目负责人id')
    interface = db.relationship('Interface',backref=db.backref('project',lazy='dynamic'))
    module = db.relationship('Module',backref=db.backref('project',lazy='dynamic'))

    def __str__(self):
        return self.project_name



