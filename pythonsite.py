#! encoding:utf-8

from flask import Flask, redirect, url_for
from flask_bootstrap3 import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from commonapp import common

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return redirect(url_for('common.home'))


if __name__ == '__main__':
    app.register_blueprint(common)
    app.run(host='0.0.0.0')
