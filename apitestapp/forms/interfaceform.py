# coding:UTF-8

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class InterfaceForm(Form):
    '''接口的表单'''
    project_name = StringField(u'项目名字', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口所属项目名称'})
    model_name = StringField(u'模块名字', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口所属模块名称'})
    interface_name = StringField(u'接口名字', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口名称'})
    interface_url = StringField(u'接口url', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口url'})
    interface_headers = StringField(u'接口headers', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口headers'})
    interface_method = StringField(u'请求方式', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口请求方式'})
    interface_params = StringField(u'请求参数示例', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口请求参数示例'})
    interface_bas = StringField(u'响应参数示例', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口响应参数示例'})


class InterfaceCaseForm(Form):
    '''测试用例的表单'''
    project_name = StringField(u'项目', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口项目名称'})
    model_name = StringField(u'模块', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口模块名称'})
    interface_name = StringField(u'接口名字', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口名称'})
    interface_url = StringField(u'接口url', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口url'})
    interface_headers = StringField(u'接口headers', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口headers'})
    interface_method = StringField(u'请求方式', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口请求方式'})
    interface_params = StringField(u'请求参数', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口请求参数'})
    interface_rest = StringField(u'响应预期', validators=[DataRequired()], render_kw={'placeholder': u'请输入接口响应预期'})
    # save = SelectField(u'选择是否保存测试结果', choices=choice_l, coerce=int)
