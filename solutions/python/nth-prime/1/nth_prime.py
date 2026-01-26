def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    
    primes = []
    candidate = 2
    
    while len(primes) < number:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
        
    return primes[-1]

def is_prime(n):
    if n < 2: 
        return False
    if n == 2: 
        return True
    if n % 2 == 0: 
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True