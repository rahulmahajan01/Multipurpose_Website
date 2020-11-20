from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField , IntegerField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms import SelectField

db = SQLAlchemy()

class Users(UserMixin, db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    #username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    #phone = db.Column(db.String(10))
    #gender = db.Column(db.String(1))
    #hostel = db.Column(db.Integer)
    #roll = db.Column(db.Integer)

class LoginForm(FlaskForm):
    email = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=50)])
    #roll = IntegerField('roll number',validators=[InputRequired(),Length(max=9)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    #username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=80)])
    #phone = StringField('phone number', validators=[InputRequired(), Length(max=10)])
    #gender = SelectField('Gender',choices=[('M','Male'),('F','Female')])
    #hostel = SelectField('Current Hostel',choices=[])

