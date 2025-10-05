class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

dll = DoublyLinkedList()
for i in range(1, 6):
    dll.append(i)

dll.display_forward()
dll.display_backward()

