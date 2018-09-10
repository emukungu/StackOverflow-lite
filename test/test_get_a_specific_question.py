from .test_base import TestBase, json, cur, conn


class Test_specific_question(TestBase):
    def test_specific_question_doesnot_exist(self):
        self.post_a_question()
        response = self.app.get('/api/v1/questions/3')
        self.assertEqual(response.status_code, 404)
        self.assertIn("The question doesnot exist on this platform", response.data.decode())
        

    # def test_get_specific_question(self):
    #     self.post_a_question()
    #     cur.execute("SELECT question_id FROM questions ORDER BY question_id DESC LIMIT 5;")
    #     qn_id = cur.fetchone()
    #     print(qn_id)
    #     response = self.app.get('/api/v1/questions/54')
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertIn("hello", response.data.decode())
    
    def test_wrong_method(self):
        response = self.app.post('/api/v1/questions/1')
        self.assertEqual(response.status_code, 405)
        self.assertIn("Please enter the correct URL method", response.data.decode())