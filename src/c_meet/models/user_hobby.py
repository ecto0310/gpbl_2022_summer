from c_meet import db, User
from c_meet.models.hobbies import Hobby
import uuid
from sqlalchemy.orm import relationship, backref

class User_Hobby(db.Model):
    __tablename__ = 'user_hobby'
    id = db.Column(db.String(36), default=lambda: str(
        uuid.uuid4()), primary_key=True)
    user_id = db.Column(db.String(64), db.ForeignKey('users.id'))
    hobby_id = db.Column(db.String(64), db.ForeignKey('hobbies.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    user = relationship(User, backref=backref("user_hobby", cascade="all, delete-orphan"))
    hobby = relationship(Hobby, backref=backref("user_hobby", cascade="all, delete-orphan"))

    def __repr__(self):
        return

    @staticmethod
    def create(user_hobby):
        db.session.add(user_hobby)
        db.session.commit()
        return
