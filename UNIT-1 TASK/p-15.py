f = open("p_11.txt", "r")

data = f.read()

characters = len(data)
words = len(data.split())
lines = len(data.splitlines())

f.close()

print("Number of Characters =", characters)
print("Number of Words =", words)
print("Number of Lines =", lines)