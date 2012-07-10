#!/usr/bin/python

import math
number = int(math.pow(2, 1000))
sum = 0
while number > 0:
	sum += number % 10
	number /= 10
print sum
raw_input("Press any key to continue...")
