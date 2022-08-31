from flask import Blueprint, render_template

from c_meet.models.hobbies import Hobby
from c_meet.models.user_hobby import User_Hobby


home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template("home.html")
