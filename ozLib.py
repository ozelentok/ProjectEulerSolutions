# Filename: ozLib.py
import math

# returns list of all primes up to limit
# Uses the Sieve of Eratosthenes
# skips even numbers in list to increase efficiency
def primesTo(limit):
	list = range(3, limit+1, 2) # numbers list
	primes = [2] # primes list initialization
	length = len(list)  # length of numbers list
	for i in xrange(0, length): # scans numbers list for primes
		if not list[i]: # list[i] == 0
			continue # moves on to next cell
		primes.append(list[i]) # add number to primes list
		for t in range(1, (length-1-i)/list[i]+1): # marks every multiple of current prime number
			list[i+t*list[i]] = 0
	return primes

# Returns 1 if num is prime, 0 if not
# Uses Trial divison
def isPrime(num):
	for i in range(2, int(math.sqrt(num)+1)):
		if num%i == 0:
			return 0
	return 1

def primeFactorsOf(num):
	pirFact = []
	for i in primesTo(num):
		while num%i == 0:
			num /= i
			pirFact.append(i)
	return pirFact
		
	
# returns list of all primes up to limit
# using Sieve of Eratosthenes
# less efficent as this function generates even numbers
"""
def primesTo(limit):
	list = range(2, limit+1)
	primes = []
	for i in list:
		if not i:
			continue # moves on to next number
		primes.append(i)
		for t in range(2, limit/i+1):
			list[i*t-2] = 0
	return primes
"""
