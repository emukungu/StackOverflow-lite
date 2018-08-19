import unittest
from flask_api import status
from web_app import app
from flask import json
from routes.routes import post


class TestRoutes(unittest.TestCase):
    
    """ set up a client for the app"""
    def setUp(self):
        self.app = app.test_client()

    def test_empty_post(self):
        response = self.app.post('/api/v1/questions', data = json.dumps({"title":"","description":"",
                                                            "user_id":"","date":"","answer":"", "qn_id":""}), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_post_success(self):
        response = self.app.post('/api/v1/questions', data = json.dumps({"title":"REST","description":"Introduction",
                                                            "user_id":"1","date":"2018-04-03","answer":"Adopted in 20000"}), content_type="application/json")
        self.assertEqual(response.status_code, 200)

