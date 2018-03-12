# coding:UTF-8

from commonapp import common, login, logout, regist

common.add_url_rule(rule='/regist/', endpoint='regist', view_func=regist, methods=['GET', 'POST'])
common.add_url_rule(rule='/login/', endpoint='login', view_func=login, methods=['GET', 'POST'])
common.add_url_rule(rule='/logout/', endpoint='logout', view_func=logout, methods=['GET', 'POST'])
