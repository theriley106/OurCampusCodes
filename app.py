#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import requests
import re
import bs4
import csv
import time
import os
import json
import re
import main
CLIENT_SECRET = open("client_secret.txt").read().strip()
CLIENT_ID = open("client_id.txt").read().strip()
SCHOOL_INFO = json.load(open("static/schools.json"))
app = Flask(__name__)


@app.route('/authGithub', methods=['GET'])
def authGithub():
	return redirect('https://github.com/login/oauth/authorize?response_type=code&client_id=b7ead49790c005829231&redirect_uri=https%3A%2F%2Fgoogle.com%2F')

def readDB(db='static/database.json'):
	return json.load(open(db))

def addUserToDB(dictfile, db='static/database.json'):
	database = json.load(open(db))
	print dictfile.items()[0][0]
	for val in database['users']:
		try:
			print str(val[dictfile.items()[0][0]]) + "already in db"
			return
		except Exception as exp:
			pass
	dictfile['joinDate'] = main.getTodayDate()
	database['users'].append(dictfile)
	with open(db, 'w') as outfile:
		json.dump(database, outfile)

def returnAllColleges(db='static/database.json'):
	return re.findall('schoolName\S\S\s\S([^"]*)', str(open(db).read()))

def returnCollegeLocations(college):
	locations = json.load(open('static/collegeLocations.json'))[college]
	return (locations['latitude'], locations['longitude'])

@app.route('/test', methods=['GET'])
def test():
	return render_template("testing.html")

@app.route('/', methods=['GET'])
def returnHackathons():
	colleges = []

	return render_template("index.html", primaryDB=SCHOOL_INFO)

@app.route('/commitBySchool/<schoolName>', methods=['GET'])
def returnSchoolInfo(schoolName):
	return "<h1>This Works</h1>"

@app.route('/addUser', methods=['POST'])
def addUser(database="static/Hackathons.csv"):
	information = {}
	postData = request.get_json(silent=True)
	#print postData
	githubName = postData['githubName']
	schoolName = postData['schoolName']
	schoolLat, schoolLong = returnCollegeLocations(schoolName)
	name = url_for('returnSchoolInfo', schoolName=str(schoolName).replace(' ', "_"))
	postData['schoolURL'] = name
	information[githubName] = postData
	addUserToDB(information)
	return jsonify(information)

def getAccessToken(code):
	url = "https://github.com/login/oauth/access_token?client_id={}&client_secret={}&code={}".format(CLIENT_ID, CLIENT_SECRET, code)
	print url
	res = requests.post(url)
	if 'error' in res.text.lower():
		return None
	try:
		return res.text.partition("access_token=")[2].partition("&")[0]
	except:
		return None

def getUserInfoFromAccessToken(accessToken):
	return requests.get("https://api.github.com/user?access_token={}".format(accessToken)).json()

@app.route("/register", methods=["POST", "GET"])
def register():
	code = request.args.get('code')
	print code
	return redirect(url_for('signupPage', accessToken=getAccessToken(code)))

@app.route("/buttonTest", methods=["POST", "GET"])
def registerz():
	return render_template("buttonTest.html")

@app.route("/signUp/<accessToken>", methods=["POST", "GET"])
def signupPage(accessToken):
	userInfo = getUserInfoFromAccessToken(accessToken)
	return render_template("signUp.html", userInfo=userInfo, schoolInfo=SCHOOL_INFO)

def genLongLat(location):
	return str(geolocator.geocode(location)[1]).strip('(').strip(')')



if __name__ == "__main__":

	#webbrowser.open("http://0.0.0.0:8888/hackathons")
	#webbrowser.open("http://0.0.0.0:8888/calc")
	#webbrowser.open("http://0.0.0.0:8888/map/hackGT2017")
	app.run()
	#print determineTeamQuality('hlin3565', 'NicholasGreenwald')
	#print len(genAllPossible(genUserFromCsv()))
	#username = raw_input('Username: ')
	#print grabUser(username)
	#print grabHackathon()
