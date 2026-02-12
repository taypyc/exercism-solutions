NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.direction = direction

    def move(self, instructions):
        for command in instructions:
            if command == 'R':
                self._turn_right()
            elif command == 'L':
                self._turn_left()
            elif command == 'A':
                self._advance()

    def _turn_right(self):
        self.direction = (self.direction + 1) % 4

    def _turn_left(self):
        self.direction = (self.direction - 1) % 4

    def _advance(self):
        x, y = self.coordinates
        if self.direction == NORTH:
            self.coordinates = (x, y + 1)
        elif self.direction == EAST:
            self.coordinates = (x + 1, y)
        elif self.direction == SOUTH:
            self.coordinates = (x, y - 1)
        elif self.direction == WEST:
            self.coordinates = (x - 1, y)