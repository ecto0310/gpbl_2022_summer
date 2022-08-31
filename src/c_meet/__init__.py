from flask_login import LoginManager
from flask import Flask, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('c_meet.config')
app.secret_key = os.urandom(32)

db = SQLAlchemy(app)


login_manager = LoginManager(app)

from c_meet.models.users import User  # noqa


@login_manager.user_loader
def load_user(user_id):
    return User.search_id(user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login?next=' + request.path)

from c_meet.views.home import home  # noqa
app.register_blueprint(home)

from c_meet.views.auth import auth  # noqa
app.register_blueprint(auth)

from c_meet.views.user import user  # noqa
app.register_blueprint(user, url_prefix="/user")

from c_meet.views.schedule import schedule  # noqa
app.register_blueprint(schedule, url_prefix="/schedule")

from c_meet.views.group import group
app.register_blueprint(group, url_prefix="/group")

from c_meet.views.hobby import hobby
app.register_blueprint(hobby, url_prefix="/hobbies")
