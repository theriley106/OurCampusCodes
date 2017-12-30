import csv
import json

information = {}
with open('schools.csv', 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)

with open('data.csv', 'rb') as f:
	reader = csv.reader(f)
	zipCodes = list(reader)

def convertZip(zipC):
	for z in zipCodes:
		if str(zipC) == str(z[0]):
			return (z[1], z[2])
	return None



for val in your_list:
	try:
		zipC = str(val[5]).partition('-')[0]
		print zipC
		longitude, latitude = convertZip(zipC)
		information[val[1]] = {}
		information[val[1]]['longitude'] = longitude
		information[val[1]]['latitude'] = latitude
		information[val[1]]['zip'] = zipC
	except Exception as exp:
		print exp


with open('data.json', 'w') as outfile:
    json.dump(information, outfile)