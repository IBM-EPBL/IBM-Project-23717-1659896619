from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, This is Prem. <br> Welcome to Flask. <br>This is a Flask program!</h1>"

@app.route("/home")
def home():
    return "<p>Hello, This is Home Page!<p>"

@app.route("/about")
def about():
    return "<p>Hello,  This is about Page!<p>"

@app.route("/profiles/<username>")
def profile(username):
    return "<h1>Hello, "+ username +". Welcome to Flask Programming!</h1>"
