from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db=SQLAlchemy()


class Users(UserMixin, db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    sername = db.Column(db.String(18), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    phone = db.Column(db.String(10))
    gender = db.Column(db.String(1))
    roll = db.Column(db.Integer)
    age =db.Column(db.Integer)

