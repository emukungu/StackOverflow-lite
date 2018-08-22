import unittest
from main.models.question_model import Question

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