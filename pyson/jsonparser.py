import string
from tokenizer import Tokenizer
from tokenizer import JsonToken


class JsonParser:
	def __init__(self):
		pass
	
	def parse(self,jsonString):
		tokenizer = Tokenizer(jsonString)
		self.tokens = tokenizer.tokenize()
		self.idx = 0
		return self._start()
		
	def _processObject(self):
		token = self._getNextToken()
		obj = {}
		while True:
			if token.kind == JsonToken.RCURLY :
				break
			elif token.kind == JsonToken.COMMA:
				token = self._getNextToken()
				continue
			else:				
				if token.kind != JsonToken.STRING:
					raise ParseError()
				colonToken = self._getNextToken()
				if colonToken.kind != JsonToken.COLON:
					raise ParseError()
				self._getNextToken()
				val = self._processValue()
				obj.update({token.text : val})
				token = self._getNextToken()
		return obj
				
					
	def _processValue(self):
		token = self._getCurrentToken()
		if token.kind == JsonToken.LCURLY :
			return self._processObject()
		elif token.kind == JsonToken.LBRACKET:
			return self._processArray();
		elif token.kind == JsonToken.STRING :
			return token.text
		elif token.kind == JsonToken.NUMBER :
			return int(token.text)
		elif token.kind == JsonToken.BOOLEAN :
			return True if token.text == 'true' else False			
		elif token.kind == JsonToken.NULL:
			return None
				
	def _processArray(self):
		token = self._getNextToken()
		obj = []
		while True:
			if token.kind == JsonToken.RBRACKET :
				break
			elif token.kind == JsonToken.COMMA :
				token = self._getNextToken()
			else:
				val = self._processValue()
				obj.append(val)
				token = self._getNextToken()
		return obj
	
	def _start(self):
		jsonObject = self._processObject()
		return jsonObject
	
	def _getCurrentToken(self):
		return self.tokens[self.idx]
	
	def _getNextToken(self):
		self.idx += 1
		if self.idx < len(self.tokens):			
			return self.tokens[self.idx]
		else:
			raise ParseError()
	
class ParseError(Exception):
	def __init__(self,near=""):			
		self.near = near
	
	def __str__(self):
		return "Error near " + self.near 	