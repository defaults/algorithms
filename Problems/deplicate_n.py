#!/usr/bin/python

def dulicate(array):
	for i in xrange(len(array)):
		if array[abs(array[i])] >= 0:
			array[abs(array[i])] = -array[abs(array[i])]
		else:
			print abs(array[i])
			
x = [1,2,3,4,1,2,6]

dulicate(x)