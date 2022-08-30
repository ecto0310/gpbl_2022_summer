from flask import Blueprint, render_template
from flask_login import (current_user, login_required)
from c_meet.models.group_user import Group_User
from c_meet.models.hobbies import Hobby
from c_meet.models.users import User
from c_meet.models.groups import Group


group = Blueprint('group', __name__)


@group.route('/')
@login_required
def index():
    groups = Group.query.filter(Group_User.user_id == current_user.id).join(Group_User).all()
    view_groups = []
    for group in groups:
        view = {}
        view["id"]= group.id
        view["date"]= group.date.date()
        view["hobby"]= Hobby.query.filter(Hobby.id == group.hobby_id).first().type
        view["place"]= group.place
        view_groups.append(view)
    return render_template("group/index.html", groups = view_groups)

@group.route('/<uuid>')
@login_required
def show_group(uuid):
    users = User.query.order_by(User.id.desc()).all()
    return render_template("group/show.html", users = users)
