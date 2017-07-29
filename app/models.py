from app import db
from flask_login import UserMixin

upvote = db.Table('upvote',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id'))
)
downvote = db.Table('downvote',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id'))
)
thank = db.Table('thank',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('answer_id',db.Integer, db.ForeignKey('answer.id'))
)
nohelp = db.Table('nohelp',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id'))
)
qbookmark = db.Table('qbookmark',
    db.Column('user_id' ,db.Integer, db.ForeignKey('user.id')),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'))
)
abookmark = db.Table('abookmark',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    # userclass = db.Column(db.Integer)
    questions = db.relationship('Question', backref='owner', lazy='dynamic')
    answers = db.relationship('Answer', backref='owner', lazy='dynamic')
    upvotes = db.relationship('Answer', secondary=upvote, backref=db.backref('upvote_users', lazy='dynamic'))
    downvotes = db.relationship('Answer', secondary=downvote, backref=db.backref('downvote_users', lazy='dynamic'))
    thanks = db.relationship('Answer', secondary=thank, backref=db.backref('thank_users', lazy='dynamic'))
    nohelps = db.relationship('Answer', secondary=nohelp, backref=db.backref('nohelp_users', lazy='dynamic'))
    qboomarks = db.relationship('Question', secondary=qbookmark, backref=db.backref('qbookmark_users', lazy='dynamic'))
    aboomarks = db.relationship('Answer', secondary=abookmark, backref=db.backref('abookmark_users', lazy='dynamic'))

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    description = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answers = db.relationship('Answer', backref='question', lazy='dynamic')

class Answer(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
