t = (1, 2, 3, 4, 5)
l = [1, 2, 3, 4, 5]
x = {1, 2, 3, 4, 5}
d = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
s = "abcde"


try:
    t[2] = 99
except Exception as e:
    print("Tuple change error:", e)

l[2] = 99
print("List after change:", l)

try:
    x[2] = 99
except Exception as e:
    print("Set change error:", e)


d[3] = "z"
print("Dictionary after change:", d)


try:
    s[2] = "z"
except Exception as e:
    print("String change error:", e)
