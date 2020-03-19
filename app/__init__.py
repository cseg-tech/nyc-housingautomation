# Begin default packages
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, jsonify
import requests
import urllib
import json
import string, random, requests, hashlib
import json

# Imported packages
from sendgrid.helpers.mail import Mail
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
from sendgrid import SendGridAPIClient

# Custom modules
from .modules import MongoHelper
from .modules import NYCDBWrapper
from .modules import Communications
from .modules import Credential

app = Flask(__name__, static_folder="./static/dist", template_folder="./static")
# COMMENT OUT THE NEXT LINE BEFORE PRODUCTION
import logging
logging.basicConfig(level=logging.DEBUG)
app.config['TEMPLATES_AUTO_RELOAD'] = True

#collection instance of DB
db, col = MongoHelper.init_Mongo()


'''path = './apiKeys/mongoURI.txt'
with open(path, 'r') as myfile:
	myURI = myfile.read()
app.config["MONGO_URI"] = myURI
mongo = PyMongo(app)'''

#get sendgrid key
key = Credential.get_sg_key()


sg_key = Credential.get_sg_key()

def cron_job():
	# Query each user, find out if anyone else has lodged complaints for thier BBL - if so, email them.
	MongoHelper.iterate_all_users(db, col)

scheduler = BackgroundScheduler()
scheduler.add_job(cron_job, 'interval', hours=24)
scheduler.start()
#Ref: https://stackoverflow.com/questions/22715086/scheduling-python-script-to-run-every-hour-accurately


#Begin Helper Routes
@app.route('/loginUser', methods=['POST'])
def loginUser():
	# print(request.get_data())
	data = request.get_json(force=True)
	email = data['email']
	password = data['password']
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
	result = "true"

	resultJson = MongoHelper.DB_login_user(db, col, email, password)
    
	print(resultJson)
	
	return resultJson

@app.route('/registerUser', methods=['POST'])
def registerUser():
	data = request.get_json(force=True)
	email = data['email']
	password = data['password']
	building = data['building']
	street = data['street']
	address = building+" "+street
	borough = data['borough']
	print("Getting BBL for: "+json.dumps(data))
	bbl = NYCDBWrapper.getBBL(building,street,borough)
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
	result = "true"
	#id_hasher = hashlib.sha256()
	#id_hasher.update(.encode('utf8'))
	identifier = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

	resultJson = MongoHelper.DB_register_user(db, col, identifier, email, password, address, bbl)
	return resultJson

@app.route('/getUserStatus', methods=['POST'])
def getUserStatus(email):
#get passed user id -> call getUserAddress to find address,
#query NYCDB to see other complaints of same address -> return JSON
	data = request.get_json(force=True)
	user_id = data['id']
	complaints = NYCDBWrapper.getSameComplaints(user_id)
	return complaints

@app.route('/resetUserPassword', methods=['POST'])
def resetPassword():
	data = request.get_json(force=True)
	email = data['email']
	statusCode = "0"
	return {"status" : statusCode}

@app.route('/getBBLDetails', methods=['POST'])
def getBBLDetails():
	data = request.get_json(force=True)
	user = data['UID']

	address = MongoHelper.getAddress(db, col, user)
	complaints = MongoHelper.getUIDComplaints(db, col, user)

	open_complaints = complaints[0]
	closed_complaints = complaints[1]
	number = complaints[2]

	returnData = {}
	returnData["address"] = address
	returnData["open_complaints"] = open_complaints
	returnData["closed_complaints"] = closed_complaints
	returnData["number"] = number

	return returnData


#endregion

#Begin page-serve routes

@app.route("/")
def index():
    return render_template("index.html")

'''
@app.route('/', methods=['GET'])
def serveIndex():
	return render_template('/index.html')

@app.route('/login', methods=['GET'])
def serveLogin():
	getMyURL=getURL()
	return render_template('/authenticate.html',myKeyURL=getMyURL)


@app.route('/signup', methods=['GET'])
def serveSignUp():
	return render_template('/signup.html')

@app.route('/mainpage', methods=['GET'])
def serveMainPage():
	user = request.args.get('UID')
	address = MongoHelper.getAddress(db, col, user)
	complaints = MongoHelper.getUIDComplaints(db, col, user)
	open_complaints = json.dumps(complaints[0])
	closed_complaints = json.dumps(complaints[1])
	number = complaints[2]
	getMyURL=getURL()
	return render_template('/mainpage.html',myKeyURL=getMyURL, address=address, open=open_complaints, closed=closed_complaints, number=number)

@app.route('/forgot', methods=['GET'])
def serveForgot():
	return render_template('/recover.html')

@app.route('/locationDetails', methods=['GET'])
def serveDetails():
	locKey = request.args.get('locationID')
	return render_template('/locationdetails.html',myLocationKey=locKey)
#endregion
'''

def getURL():
	myKey = Credential.get_places_key()
	apiString = "https://maps.googleapis.com/maps/api/js?v=3.exp&key={keyVal}&sensor=false&libraries=places".format(keyVal=myKey)
	return apiString

