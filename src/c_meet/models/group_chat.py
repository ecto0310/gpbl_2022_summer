from c_meet import db
from c_meet.models.groups import Group
from c_meet.models.users import User
import uuid
from sqlalchemy.orm import relationship, backref

class Group_Chat(db.Model):
    __tablename__ = 'group_chat'
    id = db.Column(db.String(36), default=lambda: str(
        uuid.uuid4()), primary_key=True)
    user_id = db.Column(db.String(64), db.ForeignKey('users.id'))
    group_id = db.Column(db.String(64), db.ForeignKey('groups.id'))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return

    @staticmethod
    def create(group_chat):
        db.session.add(group_chat)
        db.session.commit()
