from flask_login.utils import login_required
from application import app
from flask import render_template, flash, redirect, url_for
from application.forms import LoginForm
from flask_login import current_user, login_user
from application.models import User
from flask_login import logout_user
from flask_login import login_required




@app.route('/')
@app.route('/index')
@login_required
def index():
    user =  {'username': 'Laury'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'beautiful day in portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body':'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Homepage', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))