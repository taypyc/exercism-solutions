class Luhn:
    def __init__(self, card_num):
        self.raw_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.raw_num) <= 1:
            return False
        
        if not self.raw_num.isdigit():
            return False

        digits = [int(d) for d in self.raw_num]
        
        # We start at the second to last index (-2) and step backwards by 2
        for i in range(len(digits) - 2, -1, -2):
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            digits[i] = doubled

        return sum(digits) % 10 == 0