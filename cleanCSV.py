import csv
import json

information = {}
with open('schools.csv', 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)

for val in your_list:
	try:
		information[val[1]] = str(val[5]).partition('-')[0]
	except Exception as exp:
		print("Problem")


with open('data.json', 'w') as outfile:
    json.dump(information, outfile)