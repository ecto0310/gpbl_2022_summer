from flask_login import LoginManager
from flask import Flask
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

from c_meet.views.home import home  # noqa
app.register_blueprint(home)

from c_meet.views.auth import auth  # noqa
app.register_blueprint(auth)

from c_meet.views.user import user  # noqa
app.register_blueprint(user, url_prefix="/user")
