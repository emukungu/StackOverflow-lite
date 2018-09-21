from .test_base import TestBase, json

class Test_login(TestBase):

    def test_successful_login(self):
        self.app.post('/api/v1/auth/signup', data = self.signup_data, content_type='application/json')
        response = self.app.post('/api/v1/auth/login', data = self.login_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

     
    def test_missing_fields(self):
        response = self.app.post('/api/v1/auth/login', data = self.empty_login_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Fill in all the fields", response.data.decode())

    def test_enter_correct_values(self):
        response = self.app.post('/api/v1/auth/login', data = self.incorrect_login_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Enter the correct values", response.data.decode())

    def test_wrong_method(self):
        response = self.app.get('/api/v1/auth/login')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Please enter the correct URL method", response.data.decode())
        
    