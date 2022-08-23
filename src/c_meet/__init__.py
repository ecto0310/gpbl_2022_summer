from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('c_meet.config')

db = SQLAlchemy(app)

db.init_app(app)
