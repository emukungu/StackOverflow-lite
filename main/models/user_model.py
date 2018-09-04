class User(object):
    _id  = 0

    def __init__(self,user_id, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        User._id += 1
        self.user_id = user_id

    def useraccount(self):
        self.user_account = {
            "username": self.username,
            "email": self.email,
            "password":self.password,
            "user_id": self.user_id
        }
        return self.user_account
    