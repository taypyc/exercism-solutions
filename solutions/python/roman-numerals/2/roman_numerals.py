def roman(num: int) -> str:
    roman_numerals = [
        {"value": 1000, "numeral": "M"},
        {"value": 900, "numeral": "CM"},
        {"value": 500, "numeral": "D"},
        {"value": 400, "numeral": "CD"},
        {"value": 100, "numeral": "C"},
        {"value": 90, "numeral": "XC"},
        {"value": 50, "numeral": "L"},
        {"value": 40, "numeral": "XL"},
        {"value": 10, "numeral": "X"},
        {"value": 9, "numeral": "IX"},
        {"value": 5, "numeral": "V"},
        {"value": 4, "numeral": "IV"},
        {"value": 1, "numeral": "I"}
    ]

    result = ""
    for numeral_info in roman_numerals:
        while num >= numeral_info["value"]:
            result += numeral_info["numeral"]
            num -= numeral_info["value"]
    return result
