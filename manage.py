#! encoding:utf-8
from sqlalchemy import Column, Integer, String, DateTime

from exts import db
from pythonsite import app
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)
    age = Column(Integer)
    gender = Column(String(1))
    hiredate = Column(DateTime)
    salary = Column(String(20),nullable=True)


if __name__ == '__main__':
    manager.run()
