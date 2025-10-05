t = (1, (2, 3))
l = [1, [2, 3]]
# x = {1, {2, 3}}
x = {1, frozenset({2, 3})}
d = {"a": {"b": 1}}
s = "abc" 

print("Tuple:", t)
print("List:", l)
print("Set:", x)
print("Dictionary:", d)
print("String:", s)
