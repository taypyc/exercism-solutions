from itertools import permutations
import re

def solve(puzzle):
    words = re.findall(r'[A-Z]+', puzzle)
    unique_letters = list(set("".join(words)))
    
    first_letters = set(word[0] for word in words if len(word) > 1)
    
    weights = {letter: 0 for letter in unique_letters}
    
    for word in words[:-1]:
        for i, char in enumerate(reversed(word)):
            weights[char] += 10**i
            
    for i, char in enumerate(reversed(words[-1])):
        weights[char] -= 10**i
        
    sorted_letters = sorted(unique_letters, key=lambda l: l in first_letters, reverse=True)
    first_indices = [i for i, l in enumerate(sorted_letters) if l in first_letters]
    weighted_values = [weights[l] for l in sorted_letters]

    for p in permutations(range(10), len(sorted_letters)):
        if any(p[i] == 0 for i in first_indices):
            continue
            
        if sum(p[i] * weighted_values[i] for i in range(len(p))) == 0:
            return {sorted_letters[i]: p[i] for i in range(len(p))}

    return None