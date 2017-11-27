import requests

def grabCommits(user):
	return requests.get("https://github.com/users/{}/contributions".format(user)).text
