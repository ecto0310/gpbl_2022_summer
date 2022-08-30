import re
from c_meet import db
from flask import request, redirect, url_for,  render_template, flash, jsonify
from flask import Blueprint
from c_meet.models.achievements import Achievement
from c_meet.models.user_achievement import User_Achievement
from flask_login import (current_user, login_required)

from c_meet.models.users import User
from c_meet.models.hobbies import Hobby
from c_meet.models.user_hobby import User_Hobby


user = Blueprint('user', __name__)


@user.route('/me', methods=['GET'])
@login_required
def me():
    user_hobbies = Hobby.query.join(User_Hobby, Hobby.id == User_Hobby.hobby_id).filter(User_Hobby.user_id == current_user.id).all()
    hobbies = Hobby.query.order_by(Hobby.id.desc()).all()
    user_achievements = Achievement.query.join(User_Achievement, Achievement.id == User_Achievement.achievement_id).filter(User_Achievement.user_id == current_user.id).all()
    achievement_id = []
    for user_achievement in user_achievements:
        achievement_id.append(user_achievement.id)
    other_achievements = Achievement.query.filter(Achievement.id.notin_(achievement_id)).all()

    return render_template('user/profile.html', 
        user=current_user, 
        hobbies = hobbies, 
        user_hobbies = user_hobbies, 
        user_achievements = user_achievements,
        other_achievements = other_achievements
    )


@user.route('/me/update', methods=['POST'])
@login_required
def update_user():
    user_info = User.query.get(current_user.id)
    user_info.name = request.form['name']
    user_info.icon = request.form['icon']
    User.update(user_info)
    
    flash('記事が更新されました')
    return redirect(url_for('user.me'))


@user.route('/me/add_hobby', methods=['POST'])
@login_required
def add_hobby():
    user_hobby = User_Hobby(
        user_id = current_user.id,
        hobby_id = request.form['hobby']
    )
    User_Hobby.create(user_hobby)

    flash('趣味が追加されました')
    return redirect(url_for('user.me'))


@user.route('/me/delete_hobby', methods=['POST'])
@login_required
def delete_hobby():
    User_Hobby.delete(request.form.getlist('hobby_checkBox'))

    flash('趣味が削除されました')
    return redirect(url_for('user.me'))