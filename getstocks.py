#!/usr/bin/env python3
#
# ISIN  FR0000120628
# WKN   855705
# NAME  AXA.SA
# https://de.finance.yahoo.com/quote/CS.PA?p=CS.PA

import yfinance as yf
from datetime import datetime, date

def pushover(message):                         
	import http.client, urllib
	conn = http.client.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
		urllib.parse.urlencode({
			"token": "***",
			"user": "***",
			"message": message,
		}), { "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()

try:
	stock = yf.Ticker("FR0000120628")
	price = 'AXA.SA: %s EUR' % (stock.info['regularMarketPrice'])
except Exception as e:
	price = "error fetching stock data"
#print(price)
pushover(price)
