
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
import pymongo
from apscheduler.schedulers.blocking import BlockingScheduler
from sendgrid import SendGridAPIClient

from ..modules import NYCDBWrapper as NYCDBWrapper
from ..modules import Credential as Credential


#connect to local MongoDB
def init_Mongo():
    uname = Credential.getMongoID()
    password = Credential.getMongoPass()
    string = "mongodb+srv://{}:{}@cluster1-smxun.mongodb.net/test?retryWrites=true&w=majority".format(uname, password)
    mongo = pymongo.MongoClient(string)
    db = mongo["userdata"]
    col = db["nycauto"]
    return (db, col)

#login user to database
def DB_login_user(db, col, email, password, statusCode):
    #Connect to DB and insert, and then change the values of result and status code accordingly
    result = 0
    cursor = col.find({'email': email})
    
    id_save = 00000
    
    statusCode = "2" #email doesnt exist
    for x in cursor:
        print("iterating through cursor")
        if x:
            id_save = x['id']
            y = x['password']
            if password == y:
                statusCode = "0" # success
                result = 1
            else:
                statusCode = "1"# wrong pass
        break
    
    resultJson = jsonify({"valid" : result, "status":statusCode, 'id':id_save})

    return resultJson

#register user to database
def DB_register_user(db, col, id, email, password, address, bbl, statusCode):
    result = 0
    statusCode = "0"
    #Connect to DB and insert, and then change the values of result and status code accordingly

    # Status code == 1 implies that an id with that email already exists
    print(email)
    cursor = col.find({'email': email})
    for x in cursor:
        print("iterating through cursor")
        if x:
            print("register user failed or exists")
            statusCode = "1"
            resultJson = jsonify({"valid" : result, "status" : statusCode})
            return resultJson

    result = 1
    col.insert_one({'email': email, 'password': password, 'address': address, 'id': id, 'bbl':bbl})
    print("user inserted into database")
    
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


#get address for a given user ID
def getAddress(db, col, UID):
    #Connect to DB and insert, and then change the values of result and status code accordingly
    cursor = col.find({'id' : UID})
    for x in cursor:
        return x['address']
