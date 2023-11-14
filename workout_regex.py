from re import findall
from json import loads

def extract_json_object(text):
    regex = r"(?s)\{[\s\S]*?\}"
    matches = findall(regex, text)
    json_object_as_string = matches[0]
    json_object_as_dictionary = loads(json_object_as_string)
    return json_object_as_dictionary
