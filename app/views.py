from flask import Flask,render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from app import app, db, models,login_manager
from forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user,current_user
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = models.User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user,remember=form.remember.data)
                return redirect(url_for('dashboard'))
        return '<h1>Invalid username or password'
        # return '<h1>' + form.username.data + ' '+ form.password.data+'</h1>'
    return render_template('login.html',form = form)

@app.route('/signup', methods=['GET','POST'])
def signup():
    form =RegisterForm()
    if form.validate_on_submit():
        hash_password = generate_password_hash(form.password.data, method='sha256')
        new_user = models.User(username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(new_user)
        db.session.commit()
        return "<h1>New user has been created</h1>"
        # return '<h1>'+form.username.data+' '+form.email.data+' '+form.password.data+'</h1>'
    return render_template('signup.html',form = form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html',name = current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
