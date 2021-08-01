import flask
from DB_handler import DBModule
from flask import Flask, redirect, render_template, url_for, request, flash, session

DB = DBModule()
app = Flask(__name__)
app.secret_key='WkaQhdajrrhtlvdmsepWkwkdaudqkRdpdjqtsp'

@app.route("/")
def index():
    if "uid" in session:
        user = session["uid"]
    else:
        user = "Login"
    return render_template("index.html", users = user)

@app.route("/list")
def post_list():
    pass

@app.route("/post/<int:pid>")
def post(pid):
    pass

@app.route("/login")
def login():
    if "uid" in session:
        flash('이미 로그인되어 있습니다.')
        return redirect(url_for("index"))
    return render_template('login.html')

@app.route("/logout")
def logout():
    if "uid" in session:
        session.pop("uid")
        return redirect(url_for("index"))
    
    else:
        return redirect(url_for("login"))
    

@app.route("/login_done", methods=["GET"])
def login_done():
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    if DB.login(uid, pwd):
        session["uid"] = uid
        return redirect(url_for('index'))
    else:
        flash('아이디가 존재하지 않거나, 아이디 또는 비밀번호가 일치하지 않습니다.')
        return redirect(url_for('login'))

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signin_done")
def signin_done():
    email = request.args.get("email")
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    name = request.args.get("name")

    if DB.signin(email,uid,pwd,name):
        return redirect(url_for("index"))
    else:
        flash('이미 존재하는 아이디이거나, 빈칸이 존재 합니다.')
        return redirect(url_for("signin"))

@app.route("/user/<uid>")
def user(uid):
    pass

@app.route("/write", methods=["GET"]) #나중에 post로 변경
def write():
    pass


if __name__ == "__main__":
    app.run(host="124.50.245.150", port=80, debug=True)