num = 1
while num <= 5 :
    if num == 3:
        break
    print(num)
    num += 1

print()
for i in range(5):
    if i == 2:
        continue  # Skips the print statement for i = 2
    print(i)
