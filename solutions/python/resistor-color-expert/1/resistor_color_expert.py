def resistor_label(colors):
    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    tolerance_map = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    if len(colors) == 1:
        # Special case for one-band resistor
        return f"{color_map[colors[0]]} ohms"

    if len(colors) == 4:
        # Four-band resistor: [Band_1, Band_2, Multiplier, Tolerance]
        value = (color_map[colors[0]] * 10 + color_map[colors[1]]) * (10 ** color_map[colors[2]])
        tolerance = tolerance_map[colors[3]]
    elif len(colors) == 5:
        # Five-band resistor: [Band_1, Band_2, Band_3, Multiplier, Tolerance]
        value = (color_map[colors[0]] * 100 + color_map[colors[1]] * 10 + color_map[colors[2]]) * (
            10 ** color_map[colors[3]]
        )
        tolerance = tolerance_map[colors[4]]
    else:
        raise ValueError("Resistor must have 1, 4, or 5 color bands.")

    if value >= 1_000_000_000:
        unit = "gigaohms"
        value /= 1_000_000_000
    elif value >= 1_000_000:
        unit = "megaohms"
        value /= 1_000_000
    elif value >= 1_000:
        unit = "kiloohms"
        value /= 1_000
    else:
        unit = "ohms"

    # Format value to remove trailing .0 and handle decimals nicely
    # f"{value:g}" works well for this.
    return f"{value:g} {unit} ±{tolerance}"
