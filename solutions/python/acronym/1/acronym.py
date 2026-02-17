import re

def abbreviate(words):
    cleaned_words = words.replace('-', ' ').replace('_', ' ')
    
    word_list = re.findall(r"[A-Za-z']+", cleaned_words)
    
    acronym = ""
    for word in word_list:
        acronym += word.lstrip("'")[0].upper()
        
    return acronym