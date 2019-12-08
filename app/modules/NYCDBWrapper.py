import json
import datetime
import urllib.request
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
    token = Credential.get_nycdb_token()
    url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?$$app_token={}&&bbl={}".format(token,bbl)
    with urllib.request.urlopen(url) as r:
    	data = json.loads(r.read().decode(r.info().get_param('charset') or	 'utf-8'))
    return cleanComplaints(data)

def findDailyComplaints(bbl):
	start_date = datetime.datetime.now()
	end_date = datetime.datetime.now() + datetime.timedelta(1)
	start_date = start_date.strftime("%Y-%m-%d")
	end_date = end_date.strftime("%Y-%m-%d")
	start_date += "T00:00:00"
	end_date += "T00:00:00"
	findNewComplaints(bbl, start_date, end_date)
 
def findNewComplaints(bbl, start_date, end_date):
	token = Credential.get_nycdb_token()
	url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?$$app_token={}&&$where=created_date%20between%20%27{}%27%20and%20%27{}%27&&bbl={}".format(token,start_date, end_date, bbl)
	print(url)
	with urllib.request.urlopen(url) as r:
		data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

	return cleanComplaints(data)

def getBBL(building, street, borough):
	appID = Credential.get_nyc_appID()
	appKey = Credential.get_nyc_appKey()
	formatString = 'https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber='+building+'&street='+street+'&borough='+borough+'&app_id='+appID+'&app_key='+appKey;
	resp = requests.get(url=formatString)
	data = resp.json() # Check the JSON Response Content documentation below
	return (data['address']['bbl'])


def getSameComplaints(user_id):
    return None