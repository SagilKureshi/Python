a = {10, 20, 30}
b = {20, 30, 40}

print("add() :-")
a.add(40)
print(a)

print("\nupdate() :-")
a.update([50, 60])
print(a)

print("\ncopy() :-")
c = a.copy()
print(c)

print("\nremove() :-")
a.remove(60)
print(a)

print("\npop() :-")
a.pop()
print(a)


print("\ndiscard() :-")
a.discard(50)
print(a)


print(f"\na :- {a}\nb :- {b}")

print("\nunion() :-")
print(a.union(b))

print("\nintersection() :-")
print(a.intersection(b))


print("\ndifference() :-")
print(a.difference(b))

print("\nclear() :-")
a.clear()
print(a)