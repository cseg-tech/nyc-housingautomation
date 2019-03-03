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
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Response
import hashlib

app = Flask(__name__)

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
	result = "true"
	statusCode = "0"
	#Connect to DB and insert, and then change the values of result and status code accordingly
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
def getUserStatus():
    #return JSON of 
	return "Placeholder"

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
	return render_template('/login.html')


@app.route('/signup', methods=['GET'])
def serveSignUp():
	return render_template('/signup.html')
#endregion
