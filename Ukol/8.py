t = (1, 2, 3)
l = [1, 2, 3]
x = {1, 2, 3}
d = {1: "a", 2: "b"}
s = "abc"

# t[0] = 9
# s[0] = "z"


print (id(s))


s+= "Ahoj"


print (id(s))

l.append(4)

x.remove(2)
x.add(5)

d[3] = "c"
del d[1]

print("Tuple:", t)
print("List:", l)
print("Set:", x)
print("Dictionary:", d)
print("String:", s)
