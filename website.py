from flask import Flask,render_template,jsonify,request,redirect,url_for
import os
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/About")
def about():
    return render_template("about.html")

@app.route("/contactus")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
