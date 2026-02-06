import re
from itertools import groupby

def encode(string):
    if not string:
        return ""
    
    result = []
    for char, group in groupby(string):
        count = len(list(group))
        result.append(f"{count if count > 1 else ''}{char}")
        
    return "".join(result)

def decode(string):
    matches = re.findall(r'(\d*)(.)', string)
    
    result = []
    for count, char in matches:
        n = int(count) if count else 1
        result.append(char * n)
        
    return "".join(result)