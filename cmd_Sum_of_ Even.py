import sys as s
args = s.argv[1:]
print("Numbers : ",args)
sum = 0
for i in args:
    s = int(i)
    if (s % 2 == 0):
        sum += s

print(sum)