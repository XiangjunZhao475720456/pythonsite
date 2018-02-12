#! encoding:utf-8

from flask import render_template


def login():
    return render_template('common/login.html')
