class Allergies:
    ALLERGENS = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats"
    ]

    def __init__(self, score):
        self.score = score % 256

    def allergic_to(self, item):
        item_index = self.ALLERGENS.index(item)
        bit_value = 1 << item_index
        
        return bool(self.score & bit_value)

    @property
    def lst(self):
        return [item for item in self.ALLERGENS if self.allergic_to(item)]