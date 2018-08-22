from .test_base import *


class Test_get_all_questions(TestBase):
    def test_empty_get_all_questions(self):
        response = self.app.get('/api/v1/questions')
        self.assertEqual(response.status_code, 404)

    def test_get_all_questions(self):
        self.app.post('/api/v1/questions', data = json.dumps({"title":"REST","description":"Introduction",
                                                            "user_id":"1","date":"2018-04-03","answer":"Adopted in 20000"}), content_type="application/json")
        response = self.app.get('/api/v1/questions')
        self.assertEqual(response.status_code, 200)
