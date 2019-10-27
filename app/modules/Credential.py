from dotenv import load_dotenv
load_dotenv()
import os

SENDGRID_KEY = os.getenv("SENDGRID_KEY")
NYC_ID = os.getenv("GEOCLI_ID")
NYC_KEY = os.getenv("GEOCLI_KEY")
PLACES_KEY = os.getenv("PLACES_KEY")
NYCDB_TOKEN = os.getenv("NYC_311_TOKEN")
MONGO_UNAME = os.getenv("MONGO_UNAME")
MONGO_PASS = os.getenv("MONGO_PASS")

TEST_USERNAME = os.getenv("SAMPLE_LOGIN")
TEST_PASSWORD = os.getenv("SAMPLE_PASS")


def get_places_key():
	return PLACES_KEY

def get_sg_key():
	return SENDGRID_KEY

def get_nyc_appID():
	return NYC_ID

def get_nyc_appKey():
	return NYC_KEY

def get_nycdb_token():
	return NYCDB_TOKEN

def getMongoID():
    return MONGO_UNAME

def getMongoPass():
    return MONGO_PASS

def getSampleLogin():
	return TEST_USERNAME

def getSamplePassword():
	return TEST_PASSWORD
