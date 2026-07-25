a=1 #this is global var 
def myfunction(): 
    b=2     #this is local var 
    print("a = ",a)  #display global var 
    print("b = ",b)  #display local var 
myfunction() 
print(a) #available 
# print(b) #error,not available 