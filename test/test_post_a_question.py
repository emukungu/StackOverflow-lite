from .test_base import TestBase, json, get_jwt_identity



class Test_post_a_question(TestBase):
   
    def test_missing_fields(self):
        self.login()["token"]
        response = self.app.post('/api/v1/questions', data = self.empty_data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("Fill in the missing fields", response.data.decode())

    # def test_duplicate_post(self):
    #     # self.assertEquals(json.loads(self.data), questions_list[0])
    #     self.app.post('/api/v1/questions', data = self.data, content_type="application/json")
    #     response = self.app.post('/api/v1/questions', data = self.data, content_type="application/json")
    #     self.assertEqual(response.status_code, 400)
    #     self.assertIn("Question already exists", response.data.decode())
        
    
    # def test_empty_json_input(self):
    #     response = self.app.post('/api/v1/questions', data = json.dumps({}), content_type="application/json")
    #     self.assertEqual(response.status_code, 400)
    #     self.assertIn("Invalid inputs", response.data.decode())

    # def test_incorrect_values(self):
    #     response = self.app.post('/api/v1/questions', data = self.incorrect_data, content_type="application/json")
    #     self.assertEqual(response.status_code, 400)
    #     self.assertIn("Enter the correct values", response.data.decode())

    