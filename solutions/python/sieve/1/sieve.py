import math

def primes(limit):
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for number in range(2, int(math.sqrt(limit)) + 1):
        if sieve[number]:
            for multiple in range(number * number, limit + 1, number):
                sieve[multiple] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]