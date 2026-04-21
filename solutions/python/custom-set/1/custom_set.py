class CustomSet:
    def __init__(self, elements=[]):
        self.data = []
        for element in elements:
            self.add(element)

    def isempty(self):
        return len(self.data) == 0

    def contains(self, element):
        return element in self.data

    def issubset(self, other):
        return all(other.contains(item) for item in self.data)

    def isdisjoint(self, other):
        return not any(other.contains(item) for item in self.data)

    def add(self, element):
        if not self.contains(element):
            self.data.append(element)

    def intersection(self, other):
        common = [item for item in self.data if other.contains(item)]
        return CustomSet(common)

    def difference(self, other):
        diff = [item for item in self.data if not other.contains(item)]
        return CustomSet(diff)

    def union(self, other):
        combined = CustomSet(self.data)
        for item in other.data:
            combined.add(item)
        return combined

    def __sub__(self, other):
        return self.difference(other)

    def __add__(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        return self.union(other)

    def __iter__(self):
        return iter(self.data)

    def __eq__(self, other):
        if not isinstance(other, CustomSet):
            return False
        return self.issubset(other) and other.issubset(self)