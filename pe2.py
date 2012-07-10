#!/usr/bin/python

termA, termB, sum = 1, 2, 0
while termB < 4000000:
	if termB % 2 == 0:
		sum += termB
	termA, termB = termB, termA + termB
print sum
raw_input("press any key to continue")
