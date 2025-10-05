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

    def __contains__(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False


ll = LinkedList()
for i in range(1, 6):
    ll.append(i)

ll.display()

print(3 in ll)      
print(10 in ll)     
print("Pepa" in ll) 

ll.append("Pepa")
print("Pepa" in ll) 
