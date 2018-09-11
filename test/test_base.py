import unittest
from flask_api import status
from main import app
from flask import json, jsonify
from main.routes.baseRoutes import cur, conn



class TestBase(unittest.TestCase):
    
    def setUp(self):
        """ set up a client for the app"""
        self.app = app.app.test_client()

        "setup dummy data to use during testing"
        self.data = json.dumps({"title": "REST",
                            "description": "Introduction"
                            })
        self.empty_data = json.dumps({"title": "",
                            "description": ""
                            })
        self.incorrect_data = json.dumps({"title": 1,
                            "description": 3
                            })
        self.login_data = json.dumps({ "username":"esther",
                                        "password":"123password"
                            })
        self.signup_data = json.dumps({"username":"esther",
                                        "password":"123password",
                                        "email":"esther@gmail.com"
                            })
        self.empty_signup_data = json.dumps({"username":"",
                                        "password":"",
                                        "email":""})
        self.incorrect_signup_data = json.dumps({"username":123,
                                        "password":123,
                                        "email":[]
                            })
        self.incorrect_login_data = json.dumps({"username":123,
                                        "password":123
                            })
        self.empty_login_data = json.dumps({"username":"",
                                        "password":""
                            })
    
    # helper functions
    def login(self):
        self.app.post('/api/v1/auth/signup', data = self.signup_data, content_type ='application/json')
        response = self.app.post('/api/v1/auth/login', data = self.login_data, content_type ='application/json')
        data = json.loads(response.data.decode())
        result = data["token"]
        return result

    def post_a_question(self):
        response = self.app.post('/api/v1/questions', data=self.data,
                      headers = {"Content-Type": "application/json",
                                "Authorization": "Bearer " + self.login()
                                })
        return response
    def tearDown(self):
        cur.execute("DELETE FROM answers;")
        # cur.execute("ALTER TABLE answers DROP CONSTRAINT answers_pkey;")  
        # cur.execute("ALTER TABLE answers DROP CONSTRAINT question_id_fkey CASCADE;") 
        # cur.execute("ALTER TABLE answers DROP CONSTRAINT user_id_fkey;")     
        cur.execute("DELETE FROM questions;")
        # cur.execute("ALTER TABLE questions DROP CONSTRAINT questions_pkey;")
        # cur.execute("ALTER TABLE questions DROP CONSTRAINT user_id_fkey;")
        # cur.execute("ALTER TABLE users DROP CONSTRAINT users_pkey CASCADE;")
        cur.execute("DELETE FROM users;")       
        conn.commit()
