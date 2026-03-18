def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    count = 0
    for char_a, char_b in zip(strand_a, strand_b):
        if char_a != char_b:
            count += 1
            
    return count