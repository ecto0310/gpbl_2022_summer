from flask_script import Command, Option
from c_meet import db
from c_meet.models.achievements import Achievement
from c_meet.models.group_user import Group_User
from c_meet.models.schedules import Schedule
from c_meet.models.user_hobby import User_Hobby
from c_meet.models.users import User
from c_meet.models.hobbies import Hobby
from c_meet.models.groups import Group
from  sqlalchemy.sql.expression import func
from datetime import datetime, timedelta
import random


class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()

class DemoDB(Command):
    "Insert Demo Data"

    def run(self):
        for i in range(500):
            user = User(google_id=str(i), name="Demo"+str(i), icon="https://www.google.com/favicon.ico")
            User.create(user)
        hobbies = ["読書","野球","食事","ゴルフ","ランニング","ゲーム","プログラミング","映画鑑賞","電車","音楽鑑賞"]
        for hobby_name in hobbies:
            hobby = Hobby(type=hobby_name)
            Hobby.create(hobby)
        users = User.query.all()
        for user in users:
            for h in Hobby.query.order_by(func.rand()).limit(random.randint(1,4)).all():
                user_hobby = User_Hobby(user_id = user.id,hobby_id = h.id)
                User_Hobby.create(user_hobby)     
            today = datetime.now()
            tomorrow = today + timedelta(1)
            schedule = Schedule(user_id=user.id, date=today.strftime('%Y-%m-%d')) 
            Schedule.create(schedule)
            schedule = Schedule(user_id=user.id, date=tomorrow.strftime('%Y-%m-%d'))
            Schedule.create(schedule) 
        achievement = Achievement(name = "初めて人と会う")
        Achievement.create(achievement)
        achievement = Achievement(name = "10人と出会う")
        Achievement.create(achievement)
        achievement = Achievement(name = "30人と出会う")
        Achievement.create(achievement)
        achievement = Achievement(name = "同じ人と2回以上と会う")
        Achievement.create(achievement)
        achievement = Achievement(name = "同じ人と3回以上と会う")
        Achievement.create(achievement)
        
class CreateGroup(Command):

    option_list = (
        Option('-d', '--date',  dest='date', required=True),
    )
    def run(self,date):
        user_id_list = Schedule.query.filter(Schedule.date == date).all()
        users = []
        hobby_user = {}
        for h in Hobby.query.all():
            hobby_user[h.id] = []
        for id in user_id_list:
            user = User.search_id(id.user_id)
            users.append(user)
            hobbies = User_Hobby.query.filter(User_Hobby.user_id == user.id).all()
            for hobby in hobbies:
                hobby_user[hobby.hobby_id].append(id.user_id)
        complete_user = []
        while 0 < len(hobby_user):
            keys = list(hobby_user.keys())
            key = random.choice(keys)
            value = hobby_user[key]
            if len(value) < 3:
                hobby_user.pop(key)
                continue
            random.shuffle(value)
            group_users = []
            for user in value:
                if  user in complete_user:
                    value.remove(user)
                    continue
                group_users.append(user)
                if 4 <= len(group_users):
                    break 
            if len(group_users) < 3:
                hobby_user.pop(key)
                continue
            group = Group(date = date, place = "不明",hobby_id = key)
            Group.create(group)
            for user in group_users:
                group_user = Group_User(user_id = user, group_id = group.id)
                Group_User.create(group_user)
                value.remove(user)
            complete_user.extend(group_users)
            hobby_user[key]=value
