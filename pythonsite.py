# coding:UTF-8

from flask import Flask, render_template
from flask_login import login_required

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index/')
@login_required
def index():
    return render_template('common/index.html', nickname='pythoner')


if __name__ == '__main__':
    from exts import *
    from commonapp import common

    app.register_blueprint(common)
    app.run(host='0.0.0.0')
