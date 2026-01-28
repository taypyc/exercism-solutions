def is_pangram(sentence):
    sentence = sentence.lower()
    
    letters_found = {char for char in sentence if char.isalpha()}
    
    return len(letters_found) == 26