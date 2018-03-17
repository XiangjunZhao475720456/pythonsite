# coding:UTF-8

from flask import Blueprint

interface = Blueprint(name='interface', import_name='__name__', static_folder='static/interface',
                   template_folder='templates/interface',
                   url_prefix='/interface')

from .views.interfaceview import *
from .urls.url import *