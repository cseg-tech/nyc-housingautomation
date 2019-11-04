# Begin default packages
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, Response, jsonify
import requests
import urllib
import json
import string, random, requests, hashlib

# custom packages
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(key, to, subject, content): # @param to: list of emails; @param content: html string message
	
	sg = SendGridAPIClient(key)
	for email in to:
		print(email)
		try:
			#To be updated with correct email IDs - currently just the demo code
			message = Mail(from_email="chenrykang@gmail.com",to_emails = email,subject=subject,html_content=content)
			response = sg.send(message)
			print(response.status_code)
			print(response.body)
			print(response.headers)
		except Exception as e:
			print(e.message)





