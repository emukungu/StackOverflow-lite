from .test_base import TestBase, json
class Test_post_a_question(TestBase):

    def test_missing_fields(self):
        response = self.app.post('/api/v1/questions', data = self.empty_data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Fill in the missing fields", response.data.decode())

    def test_successful_post(self):
        response = self.app.post('/api/v1/questions', data = self.data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertIn("Your question has been posted", response.data.decode())
    
    def test_empty_json_input(self):
        response = self.app.post('/api/v1/questions', data = json.dumps({}), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid inputs", response.data.decode())

    def test_incorrect_values(self):
        response = self.app.post('/api/v1/questions', data = self.incorrect_data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        print(bytes(response.data))
        self.assertIn("Enter the correct values", response.data.decode())
