# coding:UTF-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我', default=False)


class RegistForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    realname = StringField('真实姓名',validators=[DataRequired()])
    password = PasswordField('登录密码', validators=[DataRequired()])
    password_again = PasswordField('确认登录密码', validators=[DataRequired()])
    phone = StringField('电话号码', validators=[DataRequired()])
    gender = StringField('性别')
    email = StringField('邮箱', validators=[DataRequired(), Email()])
