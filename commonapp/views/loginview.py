#! encoding:utf-8

from flask import render_template


def home():
    content = {'nickname': 'Tom'}
    return render_template('common/index.html', **content)
