import unittest
from pyson.tokenizer import Tokenizer, JsonToken,ScanError

class TokenizerTest(unittest.TestCase):
    def setUp(self):
        pass 
    
    def test_tokenize(self):
        tokenizer = Tokenizer('"str"')
        tokens = tokenizer.tokenize()
        self.assertEqual(tokens[0].text,"str")
        self.assertEqual(tokens[0].kind, JsonToken.STRING)
        
        tokenizer = Tokenizer('{"str":"val","str"}')
        tokens = tokenizer.tokenize()
        self.assertEqual(tokens[0].text, "{")
        self.assertEqual(tokens[0].kind, JsonToken.LCURLY)
        self.assertEqual(tokens[1].text, "str")
        self.assertEqual(tokens[1].kind, JsonToken.STRING)
        self.assertEqual(tokens[2].text, ":")
        self.assertEqual(tokens[2].kind, JsonToken.COLON)
        self.assertEqual(tokens[3].text, "val")
        self.assertEqual(tokens[3].kind, JsonToken.STRING)
        self.assertEqual(tokens[4].text, ",")
        self.assertEqual(tokens[4].kind, JsonToken.COMMA)
        self.assertEqual(tokens[6].text, "}")
        self.assertEqual(tokens[6].kind, JsonToken.RCURLY)
        
        
        tokenizer = Tokenizer('{"aha:')
        self.assertRaises(ScanError, tokenizer.tokenize)            
        
        