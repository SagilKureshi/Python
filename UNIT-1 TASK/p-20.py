t = (10, 20, 30, 20, 40)

print("len() :-")
print(len(t))

print("\ncount() :-")
print(t.count(20))

print("\nindex() :-")
print(t.index(30))

print("\nsorted() :-")
print(sorted(t))

print("\nmin() :-")
print(min(t))

print("\nmax() :-")
print(max(t))

# cmp() was available in Python 2, but it is removed in Python 3.
# Python 2: cmp(t1, t2)

def cmp(a, b):
    return (a > b) - (a < b)

t1 = (1, 2, 3)
t2 = (1, 2, 4)

print("\ncmp() :-")
print(cmp(t1, t2))

print("\nreversed() :-")
print(tuple(reversed(t)))