from pyson.jsonparser import JsonParser, ParseError

def parse(jsonString):
    jsonParser = JsonParser()
    try:
        return jsonParser.parse(jsonString)
    except ParseError:
        return None