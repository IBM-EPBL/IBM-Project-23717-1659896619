from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/signin")
def withoutbootstrap():
    return render_template('signin.html')