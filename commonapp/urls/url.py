# coding:UTF-8

from commonapp import common, login, logout, register, reset_pwd, change_pwd

common.add_url_rule(rule='/register/', endpoint='register', view_func=register, methods=['GET', 'POST'])
common.add_url_rule(rule='/login/', endpoint='login', view_func=login, methods=['GET', 'POST'])
common.add_url_rule(rule='/logout/', endpoint='logout', view_func=logout, methods=['GET', 'POST'])
common.add_url_rule(rule='/resetpwd/<username>/', endpoint='resetpwd', view_func=reset_pwd, methods=['POST'])
common.add_url_rule(rule='/changepwd/', endpoint='changepwd', view_func=change_pwd, methods=['GET','POST'])
