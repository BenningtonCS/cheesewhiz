#!/usr/bin/env python

import os

# Simulated input parameter in the form of what we should get from read whizzifest
datain = [['zombie', '/data/gfsbin/goawway'],['icecream', '/usr/bin/stahp'],['settlersofcatan', '/data/settlers/saved']]


# runs the unix script to output the results of top into top.txt
os.system("top -n 1 -b > top.txt")


# create an empty list to be populated with the results of parsing top.txt
tst = []

# from top.txt, parse each line to get the name of the process and append it to the empty list created above
with open('top.txt', 'r') as input:
	for line in input:
		newline = line.split(' ')
		tst.append(newline[-1].strip())

# create an empty list to be populated by the subset of all processes which are not running
notrunning = []

# check to see if the processes from the input match the processes running. Output the destination of processes that are not running
for item in datain:
	if item[0] not in tst:
		notrunning.append(item[1])


# visibility of results for testing purposes
print tst
print notrunning


