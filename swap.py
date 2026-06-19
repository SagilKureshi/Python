a = 10
b = 20 
print("before swaping")
print("a = ",a,"\nb = ",b)

#1st way
# c = a
# a = b
# b = c

#2nd way

# a = a + b # a = 10+20 = a= 30
# b = a - b # b = 30-20 = b= 10
# a = a - b # a = 30-10 = a= 20 

#3rd way
a,b = b,a
print("after swaping")
print("a = ",a,"\nb = ",b)

