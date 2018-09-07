import unittest
from flask_api import status
from main import app
from flask import json, jsonify

questions_list = [{
        "description":"Introduction",
        "title":"REST",
        "user_id":1,
        "qn_id": 1
    }]


class TestBase(unittest.TestCase):
    
    def setUp(self):
        """ set up a client for the app"""
        self.app = app.test_client()

        "setup dummy data to use during testing"
        self.data = json.dumps({"title": "REST",
                            "description": "Introduction"
                            })
        self.empty_data = json.dumps({"title": "",
                            "description": "",
                            "user_id": None,
                            "qn_id": None
                            })
        self.incorrect_data = json.dumps({"title": 1,
                            "description": 3,
                            "user_id": "yes",
                            "qn_id":"yes"
                            })

        self.login_data = json.dumps({ "username":"esther",
                                        "password":"123password"
                            })