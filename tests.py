import unittest
 
from app import app 
from app.modules import Credential

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

    # BEGINREGION - Unit Tests

    # Begin test to check main React page response
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Begin test to check login functionality
    def test_login(self):
        sample_login = Credential.getSampleLogin()
        sample_pass = Credential.getSamplePass()

        # Check if account exists, asset
        return True

    # Begin test to check signup functionality
    def test_signup(self):
        sample_login = "nonexistentemail@test.com"
        sample_pass = "thisemaildoesntexist"

        # Rami to work with Chris to delete an email from the database
        return True

    # Begin test to check find complaonts for BBL functionality
    def test_find_all_complaints(self):
        testBBL = 1019610057

        # Check if closed and open complaints are both not null

        return True

    # Begin test to check get BBL from address functionality
    def test_get_bbl(self):

        # Call NYCDBWrapper.getBBL(housenum, street, borough) and check that the return value is not null for the below inputs
        house_num = "70"
        street = "Morningside Drive"
        borough = "manhattan"

        return True

    # Begin test to check email functionality
    def test_send_email(self):
        return True

    # ENDREGION - Unit Tests

if __name__ == "__main__":
    unittest.main()
