def label(colors):
    color_map = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    unit_index = 0
    digit1 = color_map[colors[0]]
    digit2 = color_map[colors[1]]
    multiplier = color_map[colors[2]]
    total_ohms = (digit1 * 10 + digit2) * (10 ** multiplier)
    
    while total_ohms >= 1000 and unit_index < len(units) - 1:
        total_ohms //= 1000
        unit_index += 1
        
    return f"{total_ohms} {units[unit_index]}"