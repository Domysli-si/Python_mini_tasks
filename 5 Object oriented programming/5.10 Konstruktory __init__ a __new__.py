class Goods:
    def __new__(cls, name, price):
        if not isinstance(name, str) or name.strip() == "":
            return None
        if not isinstance(price, (int, float)):
            return None
        if price < 0:
            return None
        return super().__new__(cls)

    def __init__(self, name, price):
        self.name = name
        self.price = price

a = Goods("Rohlik", 5)
b = Goods("", 10)
c = Goods("Freebie", "free")
d = Goods("Hackers item", -10)

print(a)  
print(b)  
print(c)  
print(d)  
