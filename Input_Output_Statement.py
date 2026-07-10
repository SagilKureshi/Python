# Input Output Statement

# Output Statement

#Message in print

print("Hello World!")
print("")
print(3*"Hello ")

#Concatination in print
print("City name is " + "Dubai")
print("City name is " , "Mumbai")

#Print variable in print
s,k = 10,20
print("s = ",s)
print("k = ",k)
print(s,k, sep = ",")
print(f"{s} {k}")
print("Sagil \t\t Kureshi")

#object in print

l = [1,3.3,'hello']
print(l)
s = "Smile & Happy"
print(s)

#formating in print

s = 10
print("s = %i " %s)
print("s = %d " %s)

s2 = "Hello"
print("string = %s"%s2)
print("Hello %10s"%s2)
print("%20s"%s2)

a = 10
b = 20
print("a = %d b = %d"%(a,b))

str = "helloWorld"
print("%c %c "%(str[0],str[1]))

f1 = 123.434989
f2 = 134.3429090
print("f1 = %10.2f"%f1)
print("f2 = %10.2f"%f2)

#formating

print("stud NO\t\tName\t\tFees")
print("1\t\tabc\t\t5000")
print("2\t\tabc2\t\t4000")
print("3\t\tabc3\t\t3000")