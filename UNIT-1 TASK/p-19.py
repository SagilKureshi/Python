for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()

print()

for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

print()

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()