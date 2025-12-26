def is_armstrong_number(number):
    digits = str(number)    
    power = len(digits)    
    sum_of_powers = sum(int(digit) ** power for digit in digits)
    return sum_of_powers == number
