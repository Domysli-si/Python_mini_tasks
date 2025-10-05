import time

# Data
t = tuple(range(10**6))
l = list(range(10**6))
x = set(range(10**6))
d = {i: i for i in range(10**6)}
s = "a" * (10**6)

start = time.time()
val = t[500000]
end = time.time()
print("Access tuple element:", end - start, "seconds")

start = time.time()
val = l[500000]
end = time.time()
print("Access list element:", end - start, "seconds")

start = time.time()
found = 500000 in x
end = time.time()
print("Check set membership:", end - start, "seconds")

start = time.time()
val = d[500000]
end = time.time()
print("Access dict element:", end - start, "seconds")

start = time.time()
val = s[500000]
end = time.time()
print("Access string element:", end - start, "seconds")
