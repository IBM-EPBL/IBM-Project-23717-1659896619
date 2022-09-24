from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, This is Prem. <br> Welcome to Flask. <br>This is a Flask program!</h1>"

