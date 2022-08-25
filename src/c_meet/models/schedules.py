from c_meet import db
import uuid

class Schedule(db.Model):
    __tablename__ = 'schedules'

    id = db.Column(db.String(36), default=lambda: str(
        uuid.uuid4()), primary_key=True)
    user_id = db.Column(db.String(36),db.ForeignKey('users.id'),nullable = False)
    date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    __table_args__ =(db.UniqueConstraint('user_id','date',name = 'uk_user_id_date'),)


