from flask import Blueprint, render_template
from flask_login import (current_user, login_required)
from c_meet.models.users import User
from c_meet.models.groups import Group


group = Blueprint('group', __name__)


@group.route('/')
@login_required
def index():
    groups = Group.query.order_by(Group.id.desc()).all()
    return render_template("group/index.html", groups = groups)


@group.route('/<uuid>')
@login_required
def show_group(uuid):
    users = User.query.order_by(User.id.desc()).all()
    return render_template("group/show.html", users = users)
