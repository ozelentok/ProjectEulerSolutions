#!/usr/bin/python

import math
# Returns number of divisors of number
def numDivOf(num):
	counter = 0
	for i in range(2, int(math.sqrt(num))+1):
		if num%i == 0:
			counter += 1
	counter = counter*2 + 2
	return counter

sum = 28
found = 0
for d in range(8, 100000000):
	sum += d
	if numDivOf(sum) > 500:
		found = 1
		break
if found:
	print "first triangle number to have over 500 divisors: ", sum
else:
	print "no number"
raw_input("Press any key to continue...")
