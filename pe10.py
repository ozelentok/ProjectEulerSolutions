#!/usr/bin/python

import ozLib
sum = 0;
primes = ozLib.primesTo(2000000)
for i in primes:
	sum += i;
print sum


""" old version - less efficent way
﻿import math
def isPrime(num):
	for i in range(2, int(math.sqrt(num)+1)):
		if num%i == 0:
			return 0
	return 1

sum = 5
for i in range(5, 2000000, 2):
	if isPrime(i):
		sum += i
print sum
raw_input("press any key to continue...")
"""
