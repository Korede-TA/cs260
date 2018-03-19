#!/usr/bin/python
import sys
import collections

class Node:
	def __init__(self):
		self.cargo = None
		self.nxt = None
		self.child = None

	def __str__(self):
		return str(self.cargo)

class myList:
	def __init__(self):
		self.head = None
		self.cur = None

def MAKENULL() :
	temp = myList()
	return temp

def FIRST(lst) :
	return lst.head

def END(lst) :
	if lst.head is None and lst.cur is None:
		return None
	else :
		temp = lst.head
		while temp.nxt:
			temp = temp.nxt
		return temp

def LOCATE(val, lst) :
	count = 0
	temp = FIRST(lst)
	while temp :
		if temp.cargo == val :
			return count
		else :
			count += 1
			temp = temp.nxt;
	return -1

def RETREIVE(pos, lst) :
	temp = FIRST(lst)
	for k in range(0, pos) :
		if temp.nxt != None :
			temp = temp.nxt
	return temp.cargo

def GETNODE(pos, lst) :
	temp = FIRST(lst)
	for k in range(0, pos) :
		if temp.nxt != None :
			temp = temp.nxt
	return temp

def NEXT(n) :
	return n.nxt

def PREVIOUS(n, lst) :
	temp = FIRST(lst)
	while temp :
		if temp.nxt == n :
			return temp
		else :
			temp = temp.nxt
	return None

def INSERT(val, pos, lst) :
	n = Node()
	n.cargo = val
	if pos is None :
		n.nxt = None
		lst.head = n
		lst.cur = lst.head
		return
	elif (pos == FIRST(lst) and FIRST(lst) != END(lst)) or (pos == 0):
		n.nxt = lst.head
		lst.head = n
		lst.cur = lst.head
		return
	else :
		if lst.head is None :
			lst.head = n
			lst.cur = n
		else :
			tmp = FIRST(lst)
			while tmp and pos > 1 :
				tmp = tmp.nxt
				pos -= 1
			n.nxt = tmp.nxt
			tmp.nxt = n
		return

def DELETE(pos, lst) :
	temp = FIRST(lst)
	if pos == 0 :
		lst.head = temp.nxt
	elif pos == END(lst) :
		if temp.nxt == None :
			lst = MAKENULL()
		else :
			while (temp.nxt).nxt :
				temp = temp.nxt
			temp.nxt = None
	else :
		while pos - 1 > 0 :
			temp = temp.nxt
			pos -= 1
		first = temp
		second = temp.nxt
		first.nxt = second.nxt
	lst.cur = lst.head

def printList(lst) :
	temp = FIRST(lst)
	if temp is None :
		print("empty")
	else :
		while temp :
			print(temp)
			temp = temp.nxt

def ADD_CHILD(letter, lst) :
	l = myList()
	n = Node()
	n.cargo = letter
	lst.child = l
	l.head = n
	l.cur = l.head
	return l

def ADD_WORD(word, lst) :
	global wc
	L = lst
	for letter in word :
		if L is not None :
			if LOCATE(letter, L) == -1 :
				INSERT(letter, END(L), L)
				for ltr in word[word.index(letter)+1:] :
					t = ADD_CHILD(ltr, L)
					L = t
				ADD_CHILD('$', L)
				wc += 1
				return lst
			else :
				L = GETNODE(LOCATE(letter, L), L).child
		else :
			L = MAKENULL()
			INSERT(letter, END(L), L)
			L = END(L)
			for ltr in word[word.index(letter)+1:] :
				t = ADD_CHILD(ltr, L)
				L = t
			ADD_CHILD('$', L)
			wc += 1
			return lst
	return lst

Trie = MAKENULL()

global wc
wc = 0
import sys
with open("alice30.txt") as f:
	for rawline in f :
		cleanline = rawline.strip().split(' ')
		for word in cleanline :
			Trie = ADD_WORD(word.lower(), Trie)
