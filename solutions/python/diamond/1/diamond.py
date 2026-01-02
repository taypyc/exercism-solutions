def rows(letter):
    target_idx = ord(letter) - ord('A')
    size = 2 * target_idx + 1
    
    diamond = []
    
    for i in range(size):
        dist_from_center = abs(target_idx - i)
        char_idx = target_idx - dist_from_center
        char = chr(ord('A') + char_idx)
        
        row_chars = [" "] * size
        
        left_pos = target_idx - char_idx
        right_pos = target_idx + char_idx
        
        row_chars[left_pos] = char
        row_chars[right_pos] = char
        
        diamond.append("".join(row_chars))
        
    return diamond