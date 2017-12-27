import requests
import datetime
import bs4


def extractDate(element):
	return str(element).partition('data-date="')[2].partition('"')[0]

def extractCommitCount(element):
	return int(str(element).partition('data-count="')[2].partition('"')[0])

def grabCommits(user, since=None):
	totalCommits = 0
	res = requests.get("https://github.com/users/{}/contributions".format(user))
	page = bs4.BeautifulSoup(res.text, 'lxml')
	for val in page.select(".day"):
		if since != None:
			if extractDate(val) > since:
				totalCommits = totalCommits + extractCommitCount(val)
		else:
			totalCommits = totalCommits + extractCommitCount(val)
	return totalCommits



def getTodayDate():
	return datetime.datetime.now().strftime("%Y-%m-%d")

print grabCommits('theriley106', '2017-07-24')
