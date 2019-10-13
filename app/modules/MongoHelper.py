
'''
Helper file for all Mongo queries
'''

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


#connect to local MongoDB
def init_Mongo():
    client = MongoClient('mongodb://localhost:27017')
    db = client.nycautomation
    return db

#login user to database
def DB_login_user(db, email, password, statusCode):
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

    return resultJson

#register user to database
def DB_register_user(db, id, email, password, address, bbl, statusCode):
    #Connect to DB and insert, and then change the values of result and status code accordingly
    user = db.users
    x = user.find_one({'email' : email})
    if x:
        statusCode = "0"
    else:
        user.insert_one({'email': email, 'password': password, 'address': address, 'id': id, 'bbl':bbl})

    resultJson = jsonify({"valid" : result, "status" : statusCode})

    return resultJson

#get other building complaints for a given user id
def getUIDComplaints(db, user_id):
    user = db.users
    x = user.find_one({'id' : user_id})
    if x:
        bbl = x['bbl']
        result = findAllComplaints(bbl)
        return result
    return "No Complaints Found"


#get address for a given user ID
def getAddress(db, UID):
    #Connect to DB and insert, and then change the values of result and status code accordingly
    user = db.users
    x = user.find_one({'id' : UID})
    return x['address']



#-----------helper functions---------------

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



