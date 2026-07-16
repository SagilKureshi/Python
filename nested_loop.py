for s in range(2):
    for k in range(3):
        print(f"s = {s}\t k = {k}")

print("pyramid using nested for loop")

for s in range(1,6):
    for k in range(1,s+1):
        print("*",end=" ")
    print()

for s in range(1,6):
    for k in range(1,s+1):
        print(s,end=" ")
    print()

for s in range(1,6):
    for k in range(1,s+1):
        print(k,end=" ")
    print()