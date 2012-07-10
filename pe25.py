﻿#!/usr/bin/python

def digitsIn(num):
	digits = 0
	while num > 0:
		num /= 10
		digits += 1
	return digits

i = 2
termA, termB = 1, 1
digit = 0;
while digit != 1000:
	termA, termB = termB, termA+termB
	digit = digitsIn(termB)
	i += 1
print i
