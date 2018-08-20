class User(object):
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    def useraccount(self):
        self.user_account = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
        }
        return self.user_account

class Question(object):
    _id  = 0
    
    def __init__(self, title, description, user_id, date, qn_answer = ""):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.date = date
        # Question._id += 1
        self.qn_id = Question._id + 1
        self.qn_answer = qn_answer

    def questionAccount(self):
        self.question_account = {
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'date': self.date,
            'qn_id': self.qn_id,
            'qn_answer': self.qn_answer
        }
        return self.question_account