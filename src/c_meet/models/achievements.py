from c_meet import db
import uuid

class Achievement(db.Model):
    __tablename__ = 'achievements'

    id = db.Column(db.String(36), default=lambda: str(
        uuid.uuid4()), primary_key=True)
    name = db.Column(db.String(32))
    description = db.Column(db.Text())
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description
        self.created_at = db.func.now()
        self.updated_at = db.func.now()

    @staticmethod
    def create(achievement):
        db.session.add(achievement)
        db.session.commit()

    def __repr__(self):
        return 
