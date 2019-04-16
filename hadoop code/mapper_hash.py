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
		line_object=json.loads(line)
		a=line_object['entities']['hashtags']
		if a:
			hashtags=[a[i]['text'] for i in range(len(a))]
			for tag in hashtags:
				hashtext=tag
				value=1
				print "{0}\t{1}".format(hashtext, value)
		
	except:
		continue

