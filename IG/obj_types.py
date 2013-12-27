#This code contains all (build-in) types of variables.
import random

class VarInt:
	def __init__(self):
		self.__val = 0        #defult value
		self.__max = 2**64    #default max
		self.__limit_max = None  #the limited max from the original max
		self.__max_flag = False
		self.__min = -(2**64) #default min
		self.__limit_min = None  #the limited min from the original min
		self.__min_flag = False
		self.__width = 0      #the width of range
		self.__base = 10      #base options: 2, 8, 10, 16
		self._type = 'int'    #read-only
	def set_max(self, _max):
		if self.__max_flag:
			if _max < self.__max:
				self.__max = _max
		else:
			self.__max = _max
			self.__max_flag = True
	def set_min(self, _min):
		if self.__min_flag:
			if self.__min < _min:
				self.__min = _min
		else:
			self.__min = _min
			self.__min_flag = True
	def set_base(self, base):
		pass
	def get_val(self):
		if self.__base == 2:
			pass
		elif self.__base == 8:
			pass
		elif self.__base == 10:
			return self.__val
		elif self.__base == 16:
			pass
	def gen_val(self, level):
		level = int(level)
		if self.__min < self.__max:
			self.__width = self.__max - self.__min
			self.__limit_max = int(0 + self.__width ** (level/3))
			if self.__limit_max > self.__max:
				self.__limit_max = self.__max
			self.__limit_min = int(0 - self.__width ** (level/3))
			if self.__limit_min < self.__min:
				self.__limit_min = self.__min
			self.__val = random.randint(self.__limit_min, self.__limit_max)
			return True
		else:
			return False
	def prime(self):  #generate a prime number value
		pass

class RelStmt:  #this class handles relation statements
	def _init_(self):
		self.l_operand = None #left object number
		self.r_operand = None #right object number
		self.operator = None  #operator type
		
