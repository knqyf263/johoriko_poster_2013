#! /usr/bin/python

from copy import deepcopy
from cube import Cube
import sys

#define question array
c = Cube([
		["I","p","w","g"],
		["o",".",".","u"],
		["a","c","t","o"],
		["u","s","w","!"],
		[" ","u","i","l",	"o"," "," ","t",	"h","w", ":", " ",	"a", "k",".","y"],
		[" ","f","t"," ",	"S","-","t","o",	"n","w", "/", "r",	"_", "/","a","o"],
		["s","c","y","s",	"i","a","i"," ",	"o",".", "o", " ",	"_", "t","t","l"],
		["t","u","u","e",	"n","n","n",".",	"o","j", "k", "i",	"l", "k","."," "],
		["G","T","a","d"],
		["h","/","s","e"],
		["l","h"," ","r"],
		["C","S","p","F"],
			
	]) 
d = Cube(deepcopy(c.Array))



def rotate():
	test_str = "T,H,E,U,N,I,V,E,R,S,I,T,Y,O,F,T,O,K,Y,O"
#	test_str = "R"
#	print  test_str.split(",")
	for val in test_str.split(","):
		rotate_switch(val)

def rotate_switch(val):
	if val == "E": c.rotate_vertically(0)
	elif val == "F": c.rotate_vertically(1)
	elif val == "H": c.rotate_vertically(2)
	elif val == "I": c.rotate_vertically(3)
	elif val == "K": c.rotate_vertically_2(0)
	elif val == "N": c.rotate_vertically_2(1)
	elif val == "O": c.rotate_vertically_2(2)
	elif val == "R": c.rotate_vertically_2(3)
	elif val == "S": c.rotate_horizontally(4)
	elif val == "T": c.rotate_horizontally(5)
	elif val == "U": c.rotate_horizontally(6)
	elif val == "V" or val == "Y": c.rotate_horizontally(7)


print "####Before####"
c.print_cube()

for i in range(0,153):
	rotate()
	if c.Array == d.Array:
		print i
		break

print "####After####"
c.print_cube()
#print Array
