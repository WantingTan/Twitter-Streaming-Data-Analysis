#!/usr/bin/python

import sys

hashTotal = 0
oldKey = None
hashDict={}
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

    thisKey, thisVal = data_mapped

    if oldKey and oldKey != thisKey:
	if len(hashDict)<15:
		hashDict[oldKey]=hashTotal
 		slist=sorted(hashDict.items(),key=lambda kv:(-kv[1],kv[0]))[:15]
	elif hashDict.pop(slist[len(slist)-1][0])<hashTotal:
		hashDict[oldKey]=hashTotal
 		slist=sorted(hashDict.items(),key=lambda kv:(-kv[1],kv[0]))[:15]

        oldKey = thisKey;
        hashTotal = 0

    oldKey = thisKey
    hashTotal += int(thisVal)

for i in slist:
	print ("{0:20} {1}".format(i[0],i[1]))

