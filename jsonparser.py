import string

class JsonParser:
	def __init__(self):
		pass
	
	def parse(jsonString):
		pass
	
	def lexer(jsonString):
		pass
		
class JsonToken:
	STRING = 0
	NUMBER = 1
	LCURLY = 2
	RCURLY = 3
	LBRACKET = 4
	RBRACKET = 5
	COLON = 6
	BOOLEAN = 7
	NULL = 8
	
	def __init__(self, kind, text):
		self.kind = kind
		self.text = text
	def __str__(self):
		return str(self.kind)
	
class Tokenizer:
	def __init__(self,jsonString):
		self.idx = 0
		self.jsonString = jsonString.strip()
	
	def tokenize(self):
		exit = False
		result = []
		try:
			while not exit:		
				if self.jsonString[self.idx] == '{':
					result.append(self.processLeftCurly())
				elif self.jsonString[self.idx] == '}':
					result.append(self.processRightCurly())
				elif self.jsonString[self.idx] == '"':				
					result.append(self.processString())
				elif self.jsonString[self.idx] == '[':				
					result.append(self.processLeftBracket())
				elif self.jsonString[self.idx] == ']':				
					result.append(self.processRightBracket())
				elif self.jsonString[self.idx] == ':':				
					result.append(self.processColon())	
				elif self.jsonString[self.idx] == 't':				
					result.append(self.processTrue())
				elif self.jsonString[self.idx] == 'f':				
					result.append(self.processFalse())
				elif self.jsonString[self.idx] == 'n':				
					result.append(self.processNull())		
				elif self.jsonString[self.idx] == ' ':
					self.increaseIndex()
				if self.isOnEndOfString():
					exit = True
		except ScanError, e:
			print 'scan error'
			return []
		return result		
			
	def processLeftCurly(self):
		self.increaseIndex()
		return JsonToken(JsonToken.LCURLY, '{')
	
	def processRightCurly(self):
		self.increaseIndex()
		return JsonToken(JsonToken.RCURLY, '}')
	
	def processLeftBracket(self):
		self.increaseIndex()
		return JsonToken(JsonToken.LBRACKET, '[')
		
	def processRightBracket(self):
		self.increaseIndex()
		return JsonToken(JsonToken.RBRACKET, ']')	
		
	def processColon(self):
		self.increaseIndex()
		return JsonToken(JsonToken.COLON, ':')	
		
	def processString(self):
		charList = []		
		nextChar = self.getNextChar()
		while not nextChar == '"':						
			charList.append(self.jsonString[self.idx])			
			nextChar = self.getNextChar()
		self.increaseIndex()
		return JsonToken(JsonToken.STRING, string.join(charList,''))
		
	def processTrue(self):
		trueVal = self.jsonString[self.idx:self.idx+4]
		if trueVal == 'true':
			self.idx += 4
			return JsonToken(JsonToken.BOOLEAN, 'true')
		else:
			raise ScanError(self.idx)
	
	def processFalse(self):
		falseVal = self.jsonString[self.idx:self.idx+5]
		if falseVal == 'false':
			self.idx += 5
			return JsonToken(JsonToken.BOOLEAN, 'false')
		else:
			raise ScanError(self.idx)
	
	def processNull(self):
		nullVal = self.jsonString[self.idx:self.idx+4]
		if nullVal == 'null':
			self.idx += 4
			return JsonToken(JsonToken.NULL, 'null')
		else:
			raise ScanError(self.idx)
	
	def isInteger(self, val):
		try:
			int(val)
			return True
		except ValueError:
			return False
	def increaseIndex(self):
		self.idx = self.idx + 1
	
	def getNextChar(self):
		if (self.idx + 1) < len(self.jsonString):
			self.increaseIndex()
			return self.jsonString[self.idx]
		else : 
			raise ScanError()
		
	def isOnEndOfString(self):
		return self.idx == len(self.jsonString)
		
class ScanError(Exception):
	def __init__(self, charNum=0):
		self.charNum = charNum
			
			
if __name__ == '__main__' :
	tokenizer = Tokenizer('{"ahaha" : true}')
	result = tokenizer.tokenize()
	for i in range(len(result)):
		print result[i].text