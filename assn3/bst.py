#!/usr/bin/python
import sys
import collections
from random import shuffle
from math import log


class node :
	def __init__(self, element=None, lc=None, rc=None) :
		self.element = element
		self.lc  = lc
		self.rc = rc

	def __str__(self) :
		return str(self.element)

def MEMBER(x, A) :
	if A is None :
		return False
	elif x == A.element :
		return True
	elif x < A.element :
		return MEMBER(x, A.lc)
	elif x > A.element :
		return MEMBER(x, A.rc)

def INSERT(x, A) :
	if A is None :
		A = node(x)
		A.lc = None
		A.rc = None
	elif x < A.element :
		if A.lc is not None :
			INSERT(x, A.lc)
		else :
			A.lc = node(x)
	elif x > A.element :
		if A.rc is not None :
			INSERT(x, A.rc)
		else :
			A.rc = node(x)
	return A

def DELETEMIN(A) :
	if A.lc is None :
		A = A.rc	
		return A.element
	else :
		return DELETEMIN(A.lc)

def DELETE(x, A) :
	if A is not None :
		if x < A.element :
			DELETE(x, A.lc)
		elif x > A.element :
			DELETE(x, A.rc)
		elif A.lc is None and A.rc is None :
			A = None	
		elif A.lc is None :
			A = A.rc
		elif A.rc is None :
			A = A.lc
		else :
			A.element = DELETEMIN(A.rc)

def LOCATE(x, A, i=0) :
	if A is None :
		return None
	elif x == A.element :
		return i
	elif x < A.element :
		return LOCATE(x, A.lc, i+1)
	elif x > A.element :
		return LOCATE(x, A.rc, i+1)

NUMLOOPS = 25
lengthList = []
avgList = []
lengthSum = 0
for i in range(1, NUMLOOPS+1) :
	MAXVALUE = 10 * i
	values = range(0, MAXVALUE)
	shuffle(values)
	BST = None
	for e in values :
		BST = INSERT(e, BST)
	for e in values :
		lengthSum += LOCATE(e, BST)
	avgList.append( float(lengthSum)/float(MAXVALUE) )
for i in range(NUMLOOPS) :
	print (i+1)*10, "\t\t", log((i+1)*10,2), "\t\t", avgList[i]
