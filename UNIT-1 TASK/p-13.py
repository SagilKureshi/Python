# f = open("p_11.txt", "r")
# data = f.read()
# f.close()

# count = {}

# for ch in data:
#     count[ch] = count.get(ch, 0) + 1

# print("Character Frequency :-")

# for ch in count:
#     print(ch, "=", count[ch])

f = open("P_11.txt", "r")
data = f.read()
f.close()

for ch in "abcdefghijklmnopqrstuvwxyz":
    count = data.lower().count(ch)
    if count > 0:
        print(ch, "=", count)