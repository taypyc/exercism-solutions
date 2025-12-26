def value(colors):
    band_values = [
        "black", "brown", "red", "orange", "yellow", 
        "green", "blue", "violet", "grey", "white"
    ]
    
    first_color = colors[0]
    second_color = colors[1]
    
    first_digit = band_values.index(first_color)
    second_digit = band_values.index(second_color)
    
    return first_digit * 10 + second_digit