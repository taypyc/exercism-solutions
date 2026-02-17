def rotate(text, key):
    result = []
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            
            new_char = chr((ord(char) - start + key) % 26 + start)
            result.append(new_char)
        else:
            result.append(char)
            
    return "".join(result)