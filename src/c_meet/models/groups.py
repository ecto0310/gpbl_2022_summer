from c_meet import db
from c_meet.models.hobbies import Hobby
import uuid

class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.String(36), default=lambda: str(
        uuid.uuid4()), primary_key=True)
    date = db.Column(db.DateTime)
    place = db.Column(db.String(36))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    hobby_id = db.Column(db.String(36), db.ForeignKey('hobbies.id'))

    @staticmethod
    def create(group):
        db.session.add(group)
        db.session.commit()

    def __repr__(self):
        return 
