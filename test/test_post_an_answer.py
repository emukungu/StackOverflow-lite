from .test_base import TestBase, json

class Test_post_an_answer(TestBase):
    def test_post_empty_answer(self):
        self.post_a_question() 
        response = self.app.post('/api/v1/questions/1/answers', data = json.dumps({"answer":""}),
                                    headers = {"Content-Type": "application/json",
                                "Authorization": "Bearer " + self.login() 
                                })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Fill in all the fields", response.data.decode())

    def test_empty_json_input(self):
        self.post_a_question()
        response = self.app.post('/api/v1/questions/1/answers', data = json.dumps({}), 
                                headers = {"Content-Type": "application/json",
                                "Authorization": "Bearer " + self.login()
                                })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid inputs", response.data.decode())

    def test_successfully_posted_answer(self):
        self.post_a_question()
        response = self.app.post('/api/v1/questions/1/answers', data = json.dumps({"answer":"great"}), 
                                headers = {"Content-Type": "application/json",
                                "Authorization": "Bearer " + self.login()
                                })
        # self.assertEqual(response.status_code, 201)
        self.assertIn("Your answer has been added", response.data.decode())

    def test_get_question_answers(self):      
        self.post_a_question()
        self.app.post('/api/v1/questions/1/answers', data = json.dumps({"answer":"great"}),
                        headers = {"Content-Type": "application/json",
                                "Authorization": "Bearer " + self.login()
                                })
        response = self.app.get('/api/v1/questions/1/answers')
        self.assertEqual(response.status_code, 200)
       