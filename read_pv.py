#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
########################################################################
#
#	Version 2.1		neu: mit status abfrage
#
# sudo pip install lxml
# or
# python3 -m pip install lxml --user
#
########################################################################

#import sys
#import os
#import time
#from datetime import datetime
import urllib.request, urllib.parse, urllib.error

########################################################################
#
#	https://github.com/Tafkas/KostalPikoPy
#	http://libraries.io/pypi/pikopy
#
# CURRENT		data[0]	*
# TOTAL			data[1]	*
# DAILY			data[2]	*
# STRING1V		data[3] -
# L1V			data[4]
# STRING1A		data[5] -
# L1W			data[6]
# STRING2V		data[7] *
# L2V			data[8] *
# STRING2A		data[9] *
# L2W			data[10]
# L3V			data[11]
# L3W			data[12]
# ['2879', '7746', '10.97', '0', '226', '0.00', '962', '484', '228', '6.25', '958', '228', '959']
########################################################################
def readPV():
	import urllib.request, urllib.error, urllib.parse
	from lxml import html 	# sudo apt-get install python-lxml

	host = 'http://192.168.2.42'
	password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None, host, '***', '***')
	handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
	opener = urllib.request.build_opener(handler)
	opener.open(host)
	urllib.request.install_opener(opener)
	response = urllib.request.urlopen(host)
	#print(("response: ", response))
	root = html.fromstring(response.read().strip())
	data = [v.text.strip() for v in root.xpath("//td[@bgcolor='#FFFFFF']")]
	print(("data: ", data))
	if "x x x" in data[0]: # check if data is available
		data[0] = 0
		data[7] = 0
		data[9] = 0
	else:	# send only data, when available
		print(("current: ", data[0] ))
		print(("voltage: ", data[7] ))
		print(("power: ", data[9] ))
	print(("total: ", data[1] ))
	print(("daily: ", data[2] ))
	# status auslesen
	status = [v.text.strip() for v in root.xpath("//td[@colspan='4']")]
	print(("status: ", status[0]))
	return data


########################################################################
#
########################################################################
def main():
	# read PIKO42
	try:
		pv = readPV()
		pass
	except Exception as e:
		print(("Fehler: ", e))

########################################################################
#
########################################################################
if __name__ == "__main__":

	main()

