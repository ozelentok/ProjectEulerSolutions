#!/usr/bin/python

import ozLib

list = ozLib.primesTo(1000000)
print list[10000]
print "finished"
raw_input()


""" less efficent way
﻿import math
def isPrime(num):
	for i in range(2, int(math.sqrt(num)+1)):
		if num%i == 0:
			return 0
	return 1

found = 0
counter = 6
i = 13
primeMax = 0
while counter < 10000:
	i += 2
	if isPrime(i):
		counter += 1
while 1:
	i += 2
	if isPrime(i):
		primeMax=0
		counter += 1
		break
print i, "counter: ", counter
print "finished"
raw_input()
"""
