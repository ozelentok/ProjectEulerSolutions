#!/usr/bin/python

﻿import math
def sumFactOf(num):
	fact = math.factorial(num)
	sum = 0
	while fact != 0:
		sum += fact%10
		fact /= 10
	return sum

print sumFactOf(100)
raw_input("Press any key to continue...")
