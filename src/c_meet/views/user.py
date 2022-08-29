import re
from flask import request, redirect, url_for,  render_template, flash
from flask import Blueprint
from flask_login import (current_user, login_required)

from c_meet.models.users import User


user = Blueprint('user', __name__)


@user.route('/me', methods=['GET'])
@login_required
def me():
    return render_template('user/profile.html', user=current_user)


@user.route('/me/update', methods=['POST'])
@login_required
def update_user():
    user_info = User.query.get(current_user.id)
    user_info.name = request.form['name']
    user_info.icon = request.form['icon']
    User.update(user_info)
    
    flash('記事が更新されました')
    return redirect(url_for('user.me'))