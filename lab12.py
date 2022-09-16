#!/usr/bin/env python3
# Name: Amena Akbary
# Pledge :I pledge my honor the I have abided by the Stevens Honor System.
import random

def shuffledNumbers(n):
	if n < 0 :
		return []
	else:
		out = list(range(n))
		for i in range(n-1,1,-1):
			j =  random.randint(0,i)
			if j < i:
				temp = out[i]
				out[i] = out [j]
				out[j] = temp
		return out

print(shuffledNumbers(5))


def array_count9(nums):
	count = 0
	for i in range(0,len(nums),1):
		if nums[i] == 9:
			count = count+1
	return count

print(array_count9([1,2,9]))