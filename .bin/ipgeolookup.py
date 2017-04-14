import csv
import sys
import requests
import osm_shortlink

def getlocation(ip):
	data = requests.get('http://freegeoip.net/csv/' + ip).text
	datalist = data.split(',')
	return datalist

def main():
	try:
		ip = sys.argv[1]
	except IndexError:
		print('You have to pass an ip as an argument!')
		sys.exit()
	info = getlocation(ip)
	latitude = info[8]
	longitude = info[9]
	map_link = osm_shortlink.short_osm(float(latitude), float(longitude), 5) + '?m'
	#maps_link = 'https://www.openstreetmap.org/#map=6/' + latitude + '/' + longitude + '?m' #+ ',30z'
	print('Country  : ' + info[2])
	print('Region   : ' + info[4])
	print('City     : ' + info[5])
	print('Location : ' + map_link)


if __name__ == '__main__':
	main()

#8.8.8.8,US,United States,CA,California,Mountain View,94035,America/Los_Angeles,37.3860,-122.0838,807
#https://www.openstreetmap.org/#map=5/51.509/-5.581
#	maps_link = 'http://google.com/maps/place/' + latitude + ',' + longitude #+ ',30z'

#/@48.3552056,-96.322799
##google.com/maps
#8,9
#
#