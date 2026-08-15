f1 = open("p_11.txt", "r")
data = f1.read()
f1.close()

f2 = open("p_12.txt", "w")
f2.write(data)
f2.close()

f2 = open("p_12.txt", "r")
print("File copied successfully.")
print("File Content in p_12.txt :-")
print(f2.read())
f2.close()
