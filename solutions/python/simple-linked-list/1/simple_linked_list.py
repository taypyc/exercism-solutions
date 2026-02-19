class EmptyListException(Exception):
    def __init__(self, message="The list is empty."):
        self.message = message
        super().__init__(self.message)

class Node:
    def __init__(self, value, next_node=None):
        self._value = value
        self._next = next_node

    def value(self):
        return self._value

    def next(self):
        return self._next

class LinkedList:
    def __init__(self, values=None):
        self._head = None
        self._len = 0
        
        if values:
            for value in values:
                self.push(value)

    def __iter__(self):
        current = self._head
        while current:
            yield current.value()
            current = current.next()

    def __len__(self):
        return self._len

    def head(self):
        if self._head is None:
            raise EmptyListException()
        return self._head

    def push(self, value):
        self._head = Node(value, self._head)
        self._len += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException()
        
        value = self._head.value()
        self._head = self._head.next()
        self._len -= 1
        return value

    def reversed(self):
        return LinkedList(self)