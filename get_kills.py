# TODO: post to slack following info: 
#   ship cost total
#   primary corp/alliance involved
#   total number involved in kill
#   link to killboard

import urllib2, json, gzip, csv
from StringIO import StringIO

req = urllib2.Request(
	url="https://zkillboard.com/api/kills/solarSystemID/30005295/solarSystemID/30005296/pastSeconds/30000/",
	data=None,
	headers={
		'User-Agent': 'https://zkillboard.com/ Maintainer: jack.schmandt@gmail.com',
		'Accept-Encoding': 'gzip'
	}
)

#response = urllib2.urlopen(req)
#buf = StringIO( response.read())
#f = gzip.GzipFile(fileobj=buf)
#data_unzipped = f.read()

#data = json.loads(data_unzipped)
#print data

#with open('sample.json', 'w') as outfile:
	#json.dump(data, outfile)
	
# use sample pull for testing	
json_data = open('sample.json').read()
data = json.loads(json_data)

num_kills = len(data)
print "num kills: ",num_kills

for i in range(0, num_kills):

	killTime = data[i]['killTime']
	print "Time:", str(killTime)

	zkbURL = "https://zkillboard.com/kill/" + str(data[0]['killID'])
	print "zKB URL:",zkbURL

	victim_info = data[i]['victim']
	print "Character Name: ", victim_info['characterName']

	shipTypeID = victim_info['shipTypeID']
	with open('typeids.csv') as typeids:
		reader = csv.reader(typeids)
		for row in reader:
			for field in row:
				if field == str(shipTypeID):
					print "Ship Type: ", row[1]
					break

	solarSystemID = data[i]['solarSystemID']
	with open('systemids.csv') as systemids:
		reader = csv.reader(systemids)
		for row in reader:
			for field in row:
				if field == str(solarSystemID):
					print "System: ", row[1]
					break
					
	print ""
	print ""

