#!/usr/bin/python

n = 100
sumOfSquares = (n * (n+1) * (2*n+1) )/6
squareOfSum = ((n * (n+1)) / 2) * ( (n*(n+1)) / 2)
diff = squareOfSum-sumOfSquares
print diff
raw_input("press any key to continue...")
