import secrets
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = "".join(secrets.choice(string.ascii_lowercase) for _ in range(100))
        else:
            self.key = key

    def encode(self, text):
        return self._process(text, mode=1)

    def decode(self, text):
        return self._process(text, mode=-1)

    def _process(self, text, mode):
        result = []
        key_length = len(self.key)
        
        for i, char in enumerate(text):
            shift = ord(self.key[i % key_length]) - ord('a')
            
            char_pos = ord(char) - ord('a')
            new_pos = (char_pos + (mode * shift)) % 26
            
            result.append(chr(new_pos + ord('a')))
            
        return "".join(result)