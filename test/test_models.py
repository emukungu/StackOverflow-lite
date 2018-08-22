import unittest
from main.models.question_model import Question
from main.models.answer_model import Answer
from main.models.user_model import User

class TestQuestion(unittest.TestCase):
    
    """create an object of class question """
    def setUp(self):
        self.question = Question("REST", "Introduction", 1, "2018-03-04")
    
    """ test if object created is of class Question """
    def test__init__(self):      
      self.assertIsInstance(self.question, Question)

    def test_question_account(self):
        self.question_details = {
            "title": self.question.title,
            "description":self.question.description,
            "user_id": self.question.user_id,
            "date": self.question.date,
            "qn_id": self.question.qn_id, 
            
        }
        self.assertEqual(self.question.question_details(), self.question_details)

class TestAnswer(unittest.TestCase):
    def setUp(self):
        self.answer = Answer("1", "1","Uses HTTP")
    
    """ test if object created is of class Question """
    def test__init__(self):      
      self.assertIsInstance(self.answer, Answer)

    def test_answer_per_question(self):
        self.particular_answer = {
            "user_id": ("1",),
            "answer": "Uses HTTP"            
        }
        self.assertEqual(self.answer.answer_per_question(), self.particular_answer)


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("esther","123password","esther@gmail.com")
    
    """ test if object created is of class Question """
    def test__init__(self):      
      self.assertIsInstance(self.user, User)

    def test_useraccount(self):
        self.user.user_account = {
            "user_id": "1",
            "username": "esther"            
        }
        self.assertEqual(self.user.useraccount(), self.user.user_account)
