class Answer(object):
    """ create a model for the answers to the questions. """
    def __init__(self, user_id, question_id, body):
        self.user_id = user_id,
        self.question_id = question_id,
        self.body = body

    def answer_per_question(self):
        self.particular_answer = {
                "answer": self.body,
                "user_id": self.user_id
                # "question_id": self.question_id
                }

        return self.particular_answer