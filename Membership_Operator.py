l = [1,2,3,4,5]

# in operator

for i in l: 
    print(i)

s = 3
if(s in l):
    print(f"{s} is exists in list")
else:
    print(f"{s} is not exists in list")

# not operator

t = (1,2,3)

s = 5

if(s not in t):
    print(f"{s} is not exists in tuple")

else:
    print(f"{s} is exists in tuple")

text = "Python programming"
print("Python" in text)  
print("java" not in text)