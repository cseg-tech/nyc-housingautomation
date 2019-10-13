import json
import urllib
import requests

from ..modules import Credential as Credential

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

def get_dataToken():
	path = './apiKeys/dataToken.txt'
	myKey = 'noKey'
	with open(path, 'r') as myfile:
		myKey = myfile.read()
	return myKey

def getBBL(building, street, borough):
	appID = Credential.get_nyc_appID()
	appKey = Credential.get_nyc_appKey()
	formatString = 'https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber='+building+'&street='+street+'&borough='+borough+'&app_id='+appID+'&app_key='+appKey;
	print(formatString)
	resp = requests.get(url=formatString)
	data = resp.json() # Check the JSON Response Content documentation below
	print(data['address']['bbl'])
	return (data['address']['bbl'])


def getSameComplaints(user_id):
    return None