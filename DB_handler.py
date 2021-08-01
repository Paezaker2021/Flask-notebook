import pyrebase
import json

class DBModule:
    def __init__(self):

        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)


        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

        
    def login(self , id, pwd):
        pass

    def signin(self ,email, _id_, pwd, name):
        information = {
            "email":email,
            "uid":_id_,
            "pwd": pwd,
            "uname":name,
            
        }

        print(information)
        self.db.child("users").child(_id_).set(information)

    def write_post(self, user, contents):
        pass

    def post_list(self):
        pass

    def post_detail(self, pid):
        pass

    def get_user(self):
        pass
