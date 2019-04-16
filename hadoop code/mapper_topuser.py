#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import json


for line in sys.stdin:
	try:
		data = json.loads(line)
		username=data['user']['name']
		followers_count=data['user']['followers_count']
		print "{0}\t{1}".format(username, followers_count)
	except:
		continue

