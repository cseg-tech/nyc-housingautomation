import unittest
 
from app import app 

class AutomationTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
    # executed after each test
    def tearDown(self):
        pass

    # Begin tests here

    # Begin test to check main page response
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Begin test to check login functionality
    def test_login(self):
        return True

    # Begin test to check signup functionality
    def test_signup(self):
        return 

    # Begin test to check get_keys functionality
    def test_keys(self):
        return True

    # Begin test to check email functionality
    def test_email(self):
        return True

    # Begin test to check get BBL functionality
    def test_get_bbl(self):
        return True

    # Begin test to check findAllComplaints functionality
    def test_find_all_complaints(self):
        return True

if __name__ == "__main__":
    unittest.main()
