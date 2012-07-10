#!/usr/bin/python

import ozLib
import math
primes = ozLib.primesTo(int(math.sqrt(600851475143)))
maxPrime = 0
product = 1
i = -1
while product < 600851475143:
		i += 1
		if 600851475143 % primes[i] == 0:
			maxPrime = primes[i]
			product *= maxPrime
print maxPrime
raw_input()



""" - less efficent
﻿import math
import ozLib

maxPrime = 0
product = 1
i = 1
while product < 600851475143:
	i += 2
	if ozLib.isPrime(i) and 600851475143%i == 0:
		maxPrime = i
		product *= maxPrime
print i
print "finished"
raw_input()
"""
