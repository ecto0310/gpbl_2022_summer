import os

DEBUG = os.getenv("DEBUG")

SQLALCHEMY_DATABASE_URI = 'sqlite:///sample.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
