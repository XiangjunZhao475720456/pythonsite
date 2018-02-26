# coding:UTF-8

from flask import Blueprint

common = Blueprint(name='common', import_name='__name__', static_folder='static/common',
                   template_folder='templates/common',
                   url_prefix='/common')

from .views.userview import *
from .urls.url import *


