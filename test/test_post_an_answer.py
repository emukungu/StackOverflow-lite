# from .test_base import TestBase, json

# class Test_post_an_answer(TestBase):
#     def test_empty_post_answer(self):
#         self.app.post('/api/v1/questions', data = self.data, content_type="application/json")
#         response = self.app.post('/api/v1/questions/1/answer', data = json.dumps({"answer":"","user_id": ""}), content_type="application/json")
#         self.assertEqual(response.status_code, 400)
#         self.assertIn("Enter the correct values", response.data.decode())

#     def test_post_answer(self):
#         self.app.post('/api/v1/questions', data = self.data, content_type="application/json")
#         response = self.app.post('/api/v1/questions/1/answer', data = json.dumps({"answer":"great", "user_id":1}), content_type="application/json")
#         self.assertEqual(response.status_code, 201)
#         self.assertIn("Your answer has been added", response.data.decode())

#     def test_empty_json_input(self):
#         response = self.app.post('/api/v1/questions/1/answer', data = json.dumps({}), content_type="application/json")
#         self.assertEqual(response.status_code, 400)
#         self.assertIn("All data is required", response.data.decode())

#     def test_get_question_answers(self):
#         self.app.post('/api/v1/questions', data = self.data, content_type="application/json")
#         self.app.post('/api/v1/questions/1/answer', data = json.dumps({"answer":"great", "user_id":1}), content_type="application/json")
#         response = self.app.get('/api/v1/questions/1/answer')
#         self.assertEqual(response.status_code, 200)