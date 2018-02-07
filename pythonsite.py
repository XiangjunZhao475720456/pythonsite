import config
from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object(config)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index')
def index():
    content = {
        "user":"XiangjunZhao",
        "gender":"男"

    }
    return render_template('index.html',**content)


# @app.route('/add')
# def add():
#     teacher = Teacher(name='Tom',age=25)
#     db.session.add(teacher)
#     db.session.commit()
#     return '添加用户成功'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
