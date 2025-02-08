print(set("my name is Eric and Eric is my name".split()))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.difference(b))
print(b.difference(a))

print(a.union(b))

x = ["Arun", "Kumar", "Test"]
y = ["Kumar", "Passed"]

A = set(x)
B = set(y)

print(A.difference(B))
print(B.difference(A))