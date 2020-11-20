from flask import Flask,render_template, request
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager
from markupsafe import escape
from werkzeug.security import generate_password_hash,check_password_hash
import os
app = Flask(__name__)
db= SQLAlchemy()
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1234@localhost:5432/mydb'
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
   
    return render_template('login.html')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()  
    form.hostel.choices=[(hostel.number,hostel.hostel) for hostel in Hostels.query.filter_by(gender='M').all()]
    if request.method == 'POST':
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(name=form.name.data,username=form.username.data, email=form.email.data, password=hashed_password,phone=form.phone.data,gender=form.gender.data,hostel=form.hostel.data,roll=form.roll.data)
        db.session.add(new_user)
        db.session.commit()
        db.session.remove()
        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)
@app.route("/user", methods=['GET', 'POST'])
def user():
    username = request.form.get("uname")
    password = request.form.get("psw")
    return render_template("hello.html", name=username, name1=password)
    

if __name__ == '__main__':
    app.run(debug=True)
