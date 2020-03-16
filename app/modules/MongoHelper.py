
'''
Helper file for all Mongo queries
'''

# Begin default packages
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, jsonify
import requests
import urllib
import json
import datetime
import string, random, requests, hashlib

# Custom packages
from sendgrid.helpers.mail import Mail
import pymongo
from apscheduler.schedulers.blocking import BlockingScheduler
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from ..modules import NYCDBWrapper as NYCDBWrapper
from ..modules import Credential as Credential
from . import Communications 


#connect to local MongoDB
def init_Mongo():
    uname = Credential.getMongoID()
    password = Credential.getMongoPass()
    string = "mongodb+srv://{}:{}@cluster1-smxun.mongodb.net/test?retryWrites=true&w=majority".format(uname, password)
    mongo = pymongo.MongoClient(string)
    db = mongo["userdata"]
    col = db["nycauto"]
    return (db, col)

#get sendgrid key
key = Credential.get_sg_key()

def iterate_all_users(db, col):
    
    returnData = {}

    for x in col.find():

        complaints = getUIDNewComplaints(db, col, x)
        if complaints:
            open_complaints = complaints[0]
            closed_complaints = complaints[1]
            number = complaints[2]

            emaillist = list(x['email'])

            returnData["open_complaints"] = open_complaints
            returnData["closed_complaints"] = closed_complaints
            returnData["number"] = number

        if returnData:
            Communications.send_email(key, emaillist, '311 Notification – New Complaint(s) Filed', returnData)


#remove user from database (only for unit testing purposes)
def DB_remove_user(col, email):
    cursor = col.find({'email': email})
    for x in cursor:
        # print("removing email")
        col.delete_one({"email": email})
        break

#login user to database
def DB_login_user(db, col, email, password):
    '''
    Connect to DB and insert, and then change the values of result and status code accordingly
    Status Codes: 0 => success, 1=> invalid password, 2=> invalid email
    '''
    result = 0
    cursor = col.find_one({'email': email})
    
    statusCode = 1
    id = None

    print((list(cursor)))
    print(len(list(cursor)))
    if not (cursor):
        return jsonify({"status":2, "id":None})

    x = cursor
    emailList = [x['email']]

    if password==x['password']:
        statusCode=0
        id = x['id']

    return jsonify({"status":statusCode, "id":id})

#register user to database
def DB_register_user(db, col, id, email, password, address, bbl):
    result = 0
    statusCode = "0"
    #Connect to DB and insert, and then change the values of result and status code accordingly

    # Status code == 1 implies that an id with that email already exists
    # print(email)
    cursor = col.find({'email': email})
    for x in cursor:
        # print("iterating through cursor")
        if x:
            # print("register user failed or exists")
            statusCode = "1"
            resultJson = jsonify({"valid" : result, "status" : statusCode})
            return resultJson

    result = 1
    emailList = [email]
    col.insert_one({'email': email, 'password': password, 'address': address, 'id': id, 'bbl':bbl})
    # print("user inserted into database")
    #test sendgrind
    Communications.send_email(key, emailList, 'Successful Registration', 'Thank you for signing up to HousingAlertNYC!')
    
    resultJson = jsonify({"valid" : result, "status" : statusCode})
    return resultJson

#get other building complaints for a given user id
def getUIDComplaints(db, col, user_id):
    cursor = col.find({'id' : user_id})
    for x in cursor:
        bbl = x['bbl']
        result = NYCDBWrapper.findAllComplaints(bbl)
        return result
    return "No Complaints Found"

#get complaints for a given user based on the current date 
def getUIDNewComplaints(db, col, doc):
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now() + datetime.timedelta(1)
    #start_date = start_date.strftime("%m/%d/%Y")
    #end_date = end_date.strftime("%m/%d/%Y")
    
    bbl = str(doc['bbl'])
    print(bbl)
    result = NYCDBWrapper.findDailyComplaints(bbl)
    return result

    #return "No Complaints Found"

#get address for a given user ID
def getAddress(db, col, UID):
    #Connect to DB and insert, and then change the values of result and status code accordingly
    cursor = col.find({'id' : UID})
    for x in cursor:
        return x['address']
