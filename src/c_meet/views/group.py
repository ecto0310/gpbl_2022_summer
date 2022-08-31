from operator import truediv
from flask import Blueprint, render_template, redirect, url_for
from flask_login import (current_user, login_required)
from c_meet.models.group_chat import Group_Chat
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
        view["completed"]= Group_User.query.filter(Group_User.user_id == current_user.id, Group_User.group_id == group.id).first().completed
        view["place"]= group.place
        view_groups.append(view)
    return render_template("group/index.html", groups = view_groups)

@group.route('/<uuid>')
@login_required
def show_group(uuid):
    group = Group.query.filter(Group.id == uuid).first()
    group_view = {}
    group_view["uuid"]= uuid
    group_view["date"]= group.date.date()
    group_view["completed"]= Group_User.query.filter(Group_User.user_id == current_user.id, Group_User.group_id == group.id).first().completed
    group_view["hobby"]= Hobby.query.filter(Hobby.id == group.hobby_id).first().type
    group_view["place"]= group.place
    users = User.query.join(Group_User).filter(Group_User.group_id == uuid).all()
    return render_template("group/show.html", users = users,group = group_view)


@group.route('/<uuid>/complete')
@login_required
def complete_group(uuid):
    group_user = Group_User.query.filter(Group_User.user_id == current_user.id, Group_User.group_id == uuid).first()
    group_user.completed = True
    Group_User.update(group_user)
    return redirect(url_for('group.show_group', uuid = uuid))

@group.route('/<uuid>/chat')
@login_required
def show_chat(uuid):
    group = Group.query.filter(Group.id == uuid).first()
    group_view = {}
    group_view["uuid"]= uuid
    group_view["date"]= group.date.date()
    group_view["completed"]= Group_User.query.filter(Group_User.user_id == current_user.id, Group_User.group_id == group.id).first().completed
    group_view["hobby"]= Hobby.query.filter(Hobby.id == group.hobby_id).first().type
    group_view["place"]= group.place
    chat_logs = []
    logs = Group_Chat.query.filter(Group_Chat.group_id == group.id).all()
    for log in logs:
        chat = {}
        user = User.search_id(log.user_id)
        chat["me"] = True if  current_user.id  == log.user_id else False
        chat["user_icon"] = user.icon
        chat["user_name"] = user.name
        chat["content"] = log.content
        chat["date"] = log.created_at
        chat_logs.append(chat)
    return render_template("group/chat.html", group = group_view,  chat_logs = chat_logs )
