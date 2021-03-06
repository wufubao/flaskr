from flask import Flask,render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from app import app, db, models,login_manager
from forms import LoginForm, RegisterForm,QuestionForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user,current_user
from geetest import GeetestLib
from config import pc_geetest_id, pc_geetest_key
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))

@app.route('/')
@app.route('/newindex')
def new_index():
    return render_template('newindex.html')

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
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.form[gt.FN_CHALLENGE]
        validate = request.form[gt.FN_VALIDATE]
        seccode = request.form[gt.FN_SECCODE]
        status = session[gt.GT_STATUS_SESSION_KEY]
        user_gay_id = session["user_gay_id"]
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_gay_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if(result):
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
    questions = models.Question.query.filter_by(user_id = current_user.id).all()
    return render_template('dashboard.html',name = current_user.username, questions = questions)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/postquestion', methods=['GET', 'POST'])
@login_required
def postquestion():
    form = QuestionForm()
    if form.validate_on_submit():
        new_question = models.Question(title=form.title.data, description=form.description.data, user_id = current_user.id)
        db.session.add(new_question)
        db.session.commit()
        return '<h1>New question has been added!</h1>'
    return render_template('postquestion.html', form = form)

@app.route('/question/<question_id>')
@login_required
def question(question_id):
    question = models.Question.query.filter_by(id = question_id).first()
    owner = question.owner.username
    return render_template('question.html', owner=owner, question=question)

@app.route('/user_gay_id/register', methods=["GET"])
def get_pc_captcha():
    user_gay_id = 'goodgay'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_gay_id)
    session[gt.GT_STATUS_SESSION_KEY] = status
    session["user_gay_id"] = user_gay_id
    response_str = gt.get_response_str()
    return response_str

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 404
