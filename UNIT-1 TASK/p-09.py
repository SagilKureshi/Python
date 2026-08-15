i = 1

print("Break Statement :-")

while i <= 5:
    if i == 4:
        break
    print(i)
    i += 1


print("\nContinue Statement :-")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("Pass Statement :-")

for i in range(1, 4):
    if i == 2:
        pass
    else:
        print("Number =", i)