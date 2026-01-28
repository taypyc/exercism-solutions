def line_up(name, number):
    last_two = number % 100
    last_digit = number % 10
    
    if 11 <= last_two <= 13:
        suffix = "th"
    elif last_digit == 1:
        suffix = "st"
    elif last_digit == 2:
        suffix = "nd"
    elif last_digit == 3:
        suffix = "rd"
    else:
        suffix = "th"
        
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"