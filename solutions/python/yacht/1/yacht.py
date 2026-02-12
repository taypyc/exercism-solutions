from collections import Counter

YACHT = "YACHT"
ONES = 1; TWOS = 2; THREES = 3; FOURS = 4; FIVES = 5; SIXES = 6
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

def score(dice, category):
    counts = Counter(dice)
    distinct_dice = sorted(counts.keys())
    
    if isinstance(category, int):
        return counts[category] * category
    
    if category == YACHT:
        return 50 if len(counts) == 1 else 0
    
    if category == FULL_HOUSE:
        if sorted(counts.values()) == [2, 3]:
            return sum(dice)
        return 0
        
    if category == FOUR_OF_A_KIND:
        for val, count in counts.items():
            if count >= 4:
                return val * 4
        return 0

    if category == LITTLE_STRAIGHT:
        return 30 if distinct_dice == [1, 2, 3, 4, 5] else 0
        
    if category == BIG_STRAIGHT:
        return 30 if distinct_dice == [2, 3, 4, 5, 6] else 0
        
    if category == CHOICE:
        return sum(dice)
        
    return 0