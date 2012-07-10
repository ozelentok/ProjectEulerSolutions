#!/usr/bin/python

﻿import ozLib
inc = 1
num = 0
found = 0
for prime in ozLib.primesTo(20):
	inc *= prime
while not found:
	num += inc
	for divider in range(2, 21):
		if(num%divider != 0):
			found = 0
			break
		found = 1
if found:
	print num
else:
	print "No number like that exists"
	
	
""" less efficent way
﻿i = 0
found = 0
while not found:
	i += 20
	for divider in range(2, 16):
		if(i % divider != 0):
			found = 0
			break
		found = 1
found = 0
inc = i
while not found:
	i += inc # found by using same program on smaller range
	for divider in range(2, 21):
		if(i%divider != 0):
			found = 0
			break
		found = 1
if found:
	print i
else:
	print "No number like that exists"
"""
