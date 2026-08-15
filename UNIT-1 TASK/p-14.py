f = open("P_11.txt", "r")

for line in f:
    print(line.strip()[::-1])

f.close()