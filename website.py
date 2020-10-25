from flask import Flask,render_template
import os
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
