from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

@app.route("/withoutbootstrap")
def withoutbootstrap():
    return render_template('withoutbootstrap.html')