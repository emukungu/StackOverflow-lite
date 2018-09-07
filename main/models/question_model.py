class Question(object):
    _id  = 0
    
    def __init__(self, title, description, user_id, date):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.date = date
        Question._id += 1
        self.qn_id = Question._id
        

    def question_details(self):
        self.question_account = {
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
            'date': self.date
        }
        return self.question_account

    def listed_question(self):
        self.question_review = {
            'title': self.title,
            'user_id': self.user_id,
            'qn_id': self.qn_id,
            'date':self.date
        }
        return self.question_review
        
    def question_id(self):
        return self.qn_id