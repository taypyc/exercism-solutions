def recite(start, take=1):
    numbers = [
        "no", "one", "two", "three", "four", "five", 
        "six", "seven", "eight", "nine", "ten"
    ]
    
    result = []
    
    for i in range(start, start - take, -1):
        current_word = "bottle" if i == 1 else "bottles"
        next_word = "bottle" if (i - 1) == 1 else "bottles"
        
        line1 = f"{numbers[i].capitalize()} green {current_word} hanging on the wall,"
        line2 = line1
        line3 = "And if one green bottle should accidentally fall,"
        line4 = f"There'll be {numbers[i-1]} green {next_word} hanging on the wall."
        
        result.extend([line1, line2, line3, line4])
        
        if i > start - take + 1:
            result.append("")
            
    return result