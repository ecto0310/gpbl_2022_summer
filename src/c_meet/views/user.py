from flask import Blueprint
from flask_login import (current_user, login_required)

user = Blueprint('user', __name__)


@user.route('/me')
@login_required
def me():
    return current_user.id+" "+current_user.google_id+" "+current_user.name
