from flask import Blueprint, render_template, request, url_for, redirect, flash

from c_meet.models.hobbies import Hobby
from c_meet.models.user_hobby import User_Hobby


hobby = Blueprint('hobby', __name__)


@hobby.route('/', methods=['GET', 'POST'])
def search():
    hobby_type = request.args.get("hobby")
  
    if (hobby_type):
        hobbies = Hobby.query.filter(Hobby.type.like("%"+hobby_type+"%")).order_by(Hobby.id.desc()).all()
    else:
        hobbies = Hobby.query.order_by(Hobby.created_at.desc()).all()
    view_hobbies = []
    for hobby in hobbies:
        view = {}
        view["id"]= hobby.id
        view["type"]= hobby.type
        view["amount"]= User_Hobby.query.filter(User_Hobby.hobby_id == hobby.id).count()
        view_hobbies.append(view)

    
    return render_template("hobby.html", hobbies=view_hobbies, hobby=hobby_type)


@hobby.route('/add_hobby', methods=['POST'])
def add_hobby():
    hobby_type = request.form["hobby"]
    hobby = Hobby(type= hobby_type)
    Hobby.create(hobby)
       
    flash('趣味を作成しました')
    
    return redirect(url_for('hobby.search'))
