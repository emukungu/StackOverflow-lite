class User(object):
    _id  = 0

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
        User._id += 1
        self.user_id = User._id

    def useraccount(self):
        self.user_account = {
            "username": self.username,
            "user_id": self.user_id
        }
        return self.user_account