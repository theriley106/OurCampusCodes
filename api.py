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

app = Flask(__name__)





@app.route('/', methods=['GET'])
def returnHackathons():
	colleges = []
	collegeLocations = json.load(open('static/collegeLocations.json'))
	returnInfo = []
	for val in collegeLocations.items()[:50]:
		colleges.append(val[0])
	for college in colleges:
		returnInfo.append({"schoolURL": url_for('returnSchoolInfo', schoolName=college.replace(' ', "_")), "schoolName": college, "Lat": collegeLocations[college]['latitude'], "Long": collegeLocations[college]['longitude']})
	return render_template("index.html", primaryDB=returnInfo)

@app.route('/commitBySchool/<schoolName>', methods=['GET'])
def returnSchoolInfo(schoolName):
	return "<h1>This Works</h1>"

@app.route('/addUser', methods=['POST'])
def addUser(database="static/Hackathons.csv"):
	postData = request.get_json(silent=True)
	schoolName = postData['schoolName']
	githubName = postData['githubName']
	personName = postData['personName']
	email = postData['submissionEmail']
	major = postData['majorName']
	userName = postData['userName']
	schoolURL = url_for('returnSchoolInfo', schoolName=schoolName.replace(' ', "_"))
	return jsonify(['school'])


def genLongLat(location):
	return str(geolocator.geocode(location)[1]).strip('(').strip(')')

def determineTeamQuality(member1, member2):
	a = diffBetween(member1, member2)
	return clf.predict([a[2]])


if __name__ == "__main__":

	#webbrowser.open("http://0.0.0.0:8888/hackathons")
	#webbrowser.open("http://0.0.0.0:8888/calc")
	#webbrowser.open("http://0.0.0.0:8888/map/hackGT2017")
	app.run(host='0.0.0.0', port=8000)
	#print determineTeamQuality('hlin3565', 'NicholasGreenwald')
	#print len(genAllPossible(genUserFromCsv()))
	#username = raw_input('Username: ')
	#print grabUser(username)
	#print grabHackathon()