from .test_base import *
    
class test_post_a_question(TestBase):

    def test_empty_post(self):
        response = self.app.post('/api/v1/questions', data = json.dumps({"title":"","description":"",
                                                            "user_id":"","date":"","answer":"", "qn_id":""}), content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_post_success(self):
        response = self.app.post('/api/v1/questions', data = json.dumps({"title":"REST","description":"Introduction",
                                                            "user_id":"1","date":"2018-04-03","answer":"Adopted in 20000"}), content_type="application/json")
        self.assertEqual(response.status_code, 200)
    