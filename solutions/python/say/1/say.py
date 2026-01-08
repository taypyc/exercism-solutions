def say(number):
    if not 0 <= number <= 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    ones = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    scales = ["", "thousand", "million", "billion"]

    def helper(n):
        """Processes a number between 1 and 999 into words."""
        if n == 0:
            return ""
        if n < 20:
            return ones[n]
        if n < 100:
            suffix = f"-{ones[n % 10]}" if n % 10 != 0 else ""
            return tens[n // 10] + suffix
        
        hundred_part = f"{ones[n // 100]} hundred"
        remainder = helper(n % 100)
        return f"{hundred_part} {remainder}".strip()

    chunks = []
    temp_num = number
    while temp_num > 0:
        chunks.append(temp_num % 1000)
        temp_num //= 1000

    result_parts = []
    for i in range(len(chunks)):
        if chunks[i] > 0:
            chunk_words = helper(chunks[i])
            scale_word = scales[i]
            result_parts.append(f"{chunk_words} {scale_word}".strip())

    return " ".join(reversed(result_parts)).strip()