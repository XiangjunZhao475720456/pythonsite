#! encoding:utf-8
import os

DEBUG = True
SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = 'localhost'
PORT = 3306
DATABASE = 'pythonsite'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
