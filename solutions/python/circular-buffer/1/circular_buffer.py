class CircularBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.read_pos = 0
        self.write_pos = 0
        self.size = 0

    def read(self):
        if self.size == 0:
            raise BufferEmptyException("Circular buffer is empty")
        value = self.buffer[self.read_pos]
        self.buffer[self.read_pos] = None
        self.read_pos = (self.read_pos + 1) % self.capacity
        self.size -= 1
        return value

    def write(self, data):
        if self.size == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.write_pos] = data
        self.write_pos = (self.write_pos + 1) % self.capacity
        self.size += 1

    def overwrite(self, data):
        if self.size < self.capacity:
            self.write(data)
        else:
            # Overwrite the oldest element (at read_pos)
            self.buffer[self.read_pos] = data
            self.read_pos = (self.read_pos + 1) % self.capacity
            self.write_pos = self.read_pos

    def clear(self):
        self.buffer = [None] * self.capacity
        self.read_pos = 0
        self.write_pos = 0
        self.size = 0


class BufferEmptyException(BufferError):
    pass


class BufferFullException(BufferError):
    pass