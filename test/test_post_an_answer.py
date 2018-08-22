from .test_base import *

class Test_post_an_answer(TestBase):
    def test_empty_post_answer(self):
        self.app.post('/api/v1/questions', data = json.dumps({"title":"REST","description":"Introduction",
                                                            "user_id":"1","date":"2018-04-03","answer":"Adopted in 20000","question_id":"1"}), content_type="application/json")
        response = self.app.post('/api/v1/questions/1/answer', data = json.dumps({"answer":"","user_id": ""}), content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_post_answer(self):
        self.app.post('/api/v1/questions', data = json.dumps({"title":"REST","description":"Introduction",
                                                            "user_id":"1","date":"2018-04-03","answer":"Adopted in 20000","question_id":"1"}), content_type="application/json")
        response = self.app.post('/api/v1/questions/1/answer', data = json.dumps({"answer":"great", "user_id":"1"}), content_type="application/json")
        self.assertEqual(response.status_code, 201)
