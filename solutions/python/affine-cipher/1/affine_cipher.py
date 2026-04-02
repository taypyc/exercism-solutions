import math
import re

ALPHABET_SIZE = 26

def encode(plain_text, a, b):
    check_coprime(a)
    text = "".join(re.findall(r'[a-z0-9]', plain_text.lower()))
    
    encoded = []
    for char in text:
        if char.isdigit():
            encoded.append(char)
        else:
            index = ord(char) - ord('a')
            new_index = (a * index + b) % ALPHABET_SIZE
            encoded.append(chr(new_index + ord('a')))
            
    result = "".join(encoded)
    return " ".join(result[i:i+5] for i in range(0, len(result), 5))

def decode(cipher_text, a, b):
    check_coprime(a)
    
    text = cipher_text.replace(" ", "")
    a_inv = mod_inverse(a, ALPHABET_SIZE)
    
    decoded = []
    for char in text:
        if char.isdigit():
            decoded.append(char)
        else:
            index = ord(char) - ord('a')
            new_index = (a_inv * (index - b)) % ALPHABET_SIZE
            decoded.append(chr(new_index + ord('a')))
            
    return "".join(decoded)

def check_coprime(a):
    if math.gcd(a, ALPHABET_SIZE) != 1:
        raise ValueError("a and m must be coprime.")

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None