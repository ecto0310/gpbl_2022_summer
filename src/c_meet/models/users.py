from c_meet import db
from sqlalchemy.dialects.mysql import LONGTEXT
from flask_login import UserMixin
import uuid


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.String(36), default=lambda: str(
        uuid.uuid4()), primary_key=True)
    google_id = db.Column(db.String(32))
    name = db.Column(db.String(32))
    icon = db.Column(LONGTEXT)
    level = db.Column(db.Integer, default=0)
    schedules = db.relationship('Schedule')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    @staticmethod
    def search_id(user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    @staticmethod
    def search_google_id(google_id):
        user = User.query.filter_by(google_id=google_id).first()
        return user

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()
    
    @staticmethod
    def update(user):
        db.session.merge(user)
        db.session.commit()

        return
