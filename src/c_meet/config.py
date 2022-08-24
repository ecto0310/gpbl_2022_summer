import os

DEBUG = os.getenv("DEBUG")

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + os.getenv("DB_USER") + ":" + os.getenv("DB_PASSWORD") + "@" + os.getenv("DB_HOST") + ":" + os.getenv("DB_PORT") + "/" + os.getenv("DB_DATABASE")
SQLALCHEMY_TRACK_MODIFICATIONS = True
