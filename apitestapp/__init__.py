# coding:UTF-8

from flask import Blueprint

apitest = Blueprint(name='apitest', import_name='__name__', static_folder='static/apitest',
                   template_folder='templates/apitest',
                   url_prefix='/apitest')

from .views.interfaceview import *
from .urls.url import *