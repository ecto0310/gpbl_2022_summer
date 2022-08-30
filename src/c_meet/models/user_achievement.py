from c_meet import db, User
from c_meet.models.achievements import Achievement
import uuid
from sqlalchemy.orm import relationship, backref
from flask_login import current_user

class User_Achievement(db.Model):
    __tablename__ = 'user_achievement'
    id = db.Column(db.String(36), default=lambda: str(
        uuid.uuid4()), primary_key=True)
    user_id = db.Column(db.String(64), db.ForeignKey('users.id'))
    achievement_id = db.Column(db.String(64), db.ForeignKey('achievements.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    user = relationship(User, backref=backref("user_achievement", cascade="all, delete-orphan"))
    achievement = relationship(Achievement, backref=backref("user_achievement", cascade="all, delete-orphan"))

    @staticmethod
    def create(user_achievement):
        db.session.add(user_achievement)
        db.session.commit()


    def delete(ids):
        User_Achievement.query.filter(User_Achievement.user_id == current_user.id).filter(User_Achievement.hobby_id.in_(ids)).delete()
        db.session.commit()

    def __repr__(self):
        return

    @staticmethod
    def create(user_achievement):
        db.session.add(user_achievement)
        db.session.commit()
        return
