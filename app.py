import flask
from DB_handler import DBModule
from flask import Flask, redirect, render_template, url_for, request

DB = DBModule()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list")
def post_list():
    pass

@app.route("/post/<int:pid>")
def post(pid):
    pass

@app.route("/login")
def login():
    pass

@app.route("/login_done")
def login_done():
    pass

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signin_done")
def signin_done():
    pass

@app.route("/user/<uid>")
def user(uid):
    pass

@app.route("/write", methods=["GET"]) #나중에 post로 변경
def write():
    pass


if __name__ == "__main__":
    app.run(host="124.50.245.150", port=80, debug=True)