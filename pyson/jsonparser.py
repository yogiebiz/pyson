import string
from tokenizer import Tokenizer


class JsonParser:
	def __init__(self):
		pass
	
	def parse(self,jsonString):
		tokenizer = Tokenizer()
		self.tokens = tokenizer.tokenize()
		self.idx = 0
	
	def _start(self):
		pass
	def _getCurrentToken(self):
		return self.tokens[self.idx]
	
	def _getNextToken(self):
		pass
		
	
class ParseError(Exception):
	def __init__(self,near=""):			
		self.near = near
	
	def __str__(self):
		return "Error near " + self.near 	