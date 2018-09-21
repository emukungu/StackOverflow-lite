from .test_base import TestBase, json, status



class Test_signup(TestBase):
    

    def test_existing_user(self):
        self.app.post('/api/v1/auth/signup', data = self.signup_data, content_type='application/json')
        response = self.app.post('/api/v1/auth/signup', data = self.signup_data, content_type='application/json')
        self.assertEqual(response.status_code, 403)
        self.assertIn("User already exists", response.data.decode())
    
    def test_missing_fields(self):
        response = self.app.post('/api/v1/auth/signup', data = self.empty_signup_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Fill in all the fields", response.data.decode())

    def test_enter_correct_values(self):
        response = self.app.post('/api/v1/auth/signup', data = self.incorrect_signup_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Enter the correct values", response.data.decode())

    def test_wrong_method(self):
        response = self.app.get('/api/v1/auth/signup')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Please enter the correct URL method", response.data.decode())