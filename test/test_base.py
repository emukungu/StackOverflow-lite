import unittest
from flask_api import status
from main import app
from flask import json

class TestBase(unittest.TestCase):
    """ set up a client for the app"""
    def setUp(self):
        self.app = app.test_client()
        self.data = json.dumps({"title": "REST",
                            "description": "Introduction",
                            "user_id": 1
                            })
        self.empty_data = json.dumps({"title": "",
                            "description": "",
                            "user_id": None
                            })
        self.incorrect_data = json.dumps({"title": 1,
                            "description": 3,
                            "user_id": "yes"
                            })