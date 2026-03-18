def is_valid(isbn):
    chars = isbn.replace("-", "")
    
    if len(chars) != 10:
        return False
    
    if not chars[:9].isdigit():
        return False
    if not (chars[9].isdigit() or chars[9] == 'X'):
        return False

    total = 0
    for i in range(10):
        if chars[i] == 'X':
            value = 10
        else:
            value = int(chars[i])
        
        weight = 10 - i
        total += value * weight
    
    return total % 11 == 0