def sum_of_multiples(limit, factors):
    unique_multiples = set()
    
    for factor in factors:
        if factor == 0:
            continue
            
        for multiple in range(factor, limit, factor):
            unique_multiples.add(multiple)
            
    return sum(unique_multiples)