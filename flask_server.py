#!/usr/bin/python3.7
#region --Import Packages--

'''
SETUP:
 - Navigate to project directory on terminal, ensure that depeendancies are installed
 - Install needed pip3/pip packages: try running the script to see which ones are needed, 
 	it should just throw an error that says could not find package - that means you need to use pip to get that package
 - export FLASK_APP=flask_server.py
 - run brew services start mongodb-community@4.0
 - python3 -m flask run (or just flask run, if your default is python3)
'''
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, jsonify

from pymongo import MongoClient

from apscheduler.schedulers.blocking import BlockingScheduler
from sendgrid import SendGridAPIClient
import urllib.request

from sendgrid.helpers.mail import Mail

import string, random, requests, hashlib

app = Flask(__name__)
#COMMENT OUT THE NEXT LINE BEFORE PRODUCTION
app.config['TEMPLATES_AUTO_RELOAD'] = True

#connect to local MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client.nycautomation

#PyMongo connects to the MongoDB server running on port 27017 on localhost, to the database
#named myDatabase

'''path = './apiKeys/mongoURI.txt'
with open(path, 'r') as myfile:
	myURI = myfile.read()
app.config["MONGO_URI"] = myURI
mongo = PyMongo(app)'''

def get_sg_key():
	path = './apiKeys/sendgridKey.txt'
	myKey = 'noKey'
	with open(path, 'r') as myfile:
		myKey = myfile.read()
	return myKey

def get_nyc_appID():
	path = './apiKeys/nyc-appID.txt'
	myKey = 'noKey'
	with open(path, 'r') as myfile:
		myKey = myfile.read()
	return myKey

def get_nyc_appKey():
	path = './apiKeys/appKey.txt'
	myKey = 'noKey'
	with open(path, 'r') as myfile:
		myKey = myfile.read()
	return myKey

def send_email(key, to, content):
	try:
		#To be updated with correct email IDs - currently just the demo code
		message = Mail(from_email='from_email@example.com',to_emails='to@example.com',subject='Sending with Twilio SendGrid is Fun',html_content='<strong>and easy to do anywhere, even with Python</strong>')
		sg = SendGridAPIClient(key)
		response = sg.send(message)
		print(response.status_code)
		print(response.body)
		print(response.headers)
	except Exception as e:
		print(e.message)


sg_key = get_sg_key()
# Test

'''
def cron_job():
	# Query each user, find out if anyone else has lodged complaints for thier BBL - if so, email them.
	emailNeeded = True
	if(emailNeeded):
		print("sending...")
		to = "example@email.com"
		content = "Hi"
		send_mail(sg_key, to, content)

scheduler = BlockingScheduler()
scheduler.add_job(cron_job, 'interval', hours=24)
scheduler.start()'''
#Ref: https://stackoverflow.com/questions/22715086/scheduling-python-script-to-run-every-hour-accurately


#Begin Helper Routes
@app.route('/loginUser', methods=['POST'])
def loginUser():
	email = "hello@hello.com"
	password = "hello"
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
	result = "true"
	statusCode = "3" #Different statuses would symbolise different types of issues, while 0 would imply a successful login - used to update the frontend

	#Connect to DB and insert, and then change the values of result and status code accordingly
	user = db.users
	x = user.find_one({'email' : email})
	print(x)

	if x:
		y = x['password']
		if password == y:
			statusCode = "0"
		else:
			statusCode = "1"
	else:
		statusCode = "2"

	resultJson = jsonify({"valid" : result, "status":statusCode, 'id':x['id']})
	'''
	Status Codes:
	0 - Sucessful
	1 - Wrong Password
	2 - Email ID doesn't exist
	3 - Unforseen error'''
	return resultJson

@app.route('/registerUser', methods=['POST'])
def registerUser():
	print("Hi!")
	#email = request.form['email']
	#password = request.form['password']
	email = "hello@hello.com"
	password = "hello"
	address = "Hi"
	bbl = 12345
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
	#address = request.form['address']
	result = "true"
	statusCode = "0"
	#id_hasher = hashlib.sha256()
	#id_hasher.update(.encode('utf8'))
	identifier = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

	#mydict = { "name": "John", "address": "Highway 37" }
	#x = mycol.insert_one(mydict)

	#Connect to DB and insert, and then change the values of result and status code accordingly
	user = db.users
	x = user.find_one({'email' : email})
	if x:
		statusCode = "0"
	else:
		user.insert_one({'email': email, 'password': password, 'address': address, 'id': identifier, 'bbl':bbl})

	resultJson = jsonify({"valid" : result, "status" : statusCode})
	return resultJson

@app.route('/getUserStatus', methods=['POST'])
def getUserStatus(email):
#get passed user id -> call getUserAddress to find address,
#query NYCDB to see other complaints of same address -> return JSON
	user_id = request.form['id']
	complaints = getSameComplaints(user_id)
	return complaints

@app.route('/resetUserPassword', methods=['POST'])
def resetPassword():
	email = request.form['email']
	statusCode = "0"
	return {"status" : statusCode}

@app.route('/getBBL', methods=['POST'])
def getBBL():
	appID = get_nyc_appID()
	appKey = get_nyc_appKey()
	houseNo = request.form['house']
	street = request.form['street']
	nycBorough = request.form['borough']
	myBBL = 000000
	formatString = 'https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber='+houseNo+'&street='+street+'&borough='+nycBorough+'&app_id='+appID+'&app_key='+appKey;
	contents = urllib.request.urlopen(formatString).read()
	result = {
		"bbl":contents
	}
	return jsonify(result)

#endregion

#Begin page-serve routes
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
	address = getAddress(user)
	complaints = getUIDComplaints(user)
	getMyURL=getURL()
	return render_template('/mainpage.html',myKeyURL=getMyURL, address=address, complaints=complaints)

@app.route('/forgot', methods=['GET'])
def serveForgot():
	return render_template('/recover.html')

@app.route('/locationDetails', methods=['GET'])
def serveDetails():
	locKey = request.args.get('locationID')
	return render_template('/locationdetails.html',myLocationKey=locKey)
#endregion

def getURL():
	path = './apiKeys/placesKey.txt'
	myKey = 'noKey'
	with open(path, 'r') as myfile:
		myKey = myfile.read()
	apiString = "https://maps.googleapis.com/maps/api/js?v=3.exp&key={keyVal}&sensor=false&libraries=places".format(keyVal=myKey)
	return apiString

def getUIDComplaints(user_id):
	user = db.users
	x = user.find({'id' : user_id})
	resultJson = {}
	if x:
		bbl = x['bbl']
		resultJson = findAllComplaints(bbl)
	return jsonify(resultJson)

def findAllComplaints(bbl):
	url = "https://data.cityofnewyork.us/resource/fhrw-4uyv.json"
	contents = urllib.request.urlopen(url).read()
	complaints = jsonify(contents)
	print(complaints)
	# Connect to NYCDB and get all complaints with that address
	return None

	
