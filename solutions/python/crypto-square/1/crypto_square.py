import math

def cipher_text(plain_text):
    normalized = "".join(c.lower() for c in plain_text if c.isalnum())
    length = len(normalized)
    
    if length == 0:
        return ""

    c = math.ceil(math.sqrt(length))
    r = math.ceil(length / c)

    rows = [normalized[i:i + c] for i in range(0, length, c)]
    
    encoded_chunks = []
    for col_idx in range(c):
        chunk = ""
        for row in rows:
            if col_idx < len(row):
                chunk += row[col_idx]
            else:
                chunk += " "
        
        if len(chunk) < r:
            chunk += " " * (r - len(chunk))
            
        encoded_chunks.append(chunk)

    return " ".join(encoded_chunks)