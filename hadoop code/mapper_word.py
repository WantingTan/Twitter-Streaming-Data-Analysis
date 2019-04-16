#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import json
import re
import string

#from wordcloud import WordCloud, STOPWORDS
#import nltk
#from nltk.corpus import stopwords
path='./stopwords.txt'
stopwords=[]
wordfile=open(path,"r")

for line in wordfile:
	word=line.split('\n')
	stopwords.append(word[0])

for line in sys.stdin:
	try:
		line_object=json.loads(line)
		a=line_object['text']
		result=re.sub(r'@\S+|http\S+|RT|#\S+','', a)
		words=[word.lower() for word in re.split(r'\W+', result) if word.isalpha()]	
		clean_words=[w for w in words if not w in stopwords]

		for i in clean_words:
			word=i
			value=1
			print "{0}\t{1}".format(word, value)
		
	except:
		continue

