# coding:UTF-8

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from pythonsite import app
from exts import db

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

from commonapp.models.usermodel import User, Role
from apitestapp.models.interfacemodel import CaseResult,InterfaceCase,Interface,Module,Project

if __name__ == '__main__':
    manager.run()
