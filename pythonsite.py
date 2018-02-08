from flask import render_template, flash, redirect

from app import app, db
from app.forms.loginform import LoginForm
from app.models.teachermodel import Teacher


@app.route('/add')
def add():
    teacher = Teacher(name='Rose', age=25, gender='女')
    db.session.add(teacher)
    db.session.commit()
    db.session.close()
    return '添加成功'


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form)


@app.route('/index')
def index():
    context = {
        'title': 'home',
        'nickname': 'Miguel'
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
