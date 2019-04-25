#!/usr/bin/python3.7
#region --Import Packages--

'''
SETUP:
 - Navigate to project directory on terminal, ensure that depeendancies are installed
 - Install needed pip3/pip packages: try running the script to see which ones are needed, 
 	it should just throw an error that says could not find package - that means you need to use pip to get that package
 - export FLASK_APP=flask_server.py
 - python3 -m flask run (or just flask run, if your default is python3)
'''
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response

from flask_pymongo import PyMongo

import hashlib

app = Flask(__name__)
#COMMENT OUT THE NEXT LINE BEFORE PRODUCTION
app.config['TEMPLATES_AUTO_RELOAD'] = True

#PyMongo connects to the MongoDB server running on port 27017 on localhost, to the database
#named myDatabase
path = './apiKeys/mongoURI.txt'
myURI = ''
with open(path, 'r') as myfile:
	myURI = myfile.read()
app.config["MONGO_URI"] = myURI
mongo = PyMongo(app)

#Begin Helper Routes
@app.route('/loginUser', methods=['POST'])
def loginUser():
	email = request.form['email']
	password = request.form['password']
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
	result = "true"
	statusCode = "0" #Different statuses would symbolise different types of issues, while 0 would imply a successful login - used to update the frontend
	#Connect to DB and insert, and then change the values of result and status code accordingly
	resultJson = jsonify({"valid" : result, "status":statusCode})
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
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
    address = request.form['address']
	result = "true"
	statusCode = "0"
	#Connect to DB and insert, and then change the values of result and status code accordingly

    user = mongo.db.users
    x = user.find_one({'email' : email})
    if x:
        statusCode = "1"
    else:
        user.insert({'email': email, 'password': password, 'address': address})
    
	resultJson = jsonify({"valid" : result, "status":statusCode})
	'''
	Status Codes:
	0 - Sucessful
	1 - Email ID already exists
	2 - Unforseen error'''
	return resultJson

@app.route('/retrieveAddressList', methods=['POST'])
def getAddressList():
	#Retrieve a list of addresses for user suggestions
	return "Placeholder"

@app.route('/getUserStatus', methods=['POST'])
def getUserStatus(email):
#get passed user id -> call getUserAddress to find address,
#query NYCDB to see other complaints of same address -> return JSON
	userAddress = getUserAddress(email)
	complaints = getSameComplaints(userAddress)
	return "Placeholder"

@app.route('/getUserAddress', methods=['GET'])
def getUserAddress(email):
    #query MongoDB to find address
    user = mongo.db.users
    x = user.find_one({'email' : email})
    if x:
    	output = x['address']
    else:
    	output = "Does not exist"
    return output

@app.route('/resetUserPassword', methods=['POST'])
def resetPassword():
	email = request.form['email']
	statusCode = "0"
	return {"status" : statusCode}
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
	getMyURL=getURL()
	return render_template('/mainpage.html',myKeyURL=getMyURL)

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

def getSameComplaints(userAddress):
	return None;
