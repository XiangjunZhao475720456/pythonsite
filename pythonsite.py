from app import app, db
from app.models.teacher import Teacher


@app.route('/add')
def add():
    teacher = Teacher(name='Rose',age=25,gender='女')
    db.session.add(teacher)
    db.session.commit()
    db.session.close()
    return '添加成功'

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
