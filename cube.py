#! /usr/bin/python

from copy import deepcopy
import sys

class Cube:

	def __init__(self, Array):
		self.Array = Array 

	def print_cube(self):
		write = sys.stdout.write
		print("+----+")
		for i in range(0,4):	
			write("|")
			for j in range(0,4):
				write(self.Array[i][j])
			print "|"
		print "+----+----+----+----+"
		for i in range(4,8):
			write("|")
			for j in range(0,16):
				write(self.Array[i][j])
				if j == 3 or j == 7 or j == 11:
					write("|")
			print "|"
		print "+----+----+----+----+"
		for i in range(8,12):
			write("|")	
			for j in range(0,4):
				write(self.Array[i][j])
			print "|"
		print("+----+")

	def rotate_horizontally(self, line):
#		print "horizon"
		temp = self.Array[line][:]
		for i in range(0,16):
			self.Array[line][i] = temp[i - 4]
	
		if line == 4: self.matrix_permute_switch(0)
		elif line == 7: self.matrix_permute_switch(5)

	def rotate_vertically(self,line):
#		print "vertically"
		#initialize temp
		temp = [[0 for i in range(4)] for i in range(4)] 

		#copy from original to temp
		temp[0] = self.Array[3 - line][:] #first set
		for i in range(0,4):
			temp[1][i] = self.Array[i + 4][4 + line] #second set
			temp[2][i] = self.Array[8 + line][-1-i] #third set
			temp[3][3 - i] = self.Array[i + 4][15 - line] #fourth set

		#copy from temp to original 
		for i in range(0, 4):
			self.Array[4 + i][4 + line] = temp[0][i]
			self.Array[8 + line][3 - i] = temp[1][i]
			self.Array[7 - i][15 - line] = temp[2][i]
			self.Array[3 - line] = temp[3][:]

		if line == 0: self.matrix_permute_switch(1)
		elif line == 3: self.matrix_permute_switch(3)

	def rotate_vertically_2(self,line):
#		print "vertically_2"
		temp = [[0 for i in range(4)] for i in range(4)] 
	
		for i in range(0,4):
			temp[0][i] = self.Array[3 - i][3 - line] #first set
			temp[1][i] = self.Array[4 + i][8 + line] #second set
			temp[2][i] = self.Array[11 - i][3 - line] #third set
			temp[3][i] = self.Array[7 - i][3 - line] #fourth set
		
		for i in range(0, 4):
			self.Array[4 + i][8 + line] = temp[0][i]
			self.Array[11 - i][3 - line] = temp[1][i]
			self.Array[7 - i][3 - line] = temp[2][i]
			self.Array[3 - i][3 - line] = temp[3][i]
		
		if line == 0: self.matrix_permute_switch(2)
		elif line == 3: self.matrix_permute_switch(4)

	def matrix_permute_switch(self,dimension):
		if dimension == 0: self.matrix_permute(0,0,True)
		elif dimension == 1: self.matrix_permute(4,0,False)
		elif dimension == 2: self.matrix_permute(4,4,False)
		elif dimension == 3: self.matrix_permute(4,8,True)
		elif dimension == 4: self.matrix_permute(4,12,True)
		elif dimension == 5: self.matrix_permute(8,0,False)

	def matrix_permute(self,line,column,left):
		temp = deepcopy(self.Array)
		for i in range(0, 4):
			for j in range(0, 4):
				if left:
					self.Array[j + line][i + column] = temp[i + line][column + 3 - j]
				else:
					self.Array[j + line][column + 3 - i] = temp[i + line][column + j]


