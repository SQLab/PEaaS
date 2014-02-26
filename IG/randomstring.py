import string
import random



def randomstring(string_len):
	characters = string.ascii_letters# + string.punctuation + string.digits
	password=""
	for x in range(random.randint(1,string_len)):
    		password =password+"".join(random.choice(characters))
	return password

def randomstringdigit(string_len):
	characters = string.ascii_letters + string.punctuation + string.digits
	password = ""
	for x in range(random.randint(1,string_len)):
		password = password+"".join(random.choice(characters))
	return password

class VarString:
	def __init__(self):
		self._len = 20
		self._string = ''
		self._type = 'string'
	def gen_str(self):
		self._string = randomstring(self._len) 
	def set_len(self,_len):
		self._len=_len
	def get_str(self):
		return self._string

class VarStringDigit:
	def __init__(self):
		self._len = 20
		self._string = ''
		self._type = 'stringdigit'
	def gen_str(self):
		self._string = randomstringdigit(self._len)
	def gen_len(self,_len):
		self._len =_len
	def get_str(self):
		return self._string

