f = open("p_11.txt", "w")
f.write("Hello Sagil\nBe Happy and Smile")
f.close()

f = open("p_11.txt", "r")
print("File Content in p_11.txt :-")
print(f.read())
f.close()