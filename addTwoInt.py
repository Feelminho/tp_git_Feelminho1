#!/bin/python3

import sys

def add (a,b):
	return (a+b)

def main ():
	a = int (sys.argv [1])
	b = int (sys.argv [2])
	print (add(a,b))

main ()
