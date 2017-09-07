import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
TEMPLATES_AUTO_RELOAD = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


pc_geetest_id = "277de4efe78c203667f95862cafec5c3"
pc_geetest_key = "86b8d3b7b537558ff70a3b7b43eab658"
