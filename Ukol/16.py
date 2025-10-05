import time

t = tuple(range(10**6))
l = list(range(10**6))
x = set(range(10**6))
d = {i: i for i in range(10**6)}
s = "a" * (10**6 - 1) + "z"  

start = time.time()
999999 in t
end = time.time()
print("Tuple search:", end - start, "seconds")


start = time.time()
999999 in l
end = time.time()
print("List search:", end - start, "seconds")


start = time.time()
999999 in x
end = time.time()
print("Set search:", end - start, "seconds")


start = time.time()
999999 in d
end = time.time()
print("Dict search:", end - start, "seconds")


start = time.time()
"z" in s
end = time.time()
print("String search:", end - start, "seconds")
