a = [10, 20, 30, 20, 40]

print("list() :-")
print(list((1, 2, 3)))

print("\nlen() :-")
print(len(a))

print("\ncount() :-")
print(a.count(20))

print("\nindex() :-")
print(a.index(30))

print("\nappend() :-")
a.append(50)
print(a)

print("\ninsert() :-")
a.insert(1, 15)
print(a)

print("\nextend() :-")
a.extend([60, 70])
print(a)

print("\nremove() :-")
a.remove(20)
print(a)

print("\npop() :-")
a.pop()
print(a)

print("\nreverse() :-")
a.reverse()
print(a)

print("\nsort() :-")
a.sort()
print(a)

print("\ncopy() :-")
b = a.copy()
print(b)

print("\nclear() :-")
a.clear()
print(a)