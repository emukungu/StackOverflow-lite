from .test_base import TestBase, json


class Test_specific_question(TestBase):
    def test_get_no_specific_question(self):
        self.app.post('/api/v1/questions', data=self.data,
                      content_type="application/json")
        response = self.app.get('/api/v1/questions/3')
        self.assertEqual(response.status_code, 404)
        self.assertIn("The question doesnot exist on this platform", response.data.decode())
        

    def test_get_specific_question(self):
        self.app.post('/api/v1/questions', data= self.data, content_type="application/json")
        response = self.app.get('/api/v1/questions/1')
        self.assertEqual(response.status_code, 200)
