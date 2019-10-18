from dotenv import load_dotenv
load_dotenv()
import os

SENDGRID_KEY = os.getenv("SENDGRID_KEY")
NYC_ID = os.getenv("GEOCLI_ID")
NYC_KEY = os.getenv("GEOCLI_KEY")
PLACES_KEY = os.getenv("PLACES_KEY")
NYCDB_TOKEN = os.getenv("NYC_311_TOKEN")

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