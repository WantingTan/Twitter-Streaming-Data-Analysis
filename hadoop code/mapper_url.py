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
		a=line_object['entities']['urls']
		if a:
			urls=[a[i]['url'] for i in range(len(a))]
			for i in urls:
				url=i
				value=1
				print "{0}\t{1}".format(url, value)
		
	except:
		continue

