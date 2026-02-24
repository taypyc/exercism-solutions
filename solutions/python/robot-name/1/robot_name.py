import random
import string

class Robot:
    _used_names = set()

    def __init__(self):
        self._name = None

    @property
    def name(self):
        if self._name is None:
            self._name = self._generate_unique_name()
        return self._name

    def _generate_unique_name(self):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            numbers = ''.join(random.choices(string.digits, k=3))
            candidate = letters + numbers
            
            if candidate not in Robot._used_names:
                Robot._used_names.add(candidate)
                return candidate

    def reset(self):
        old_name = self._name
        
        self._name = self._generate_unique_name()
        
        if old_name:
            Robot._used_names.remove(old_name)