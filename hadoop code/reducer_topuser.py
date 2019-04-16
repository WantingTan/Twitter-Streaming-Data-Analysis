#!/usr/bin/python

import sys

follower = 0
oldKey = None
userDict={}
slist=[]
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisFollow = data_mapped

    if oldKey and oldKey != thisKey:
	if len(userDict)<15:
		userDict[oldKey]=follower
 		slist=sorted(userDict.items(),key=lambda kv:(-kv[1],kv[0]))[:15]
	elif userDict.pop(slist[len(slist)-1][0])<follower:
		userDict[oldKey]=follower
 		slist=sorted(userDict.items(),key=lambda kv:(-kv[1],kv[0]))[:15]

        oldKey = thisKey;
        follower = 0

    oldKey = thisKey
    if int(thisFollow) > follower:
    	follower = int(thisFollow)

for i in slist:
	print ("{0:20} {1}".format(i[0],i[1]))

