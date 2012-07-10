#!/usr/bin/python

﻿ones = ["one", "two", "three", "four", "five",
	    "six", "seven", "eight", "nine"] # 1 - 9
teen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
		"sixteen", "seventeen", "eighteen", "nineteen"] # 10-19
tens = ["twenty", "thirty", "forty", "fifty",
		"sixty", "seventy", "eighty", "ninety"] # 20 - 90
hundred = len("hundred")
andLen = len("and")
onesLength = 0
nineNineLength = 0
hundredsLength = 0
for i in ones: # 1-9
	onesLength += len(i)
nineNineLength = onesLength
for i in teen: # 10 - 19
	nineNineLength += len(i)
for i in tens: # 20 - 99
	nineNineLength += 10*len(i) + onesLength
length = nineNineLength
for i in ones: # 100 - 999
	length += 100*len(i) + 100*hundred + 99*andLen + nineNineLength
length += len("onethousand")
print length
raw_input("Press any key to continue...")
