import flask, os
from DB_handler import DBModule
from flask import Flask, redirect, render_template, url_for, request, Response, flash, session, send_file

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
    '''
    ,yeardata = [{'name':'2019학년도'}, {'name':'2020학년도'}, {'name':'2021학년도'}]
        ,subjectdata =[{'name':'국어'}, {'name':'수학'}, {'name':'물리학1'}, {'name':'화학1'}, {'name':'생물과학1'}, {'name':'지구과학1'}, {'name':'정보과학'}]
        ,semesterdata = [{'name':'1학년 1학기'}, {'name':'1학년 2학기'}, {'name':'2학년 1학기'}, {'name':'2학년 2학기'}, {'name':'3학년 1학기'}, {'name':'3학년 2힉기'}]
        )

    '''


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
        if DB.verify_notbot_done(uid, pwd):
            session["uid"] = uid
            return redirect(url_for('index'))

        else:
            flash('자동가입 인증을 하지 않았습니다.')
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

@app.route('/download_verify')
def download_verify():
    file_name = f"counting.exe"
    return send_file(file_name,
                     mimetype='text/exe',
                     attachment_filename='downloaded_file_name.exe',# 다운받아지는 파일 이름.
                     as_attachment=True)


if __name__ == "__main__":
    app.run(host="localhost", port=80, debug=True)
