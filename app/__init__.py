from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Link
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)
db = SQLAlchemy(app)
nav = Nav()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'


@nav.navigation()
def mynavbar():
    return Navbar(
        'Flaskr',
        View('Home', 'index'),
        View('Dashboard', 'dashboard'),
        View('Sign up', 'signup'),
    )

@nav.navigation()
def mynavbar_login():
    return Navbar(
        'Flaskr',
        View('Home', 'index'),
        View('Dashboard', 'dashboard'),
        View('Log out', 'logout'),
    )
nav.register_element('top', mynavbar)
nav.init_app(app)
# ...


from app import views, models
