import requests
import datetime
import bs4
import re


def extractDate(element):
	return str(element).partition('data-date="')[2].partition('"')[0]

def extractTotalCommitCount(element):
	return int(str(element).partition('data-count="')[2].partition('"')[0])

def getLastCommits(pageHTML, dayCount):
	return [int(commit) for commit in re.findall('data-count="(\d+)', pageHTML)[dayCount * -1:]]

def grabCommits(user, since=None):
	commitInfo = {}
	totalCommits = 0
	urlVal = "https://github.com/users/{}/contributions".format(user)
	print urlVal
	res = requests.get(urlVal)
	commitInfo['year'] = sum(getLastCommits(res.text, 365))
	commitInfo['week'] = sum(getLastCommits(res.text, 7))
	commitInfo['day'] = sum(getLastCommits(res.text, 7))
	return commitInfo

def getTodayDate():
	return datetime.datetime.now().strftime("%Y-%m-%d")

#print grabCommits('theriley106', getTodayDate())
