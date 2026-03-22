def triplets_with_sum(number):
    results = []
    
    for a in range(1, number // 3):        
        numerator = number**2 - 2 * number * a
        denominator = 2 * (number - a)
        
        if numerator % denominator == 0:
            b = numerator // denominator
            c = number - a - b
            
            if a < b < c:
                results.append([a, b, c])
                
    return results