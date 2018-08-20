import unittest
from flask_api import status
from web_app import app
from flask import json
from routes.routes import post, get_all_questions, question_id, answer


class TestRoutes(unittest.TestCase):
    
    """ set up a client for the app"""
    def setUp(self):
        self.app = app.test_client()

    def test_empty_post(self):
        response = self.app.post('/api/v1/questions', data = json.dumps({"title":"","description":"",
                                                            "user_id":"","date":"","answer":"", "qn_id":""}), content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_post_success(self):
        response = self.app.post('/api/v1/questions', data = json.dumps({"title":"REST","description":"Introduction",
                                                            "user_id":"1","date":"2018-04-03","answer":"Adopted in 20000"}), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_empty_get_all_questions(self):
        response = self.app.get('/api/v1/questions')
        self.assertEqual(response.status_code, 404)

    def test_get_all_questions(self):
        response = self.app.get('/api/v1/questions')
        self.assertEqual(response.status_code, 200)

    def test_get_no_specific_question(self):
        self.app.post('/api/v1/questions', data = json.dumps({"title":"REST","description":"Introduction",
                                                            "user_id":"1","date":"2018-04-03","answer":"Adopted in 20000","question_id":"1"}), content_type="application/json")
        response = self.app.get('/api/v1/questions/3')
        self.assertEqual(response.status_code, 404)

    def test_get_specific_question(self):
        self.app.post('/api/v1/questions', data = json.dumps({"title":"REST","description":"Introduction",
                                                            "user_id":"1","date":"2018-04-03","answer":"Adopted in 20000","question_id":"1"}), content_type="application/json")
        response = self.app.get('/api/v1/questions/1')
        self.assertEqual(response.status_code, 200)

    def test_empty_post_answer(self):
        self.app.post('/api/v1/questions', data = json.dumps({"title":"REST","description":"Introduction",
                                                            "user_id":"1","date":"2018-04-03","answer":"Adopted in 20000","question_id":"1"}), content_type="application/json")
        response = self.app.post('/api/v1/questions/1/answer', data = json.dumps({"answer":""}), content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_post_answer(self):
        self.app.post('/api/v1/questions', data = json.dumps({"title":"REST","description":"Introduction",
                                                            "user_id":"1","date":"2018-04-03","answer":"Adopted in 20000","question_id":"1"}), content_type="application/json")
        response = self.app.post('/api/v1/questions/1/answer', data = json.dumps({"answer":"great"}), content_type="application/json")
        self.assertEqual(response.status_code, 200)
