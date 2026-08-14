f = open("p-11.txt", "w")
f.write("Hello Python")
f.close()

f = open("p-11.txt", "r")
print("File Content :-")
print(f.read())
f.close()