#!/usr/bin/python

﻿found = 0
for a in range(1,400):
	if found:
		break
	for b in range(1, 500):
		if found:
			break
		for c in range(1, 999):
			if a+b+c == 1000 and a*a+b*b==c*c:
				found = 1
				print a, " ", b, " ", c
				print "a*b*c", a*b*c
				raw_input("press any key to continue...")
				break
if not found:
	print "didn't find"
