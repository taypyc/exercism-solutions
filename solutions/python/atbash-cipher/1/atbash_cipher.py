import string

ALPHABET = string.ascii_lowercase
REVERSED = ALPHABET[::-1]
TRANS_TABLE = str.maketrans(ALPHABET, REVERSED)

def encode(plain_text):
    cleaned = "".join(c.lower() for c in plain_text if c.isalnum())
    ciphered = cleaned.translate(TRANS_TABLE)
    
    chunks = [ciphered[i:i + 5] for i in range(0, len(ciphered), 5)]
    return " ".join(chunks)

def decode(ciphered_text):
    cleaned = ciphered_text.replace(" ", "")
    
    return cleaned.translate(TRANS_TABLE)