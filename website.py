from flask import Flask,render_template,jsonify,request,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect,CSRFError
from wtforms import StringField, PasswordField,BooleanField
from wtforms.validators import InputRequired,Email,Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from models import *
import os
app = Flask(__name__)
bootstrap = Bootstrap(app)
db= SQLAlchemy()
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:12345@localhost:5432/software'
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        user = Users.query.filter_by(email=form.email.data).first()
        name = user.name
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                #return '<h1>' + form.email.data + ' ' + form.password.data + ' ' + '  </h1>'
                return render_template("user.html", name=name)

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form=RegisterForm()
    if request.method == 'POST' :
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return render_template("services.html")

    return render_template('signup.html', form=form)
@app.route("/user", methods=['GET', 'POST'])
def user():
    username = request.form.get("uname")
    password = request.form.get("psw")
    return render_template("hello.html", name=username, name1=password)
    

if __name__ == '__main__':
    app.run(debug=True)
