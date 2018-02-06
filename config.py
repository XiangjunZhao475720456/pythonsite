DEBUG = True
SECRET_KEY = 'development key'

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = 'localhost'
PORT = 3306
DATABASE = 'pythonsite'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)