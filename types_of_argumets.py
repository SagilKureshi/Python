# #positional arguments 
# def attach(s1,s2): 
#     s3=s1+s2 
#     print("total string: "+s3) 

# attach("new","york")    #positional arguments 


#keyword arguments  
# def grocery(item,price): 

#     print("Item=",item) 
#     print("Price=",price) 

# grocery(item="sugar",price=48.50) #keyword arguments 
# grocery(price=88.00,item="Oil")  #keyword arguments


#default arguments  

# def grocery(item,price=88.00): 

#     print("item=%s"%item) 
#     print("price=%.2f"%price) 

# grocery(item="sugar",price=48.50) #keyword arguments 
# grocery(item="Oil")  #keyword arguments 


# variable length arguments


def add(farg,*args):   #*args can take 0 or more values 
    print("Formal arguments = ",farg) 
    sum=0 
    for i in args:   
        sum+=i 
    print("sum of all numbers= ",(farg+sum)) 
#call add() and pass arguments 
add(5,10) 
add(15,20,25,30) 