from app import db
from flask_login import UserMixin
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    # userclass = db.Column(db.Integer)
    questions = db.relationship('Question', backref='owner', lazy='dynamic')
    answers = db.relationship('Answer', backref='owner', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref='owner', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='owner', lazy='dynamic')
    thanks = db.relationship('Thank', backref = 'owner', lazy='dynamic')
    nohelps = db.relationship('Nohelp', backref = 'owner', lazy='dynamic')
    qboomarks = db.relationship('QBookmark', backref= 'owner', lazy='dynamic')
    aboomarks = db.relationship('ABookmark', backref= 'owner', lazy='dynamic')


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    description = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answers = db.relationship('Answer', backref='question', lazy='dynamic')
    boomarks = db.relationship('QBookmark', backref='question', lazy='dynamic')

class Answer(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    upvotes = db.relationship('Upvote', backref='answer', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='answer', lazy='dynamic')
    thanks = db.relationship('Thank', backref='answer', lazy='dynamic')
    nohelps = db.relationship('Nohelp', backref='answer', lazy='dynamic')
    boomarks = db.relationship('ABookmark', backref='answer', lazy='dynamic')


class Upvote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Downvote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Thank(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Nohelp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class QBookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

class ABookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
