SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    
    if is_contained_in(list_one, list_two):
        return SUBLIST
    
    if is_contained_in(list_two, list_one):
        return SUPERLIST
        
    return UNEQUAL

def is_contained_in(small_list, big_list):
    if not small_list:
        return True
    
    len_small = len(small_list)
    len_big = len(big_list)
    
    for i in range(len_big - len_small + 1):
        if big_list[i : i + len_small] == small_list:
            return True
            
    return False