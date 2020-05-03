import unittest
import json
import random, string
import datetime
from app import app 
from app.modules import Credential
from app.modules import MongoHelper
from app.modules import NYCDBWrapper
from flask import Flask, current_app
import hashlib

db, col = MongoHelper.init_Mongo()

class AutomationTests(unittest.TestCase):


    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.APP = Flask(__name__)
 
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
        sample_pass = Credential.getSamplePassword()

        hasher = hashlib.sha256()
        hasher.update(sample_pass.encode('utf8'))
        sample_pass = hasher.digest()

        with self.APP.app_context():
            result = MongoHelper.DB_login_user(db, col, sample_login, sample_pass, "0").get_json()
            # print(result)
            self.assertEqual(result["status"], '0')
            result = MongoHelper.DB_login_user(db, col, "notanemail", sample_pass, "0").get_json()
            # print(result)
            self.assertEqual(result["status"], '2')
            result = MongoHelper.DB_login_user(db, col, sample_login, "wrongpass", "0").get_json()
            # print(result)
            self.assertEqual(result["status"], '1')

    # Begin test to check signup functionality
    def test_signup(self):
        sample_login = "nonexistentemail@test.com"
        sample_pass = "thisemaildoesntexist"
        existing_login = Credential.getSampleLogin()
        identifier = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        with self.APP.app_context():
            result = MongoHelper.DB_register_user(db, col, identifier, sample_login, sample_pass, "70 Morningside Drive", 1019610057, 0).get_json()
            self.assertEqual(result["status"], '0')
            MongoHelper.DB_remove_user(col, sample_login)
            result = MongoHelper.DB_register_user(db, col, identifier, existing_login, sample_pass, "70 Morningside Drive", 1019610057, 0).get_json()
            self.assertEqual(result["status"], '1')

    # # Begin test to check find complaonts for BBL functionality
    def test_find_all_complaints(self):
        testBBL = 1019610057
        complaints = NYCDBWrapper.findAllComplaints(testBBL)
        self.assertIsNotNone(complaints[0])
        self.assertIsNotNone(complaints[1])
        # Check if closed and open complaints are both not null
        
    def test_complaint_sort(self):
        testBBL = 1019610057
        complaints = NYCDBWrapper.findAllComplaints(testBBL)
        complaints[0].extend(complaints[1])
        print(complaints[0])
        keywords = [['Administrative'],['Environmental'],['Safety']]
        sorted_complaints = NYCDBWrapper.sortComplaints(complaints[0],keywords)
        self.assertIsNotNone(sorted_complaints)
        
    def test_find_new_complaints(self):
        testBBL = 1019610057
        start_date = "2010-01-22T16:04:13"
        end_date = "2010-01-22T16:05:13"
        complaints = NYCDBWrapper.findNewComplaints(testBBL, start_date, end_date)
        self.assertIsNotNone(complaints[0])
    # Check if closed and open complaints are both not null


    # # Begin test to check get BBL from address functionality
    def test_get_bbl(self):
        # Call NYCDBWrapper.getBBL(housenum, street, borough) and check that the return value is not null for the below inputs
        house_num = "70"
        street = "Morningside Drive"
        borough = "manhattan"
        bbl = NYCDBWrapper.getBBL(house_num, street, borough)
        self.assertIsNotNone(bbl)

    # Begin test to check email functionality
    def test_send_email(self):
        return True
    


    # ENDREGION - Unit Tests

if __name__ == "__main__":
    unittest.main()
