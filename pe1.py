#!/usr/bin/python

sum = 0
for i in range(3, 1000):
	if i % 3 == 0:
		sum += i
	elif i % 5 == 0:
		sum += i
tf = open("pe1.txt", "w")
st1 = str(sum)
tf.write(st1)
tf.close()
print "saved to file"
raw_input()
