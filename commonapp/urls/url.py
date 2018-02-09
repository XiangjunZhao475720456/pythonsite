#! encoding:utf-8
from commonapp import common, home

common.add_url_rule(rule='/', endpoint='home', view_func=home, methods=['GET'])
