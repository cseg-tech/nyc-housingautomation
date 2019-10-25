# Begin default packages
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, jsonify
import requests
import urllib
import json
import string, random, requests, hashlib

# Imported packages
from sendgrid.helpers.mail import Mail
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
from sendgrid import SendGridAPIClient

# Custom modules
from .modules import MongoHelper
from .modules import NYCDBWrapper
from .modules import Communications
from .modules import Credential

app = Flask(__name__, static_folder="./static/dist", template_folder="./static")
# COMMENT OUT THE NEXT LINE BEFORE PRODUCTION
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = MongoHelper.init_Mongo()

#PyMongo connects to the MongoDB server running on port 27017 on localhost, to the database
#named myDatabase

'''path = './apiKeys/mongoURI.txt'
with open(path, 'r') as myfile:
	myURI = myfile.read()
app.config["MONGO_URI"] = myURI
mongo = PyMongo(app)'''

def get_sg_key():
	path = 'apiKeys/sendgridKey.txt'
	myKey = 'noKey'
	with open(path, 'r') as myfile:
		myKey = myfile.read()
	return myKey



'''
sg_key = Credential.get_sg_key()

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
	email = request.form['email']
	password = request.form['password']
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
	result = "true"
	statusCode = "3" #Different statuses would symbolise different types of issues, while 0 would imply a successful login - used to update the frontend

	resultJson = MongoHelper.DB_login_user(db, email, password, statusCode)
    
	print(resultJson)
	'''
	Status Codes:
	0 - Sucessful
	1 - Wrong Password
	2 - Email ID doesn't exist
	3 - Unforseen error'''
	
	return resultJson

@app.route('/registerUser', methods=['POST'])
def registerUser():
	email = request.form['email']
	password = request.form['password']
	building = request.form['building']
	street = request.form['street']
	address = building+" "+street
	borough = request.form['borough']
	print(email)
	bbl = NYCDBWrapper.getBBL(building,street,borough)
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
	result = "true"
	statusCode = "0"
	#id_hasher = hashlib.sha256()
	#id_hasher.update(.encode('utf8'))
	identifier = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

	resultJson = MongoHelper.DB_register_user(db, identifier, email, password, address, bbl, statusCode)
    
	return resultJson

@app.route('/getUserStatus', methods=['POST'])
def getUserStatus(email):
#get passed user id -> call getUserAddress to find address,
#query NYCDB to see other complaints of same address -> return JSON
	user_id = request.form['id']
	complaints = NYCDBWrapper.getSameComplaints(user_id)
	return complaints

@app.route('/resetUserPassword', methods=['POST'])
def resetPassword():
	email = request.form['email']
	statusCode = "0"
	return {"status" : statusCode}
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
	address = MongoHelper.getAddress(db, user)
	complaints = MongoHelper.getUIDComplaints(db, user)
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
