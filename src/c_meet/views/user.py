from flask import request, redirect, url_for,  render_template
from flask import Blueprint
from flask_login import (current_user, login_required)

user = Blueprint('user', __name__)


@user.route('/me')
@login_required
def me():
    return render_template('user/profile.html', user=current_user)
