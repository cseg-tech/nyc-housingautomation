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
     render_template, flash

app = Flask(__name__)

#Begin Helper Routes - You can define either a POST/GET route, and set it to a function which'll execute when that route is called
@app.route('/myRoute', methods=['POST'])
def identifyImage():
    return "Hello World"
#endregion
