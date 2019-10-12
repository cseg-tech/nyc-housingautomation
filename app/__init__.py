# Begin default packages
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, jsonify
import requests
import urllib
import json
import string, random, requests, hashlib

# Custom packages
from sendgrid.helpers.mail import Mail
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
from sendgrid import SendGridAPIClient

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
	path = 'apiKeys/sendgridKey.txt'
	myKey = 'noKey'
	with open(path, 'r') as myfile:
		myKey = myfile.read()
	return myKey

def get_nyc_appID():
	path = 'apiKeys/nyc-appID.txt'
	myKey = 'noKey'
	with open(path, 'r') as myfile:
		myKey = myfile.read()
	return myKey

def get_nyc_appKey():
	path = 'apiKeys/appKey.txt'
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

'''
sg_key = get_sg_key()

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
	print(email)
	print(password)
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
	result = "true"
	statusCode = "3" #Different statuses would symbolise different types of issues, while 0 would imply a successful login - used to update the frontend

	#Connect to DB and insert, and then change the values of result and status code accordingly
	user = db.users
	x = user.find_one({'email' : email})
	print(x)
	id_save = 00000
	if x:
		id_save = x['id']
		y = x['password']
		if password == y:
			statusCode = "0"
		else:
			statusCode = "1"
	else:
		statusCode = "2"
	resultJson = jsonify({"valid" : result, "status":statusCode, 'id':id_save})
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
	bbl = getBBL(building,street,borough)
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
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

def getBBL(building, street, borough):
	appID = get_nyc_appID()
	appKey = get_nyc_appKey()
	formatString = 'https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber='+building+'&street='+street+'&borough='+borough+'&app_id='+appID+'&app_key='+appKey;
	print(formatString)
	resp = requests.get(url=formatString)
	data = resp.json() # Check the JSON Response Content documentation below
	print(data['address']['bbl'])
	return (data['address']['bbl'])

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

def getURL():
	path = './apiKeys/placesKey.txt'
	myKey = 'noKey'
	with open(path, 'r') as myfile:
		myKey = myfile.read()
	apiString = "https://maps.googleapis.com/maps/api/js?v=3.exp&key={keyVal}&sensor=false&libraries=places".format(keyVal=myKey)
	return apiString

def getUIDComplaints(user_id):
	user = db.users
	x = user.find_one({'id' : user_id})
	if x:
		bbl = x['bbl']
		result = findAllComplaints(bbl)
		return result
	return "No Complaints Found"

def getAddress(UID):
	#Connect to DB and insert, and then change the values of result and status code accordingly
	user = db.users
	x = user.find_one({'id' : UID})
	return x['address']

def get_dataToken():
	path = './apiKeys/dataToken.txt'
	myKey = 'noKey'
	with open(path, 'r') as myfile:
		myKey = myfile.read()
	return myKey

def cleanComplaints(complaintData):
	open_complaints = []
	closed_complaints = []
	for complaint in complaintData:
		fresh = {}
		try:
			fresh['Date_Created'] = complaint['created_date']
		except:
			fresh['Date_Created'] = "N/A"
		try:
			fresh['Updated_On'] = complaint['resolution_action_updated_date']
		except:
			fresh['Updated_On'] = "N/A"
		try:
			fresh['Description'] = complaint['resolution_description']
		except:
			fresh['Description'] = "N/A"
		if(complaint['status'] == 'Closed'):
			closed_complaints.append(fresh)
		else:
			open_complaints.append(fresh)
	return [open_complaints, closed_complaints, len(open_complaints)+len(closed_complaints)]

def findAllComplaints(bbl):
	token = get_dataToken()
	url = "https://data.cityofnewyork.us/resource/fhrw-4uyv.json?$$app_token={}&&bbl={}".format(token,bbl)
	r = urllib.urlopen(url)
	data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
	return cleanComplaints(data)