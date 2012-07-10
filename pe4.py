#!/usr/bin/python

﻿def isPali(x):
	string = str(x)
	length = len(string)
	for i in range(0, length/2):
		if(string[i] != string[length-1-i]):
			return 0
	return 1

paliMax = 0
num = 0
maxI = 0
maxJ = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		num = i*j
		if isPali(num):
			if num > paliMax:
				maxI = i
				maxJ = j
				paliMax = num
print paliMax
print "i = ", maxI
print "j = ", maxJ
raw_input("Press any key to continue...")
	
