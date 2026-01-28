import re

def translate(text):
    words = text.split()
    result = []
    
    for word in words:
        if re.match(r'^([aeiou]|xr|yt)', word):
            result.append(word + "ay")
            
        elif match := re.match(r'^([^aeiou]*qu)(.*)', word):
            result.append(match.group(2) + match.group(1) + "ay")
            
        elif match := re.match(r'^([^aeiou]+)(y.*)', word):
            result.append(match.group(2) + match.group(1) + "ay")
            
        else:
            match = re.match(r'^([^aeiou]+)(.*)', word)
            result.append(match.group(2) + match.group(1) + "ay")
            
    return " ".join(result)