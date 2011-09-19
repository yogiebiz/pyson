import unittest
from pyson.jsonparser import JsonParser


class ParserTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_parser(self):
        parser = JsonParser()
        
        text = "{}"
        result = parser.parse(text)
        self.assertEqual(result,{})        
        
        text = '{"a":1}'
        result = parser.parse(text)
        self.assertEqual(result,{"a":1})
        
        text = '{"a":"1"}'
        result = parser.parse(text)
        self.assertEqual(result,{"a":"1"})
        
        text = '{"a": false}'
        result = parser.parse(text)
        self.assertEqual(result,{"a":False})
        
        text = '{"a": true}'
        result = parser.parse(text)
        self.assertEqual(result,{"a":True})
        
        text = '{"a": null}'
        result = parser.parse(text)
        self.assertEqual(result,{"a":None})
        
        text = '{"a": true, "b": 1}'
        result = parser.parse(text)
        self.assertEqual(result,{"a":True, "b" : 1})
        
        text = '{"a": true, "b": 1, "c": "aha"}'
        result = parser.parse(text)
        self.assertEqual(result,{"a":True, "b" : 1, "c": "aha"})
        
        text = '{"a": true, "b": {"a" : 1, "b" : 2}}'
        result = parser.parse(text)
        self.assertEqual(result,{"a":True, "b" : {"a":1,"b":2}})
        