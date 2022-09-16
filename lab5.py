#!/usr/bin/env python3
# Amena Akbary 09/30/2021
# I pledge my honor that I have abided by the Stevens Honor System
##
l1 = [1,2,3]
l2 = [4,5,6]
def dotProduct(l,k):
	if l == []:
		return 0.0
	else:
		return l[0]*k[0] + dotProduct(l[1:], k[1:])

def removeAll(e,l):
	if l == []:
		return []
	elif l[0] == e:
		return removeAll(e, l[1:])
	else:
		return [l[0]] + removeAll(e, l[1:])

lst = [55, 77, 42, 11, 42, 88]
print(removeAll(42,lst))

def geometricSeq(n,f,b):
	if n == 1:
		return b
	else:
		return b*(n-1)
	
print(geometricSeq(1, 2, 5))

def deepReverse(l):
	if l == []:
		return []
	elif isinstance(l[0], list) == True:
		return deepReverse(l[1:]) + [deepReverse(l[0])]
	else:
		return deepReverse(l[1:]) + [l[0]]
	
lst2=[1,[2,3],4]
print(deepReverse(lst2))