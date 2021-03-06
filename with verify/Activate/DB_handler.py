from logging import info
import pyrebase
import json

class DBModule:
    def __init__(self):

        with open('./auth/firebaseAuth.json') as f:
            config = json.load(f)


        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

        
    def login(self , uid, pwd):
        users = self.db.child("users").get().val()
        try:
            userinfo = users[uid]
            if userinfo["pwd"] == pwd:
                return True
            else:
                return False
        except:
            return False



    def signin(self ,email, _id_, pwd, name):
        '''
            if(email or _id_ or pwd == ""):
            return False
        '''

        
        information = {
            "email":email,
            "uid":_id_,
            "pwd": pwd,
            "uname":name,
            "verify":False,
        }


        '''
        if self.signin_verf(_id_):
            
            return True
        else:
            return False
        '''
        self.db.child("users").child(_id_).set(information)
        return True



    def verify_notbot(self, verify, _id_):
        verifydic = {
            "verify": verify,
        }
        self.db.child("users").child(_id_).update(verifydic)
        return True

    def verify_notbot_done(self, uid):
        users = self.db.child("users").get().val()
        try:
            userinfo = users[uid]
            if userinfo["verify"] == "T":
                return True
            else:
                return False
        except:
            return False

    def post_detail(self, pid):
        pass

    def download(self):
        pass

    def signin_verf(self, uid):
        users = self.db.child("users").get().val()
        for i in users:
            if uid == i:
                return False

        return True
