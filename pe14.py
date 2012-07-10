#!/usr/bin/python

chainMax = 0
max = 0
orignalNum = 0
chain = 1
for i in range(3, 1000000):
	originalNum = i
	chain = 1
	while i != 1:
		if i%2:	#isn't divisible by 2
			i = 3*i + 1
		else:
			i /= 2
		chain += 1
	if chain > chainMax:
		chainMax = chain
		max = originalNum
print "starting number: ", max
print "chain: ", chainMax
raw_input("Press any key to continue...")
