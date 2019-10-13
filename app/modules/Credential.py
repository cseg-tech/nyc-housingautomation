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