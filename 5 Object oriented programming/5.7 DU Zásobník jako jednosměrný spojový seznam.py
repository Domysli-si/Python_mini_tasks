class EmptyStackException(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def add(self, data):
        if data is None:
            raise ValueError("Cannot add None to the stack")
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if not self.top:
            raise EmptyStackException("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def count(self):
        return self.size

    def clear(self):
        self.top = None
        self.size = 0

    def popAll(self):
        if not self.top:
            return []
        elements = []
        while self.top:
            elements.append(self.pop())
        return elements
