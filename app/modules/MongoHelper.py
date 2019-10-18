
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

from ..modules import NYCDBWrapper as NYCDBWrapper


#connect to local MongoDB
def init_Mongo():
    client = MongoClient('mongodb://localhost:27017')
    db = client.nycautomation
    return db

#login user to database
def DB_login_user(db, email, password, statusCode):
    #Connect to DB and insert, and then change the values of result and status code accordingly
    result = 0
    user = db.users
    x = user.find_one({'email' : email})
    print(x)
    id_save = 00000
    if x:
        id_save = x['id']
        y = x['password']
        if password == y:
            statusCode = "0"
            result = 1
        else:
            statusCode = "1"
    else:
        statusCode = "2"

    resultJson = jsonify({"valid" : result, "status":statusCode, 'id':id_save})

    return resultJson

#register user to database
def DB_register_user(db, id, email, password, address, bbl, statusCode):
    result = 0
    statusCode = "0"
    #Connect to DB and insert, and then change the values of result and status code accordingly

    # Status code == 1 implies that an id with that email already exists
    user = db.users
    x = user.find_one({'email' : email})
    if x:
        statusCode = "1"
    else:
        result = 1
        user.insert_one({'email': email, 'password': password, 'address': address, 'id': id, 'bbl':bbl})

    resultJson = jsonify({"valid" : result, "status" : statusCode})

    return resultJson

#get other building complaints for a given user id
def getUIDComplaints(db, user_id):
    user = db.users
    x = user.find_one({'id' : user_id})
    if x:
        bbl = x['bbl']
        result = NYCDBWrapper.findAllComplaints(bbl)
        return result
    return "No Complaints Found"


#get address for a given user ID
def getAddress(db, UID):
    #Connect to DB and insert, and then change the values of result and status code accordingly
    user = db.users
    x = user.find_one({'id' : UID})
    return x['address']


