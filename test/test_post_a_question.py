from .test_base import TestBase, json



class Test_post_a_question(TestBase):
    
    
    def test_missing_fields(self):
        response = self.app.post('/api/v1/questions',
                                  data = self.empty_data, 
                                  headers = {
                                      "Content-Type": "application/json",
                                      "Authorization": "Bearer " + self.login()
                                        }
                                  )
        self.assertEqual(response.status_code, 400)
        self.assertIn("Fill in the missing fields", response.data.decode())

    def test_duplicate_post(self):
        self.post_a_question()
        response = self.post_a_question()
        self.assertEqual(response.status_code, 409)
        self.assertIn("Question already exists", response.data.decode())
        
    
    def test_empty_json_input(self):
        response = self.app.post('/api/v1/questions', data = json.dumps({}), headers = {
                                      "Content-Type": "application/json",
                                      "Authorization": "Bearer " + self.login()
                                        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid inputs", response.data.decode())

    def test_incorrect_values(self):
        response = self.app.post('/api/v1/questions', data = self.incorrect_data, headers = {
                                      "Content-Type": "application/json",
                                      "Authorization": "Bearer " + self.login()
                                        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Enter the correct values", response.data.decode())

    def test_successful_post(self):
        response = self.post_a_question()
        self.assertEqual(response.status_code, 201)
        self.assertIn("Your question has been added to database", response.data.decode())

    