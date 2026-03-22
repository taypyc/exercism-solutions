def best_hands(hands):
    scored_hands = [(hand_rank(h), h) for h in hands]
    max_score = max(scored_hands, key=lambda x: x[0])[0]
    return [h for score, h in scored_hands if score == max_score]

def hand_rank(hand):
    cards = hand.split()
    translation = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    values = []
    for c in cards:
        v = c[:-1]
        values.append(translation.get(v) or int(v))
    
    values.sort(reverse=True)
    suits = [c[-1] for c in cards]
    
    if values == [14, 5, 4, 3, 2]:
        values = [5, 4, 3, 2, 1]
    
    counts = sorted([(values.count(v), v) for v in set(values)], reverse=True)
    counts_only = [c[0] for c in counts]
    values_only = [c[1] for c in counts]
    
    is_flush = len(set(suits)) == 1
    is_straight = len(set(values)) == 5 and (max(values) - min(values) == 4)

    if is_straight and is_flush: return (8, values_only)
    if counts_only == [4, 1]:    return (7, values_only)
    if counts_only == [3, 2]:    return (6, values_only)
    if is_flush:                 return (5, values_only)
    if is_straight:              return (4, values_only)
    if counts_only == [3, 1, 1]: return (3, values_only)
    if counts_only == [2, 2, 1]: return (2, values_only)
    if counts_only == [2, 1, 1, 1]: return (1, values_only)
    return (0, values_only)