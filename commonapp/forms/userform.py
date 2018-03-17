# coding:UTF-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(),Length(min=4,max=16,message=u'用户名长度在4-16位')])
    password = PasswordField('密码', validators=[DataRequired(),Length(min=8,max=16,message=u'密码长度在4-16位')])
    remember_me = BooleanField('记住我', default=False)


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(),Length(min=4,max=16,message=u'用户名长度在4-16位')])
    realname = StringField('真实姓名', validators=[DataRequired()])
    password = PasswordField('登录密码', validators=[DataRequired(),Length(min=8,max=16,message=u'密码长度在4-16位')])
    password_again = PasswordField('确认登录密码', validators=[DataRequired(),Length(min=8,max=16,message=u'密码长度在4-16位')])
    phone = StringField('电话号码', validators=[DataRequired()])
    gender = StringField('性别')
    email = StringField('邮箱', validators=[DataRequired(), Email()])


class ChangePwdForm(FlaskForm):
    current_pwd = PasswordField('原始密码', validators=[DataRequired(),Length(min=8,max=16,message=u'密码长度在4-16位')])
    password = PasswordField('登录密码', validators=[DataRequired(),Length(min=8,max=16,message=u'密码长度在4-16位')])
    password_again = PasswordField('确认登录密码', validators=[DataRequired(),Length(min=8,max=16,message=u'密码长度在4-16位')])
