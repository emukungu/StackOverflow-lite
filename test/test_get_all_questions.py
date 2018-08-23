from .test_base import TestBase, json


class Test_get_all_questions(TestBase):
    def test_empty_get_all_questions(self):        
        response = self.app.get('/api/v1/questions')
        self.assertEqual(response.status_code, 404)
        self.assertIn("No questions exist on this platform", response.data.decode())

    def test_get_all_questions(self):
        self.app.post('/api/v1/questions', data = self.data, content_type="application/json")
        response = self.app.get('/api/v1/questions')
        self.assertEqual(response.status_code, 200)
        
