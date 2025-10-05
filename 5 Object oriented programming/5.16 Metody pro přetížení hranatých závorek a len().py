class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Fronta:
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def add(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self._count += 1

    def pop(self):
        if not self.head:
            raise Exception("Fronta je prázdná")
        value = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self._count -= 1
        return value

    def __len__(self):
        return self._count

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Index musí být celé číslo")
        if key < 0 or key >= self._count:
            raise IndexError("Index mimo rozsah fronty")
        
        current = self.head
        for _ in range(key):
            current = current.next
        return current.data

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Index musí být celé číslo")
        if key < 0 or key >= self._count:
            raise IndexError("Index mimo rozsah fronty")
        
        current = self.head
        for _ in range(key):
            current = current.next
        current.data = value


fronta = Fronta()
fronta.add("A")
fronta.add("B")
fronta.add("C")
fronta.add("D")

print(len(fronta))    
print(fronta[2])      

fronta[0] = "Pepa"

print(fronta[0])      
print(fronta.pop())   
print(len(fronta))    
