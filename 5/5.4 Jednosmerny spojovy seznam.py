class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

ll = LinkedList()
for i in range(1, 6):
    ll.append(i)
ll.display()
