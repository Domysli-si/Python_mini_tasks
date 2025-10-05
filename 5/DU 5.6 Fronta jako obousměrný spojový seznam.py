class EmptyQueueException(Exception):
    pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def pop(self):
        if not self.head:
            raise EmptyQueueException("Queue is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return data

    def count(self):
        return self.size

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def popAll(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        self.clear()
        return elements

