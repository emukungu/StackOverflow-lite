from .test_base import *

class Test_specific_question(TestBase):
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
