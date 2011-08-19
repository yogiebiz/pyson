
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
    COMMA = 9
    
    def __init__(self, kind, text):
        self.kind = kind
        self.text = text
    def __str__(self):
        return str(self.kind)
    
    @property
    def text(self):
        return self.text
    
    @property
    def kind(self):
        return self.kind
    
class Tokenizer:
    def __init__(self,jsonString):
        self.idx = 0
        self.jsonString = jsonString.strip()
    
    def tokenize(self):
        exit = False
        result = []
        
        while not exit:        
            if self.jsonString[self.idx] == '{':
                result.append(self._processLeftCurly())
            elif self.jsonString[self.idx] == '}':
                result.append(self._processRightCurly())
            elif self.jsonString[self.idx] == '"':                
                result.append(self._processString())
            elif self.jsonString[self.idx] == '[':                
                result.append(self._processLeftBracket())
            elif self.jsonString[self.idx] == ']':                
                result.append(self._processRightBracket())
            elif self.jsonString[self.idx] == ':':                
                result.append(self._processColon())    
            elif self.jsonString[self.idx] == 't':                
                result.append(self._processTrue())
            elif self.jsonString[self.idx] == 'f':                
                result.append(self._processFalse())
            elif self.jsonString[self.idx] == 'n':                
                result.append(self._processNull())        
            elif self.jsonString[self.idx] == ',':                
                result.append(self._processComma())
            elif self.jsonString[self.idx] == ' ':
                self._increaseIndex()
            if self._isOnEndOfString():
                exit = True        
        return result        
            
    def _processLeftCurly(self):
        self._increaseIndex()
        return JsonToken(JsonToken.LCURLY, '{')
    
    def _processRightCurly(self):
        self._increaseIndex()
        return JsonToken(JsonToken.RCURLY, '}')
    
    def _processLeftBracket(self):
        self._increaseIndex()
        return JsonToken(JsonToken.LBRACKET, '[')
        
    def _processRightBracket(self):
        self._increaseIndex()
        return JsonToken(JsonToken.RBRACKET, ']')    
        
    def _processColon(self):
        self._increaseIndex()
        return JsonToken(JsonToken.COLON, ':')    
    
    def _processComma(self):
        self._increaseIndex()
        return JsonToken(JsonToken.COMMA, ',')
        
    def _processString(self):
        charList = []        
        nextChar = self._getNextChar()
        while not nextChar == '"':                        
            charList.append(self.jsonString[self.idx])            
            nextChar = self._getNextChar()
        self._increaseIndex()
        return JsonToken(JsonToken.STRING, ''.join(charList))
        
    def _processTrue(self):
        trueVal = self.jsonString[self.idx:self.idx+4]
        if trueVal == 'true':
            self.idx += 4
            return JsonToken(JsonToken.BOOLEAN, 'true')
        else:
            raise ScanError(self.idx)
    
    def _processFalse(self):
        falseVal = self.jsonString[self.idx:self.idx+5]
        if falseVal == 'false':
            self.idx += 5
            return JsonToken(JsonToken.BOOLEAN, 'false')
        else:
            raise ScanError(self.idx)
    
    def _processNull(self):
        nullVal = self.jsonString[self.idx:self.idx+4]
        if nullVal == 'null':
            self.idx += 4
            return JsonToken(JsonToken.NULL, 'null')
        else:
            raise ScanError(self.idx)
    
    def _isInteger(self, val):
        try:
            int(val)
            return True
        except ValueError:
            return False
        
    def _increaseIndex(self):
        self.idx = self.idx + 1
    
    def _getNextChar(self):
        if (self.idx + 1) < len(self.jsonString):
            self._increaseIndex()
            return self.jsonString[self.idx]
        else : 
            raise ScanError()
        
    def _isOnEndOfString(self):
        return self.idx == len(self.jsonString)
        
class ScanError(Exception):
    def __init__(self, charNum=0):
        self.charNum = charNum
