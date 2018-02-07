#! encoding:utf-8
from app import db, app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.models.teacher import Teacher

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
