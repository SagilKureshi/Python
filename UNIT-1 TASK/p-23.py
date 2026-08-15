print("1. Creating Empty Dictionary :-")
d1 = {}
print(d1)

print("\n2. Creating Dictionary with Elements :-")
d2 = {"name": "Sagil", "age": 19}
print(d2)

print("\n3. Creating Dictionary using dict() :-")
d3 = dict(name="Sagil", age=19)
print(d3)

print("\n4. Creating Dictionary from List :-")
d4 = dict([("a", 10), ("b", 20)])
print(d4)

print("\n5. Creating Dictionary using fromkeys() :-")
d5 = dict.fromkeys(["a", "b", "c"], 0)
print(d5)