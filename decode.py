#! /usr/bin/python
import sys

f = open('poster.txt',"rb")
write = sys.stdout.write
while True:
	buf=f.read(8)	
	if not buf or not buf.isdigit():
		break
	write(chr(int(buf,2)))
f.close()
