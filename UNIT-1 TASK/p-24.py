print("dict() :-")
d = dict(name="Sagil", age=19)
print(d)

print("\nlen() :-")
print(len(d))

print("\nget() :-")
print(d.get("name"))

print("\nkeys() :-")
print(d.keys())

print("\nvalues() :-")
print(d.values())

print("\nitems() :-")
print(d.items())

print("\ncopy() :-")
d1 = d.copy()
print(d1)

print("\nupdate() :-")
d.update({"city": "Amreli"})
print(d)

print("\npop() :-")
d.pop("age")
print(d)

print("\npopitem() :-")
d.popitem()
print(d)

print("\nclear() :-")
d.clear()
print(d)