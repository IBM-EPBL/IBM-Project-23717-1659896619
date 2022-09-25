from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, This is Prem. <br> Welcome to Flask. <br>This is a Flask program!</h1>"

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/profiles/<username>")
def profile(username):
    return "<h1>Hello, "+ username +". Welcome to Flask Programming!</h1>"