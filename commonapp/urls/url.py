#! encoding:utf-8

from commonapp import common, login

common.add_url_rule(rule='/login', endpoint='login', view_func=login, methods=['GET'])
