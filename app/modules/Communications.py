# Begin default packages
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, jsonify
import requests
import urllib
import json
import string, random, requests, hashlib

# custom packages
from sendgrid import SendGridAPIClient


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





