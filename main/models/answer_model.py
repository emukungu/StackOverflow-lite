class Answer(object):
    """ create a model for the answers to the questions. """
    def __init__(self, user_id, question_id, body):
        self.user_id = user_id,
        self.question_id = question_id,
        self.answer = body

    def answer_per_question(self):
        self.particular_answer = {
                "answer": self.answer,
                "user_id": self.user_id
                }
        return self.particular_answer

    def qn_id(self):
        self._id = self.question_id
        return self._id