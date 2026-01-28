def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"

    aliquot_sum = 0
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            aliquot_sum += i
            paired_factor = number // i
            if paired_factor != number and paired_factor != i:
                aliquot_sum += paired_factor

    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"