t = (1, 2, 3)
l = [1, 2, 3]
x = {1, 2, 3}
d = {1: "a", 2: "b"}
s = "abc"


# del t[0]

l.remove(2)


x.discard(2)


del d[1]


# del s[0]

print("Tuple:", t)
print("List:", l)
print("Set:", x)
print("Dictionary:", d)
print("String:", s)
