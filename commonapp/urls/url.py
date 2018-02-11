#! encoding:utf-8

from commonapp import common, home, login

common.add_url_rule(rule='/login',endpoint='login',view_func=login,method=['GET'])
common.add_url_rule(rule='/', endpoint='home', view_func=home, methods=['GET'])
