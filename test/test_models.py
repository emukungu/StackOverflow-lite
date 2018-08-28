import unittest
from main.models.question_model import Question
from main.models.answer_model import Answer
from main.models.user_model import User

class TestQuestion(unittest.TestCase):    
    
    def setUp(self):
        """create an object of class question """
        self.question = Question("REST", "Introduction", 1, "2018-03-04")
    
    def test__init__(self): 
        """ test if object created is of class Question """     
        self.assertIsInstance(self.question, Question)

    def test_question_account(self):
        self.question_details = {
            "title": "REST",
            "description":"Introduction",
            "user_id": 1,
            "date": "2018-03-04"
        }
        self.assertEquals(self.question.question_details(), self.question_details)
        

class TestAnswer(unittest.TestCase):
    def setUp(self):
        self.answer = Answer(1, 1,"Uses HTTP")
    
    def test__init__(self): 
        """ test if object created is of class Answer """     
        self.assertIsInstance(self.answer, Answer)

    def test_answer_per_question(self):
<<<<<<< HEAD
        self.answer.particular_answer = {
            "user_id": 1,
            "answer": "Uses HTTP"            
        }
        self.assertEqual(self.answer.answer_per_question(), self.answer.particular_answer)
=======
        self.particular_answer = {
            "user_id": 1,
            "answer": "Uses HTTP"            
        }
        self.assertEquals(self.answer.answer_per_question(), self.particular_answer)
        
>>>>>>> ft-post-a-question-159866594


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("esther","123password","esther@gmail.com")
    
    def test__init__(self):  
        """ test if object created is of class User """    
        self.assertIsInstance(self.user, User)

    def test_useraccount(self):
<<<<<<< HEAD
        self.user.user_account = {
            "user_id": 1,
=======
        self.user_account = {
            "email": "esther@gmail.com",
>>>>>>> ft-post-a-question-159866594
            "username": "esther"            
        }
        self.assertEqual(self.user.useraccount(), self.user_account)
