from .test_base import TestBase, json


class Test_get_all_questions(TestBase): 
    def test_non_existent_questions(self):
        response = self.app.get('/api/v1/questions')
        # self.assertEqual(response.status_code, 404)
        self.assertIn("No questions exist.", response.data.decode())
        
    def test_get_all_questions(self):
        self.post_a_question()
        response = self.app.get('/api/v1/questions')
        self.assertEqual(response.status_code, 200)
        
