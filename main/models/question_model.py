class Question(object):
        
    def __init__(self, title, description, user_id, date, qn_id):
        self.title = title
        self.description = description
        self.user_id = int(user_id)
        self.date = date
        self.qn_id = int(qn_id)

    def listed_question(self):
        self.question_review = {
            'title': self.title,
            'user_id': self.user_id,
            'qn_id': self.qn_id,
            'date':self.date,
            'description': self.description
        }
        return self.question_review
        
    def question_id(self):
        return self.qn_id